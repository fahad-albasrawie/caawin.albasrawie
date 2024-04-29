from datetime import datetime

from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app
from app.configuration import MyConfiguration
from app.admin.dashboard_model import Database, Admin
from app.public.ask_help_model import Database, Public


def format_time_ago(timestamp):
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
    time_difference = datetime.now() - timestamp
    minutes = int(time_difference.total_seconds() / 60)

    if minutes < 1:
        return 'just now'
    elif minutes == 1:
        return '1 minute ago'
    elif minutes < 60:
        return f'{minutes} minutes ago'
    elif minutes < 1440:
        hours = int(minutes / 60)
        return f'{hours} hours ago'
    else:
        days = int(minutes / 1440)
        return f'{days} days ago'

# Registering the function as a Jinja filter
app.jinja_env.filters['format_time_ago'] = format_time_ago

my_configuration = MyConfiguration()


def check_admin_connection():
    try:
        mysql_connect = Database(
            host=my_configuration.DB_HOSTNAME,
            port=3306,
            user=my_configuration.DB_USERNAME,
            password=my_configuration.DB_PASSWORD,
            database=my_configuration.DB_NAME
        )
        # Create an instance of the Store class
        mysql_connect.make_connection()
        trainee = Admin(mysql_connect.connection)

        return True, trainee
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'


def check_public_connection():
    try:
        mysql_connect = Database(
            host=my_configuration.DB_HOSTNAME,
            port=3306,
            user=my_configuration.DB_USERNAME,
            password=my_configuration.DB_PASSWORD,
            database=my_configuration.DB_NAME
        )
        # Create an instance of the Store class
        mysql_connect.make_connection()
        trainee = Public(mysql_connect.connection)

        return True, trainee
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'

@app.route('/oggolow')
def open_accept_help_page():
    # connect to the database
    print('Connecting to the database...')
    connection_status, admin = check_admin_connection()
    data = {}
    if connection_status:

        print('Connected to the database successfully!')
        # get help requests
        flag, pending_and_accepted_requests = admin.get_pending_and_accepted_requests()
        if flag:
            if not pending_and_accepted_requests:
                print('No help requests!')
                data = {
                    'help_requests': []
                }
                return render_template('admin/dashboard.html', data=data)

            # calculate the number of help requests by status
            # Initialize a dictionary to store the count of each status, starting all counts at 0
            status_counts = {'pending': 0, 'accepted': 0}
            # Loop through each item in the list
            for item in pending_and_accepted_requests:
                # Get the status from the dictionary
                status = item['helping_status']
                # Check if the status is one of the ones we're tracking
                if status in status_counts:
                    # If it is, increment its count
                    status_counts[status] += 1
            print(status_counts)
            data = {
                'pending_and_accepted_requests': pending_and_accepted_requests[::-1],
                'status_counts': status_counts
            }
            return render_template('public/accept_help.html', data=data)
        else:
            print('Failed to get the help requests!')
            data = {}
            return render_template('public/accept_help.html', data=data)

    else:
        print('Failed to connect to the database!')
        return render_template('public/accept_help.html', data=data)


@app.route('/accept_helping', methods=['POST'])
def accept_helping():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            print(req)

            if not req.get('helper_id'):
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay caawiye, fadlan soo gali aqoonsigaaga.'
                }
                print('Waanu ka xunnahay caawiye, fadlan soo gali aqoonsigaaga.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # connect to the database
            print('Connecting to the database...')
            connection_status, public = check_public_connection()
            if connection_status:
                print('Connected to the database successfully!')
                # get help requests
                # check if the helper_id is in the helpers table
                flag, helper_full_name_and_id = public.check_helper_and_return_fullname(req.get('helper_id'))
                if flag:

                    # Save data
                    flag1, _ = public.allow_help(
                        helper_full_name_and_id[0],
                        trainee_id=req.get('trainee_id'),
                        request_id=req.get('request_id')
                    )

                    if flag1:
                        my_respond = {
                            'message': 'data_not_js',
                            'status': 'success',
                            'text': f'Mahadsanid {helper_full_name_and_id[-1]}. Hoose waxaa ku xusan xogta qofka la caawinayo. Fadlan la xirriir.',
                            'helper_full_name': helper_full_name_and_id[-1]
                        }
                        res = make_response(jsonify(my_respond), 200)
                        return res

                    my_respond = {
                        'message': 'data_not_js',
                        'status': 'error',
                        'text': 'Waanu ka xunnahay qalad baa dhacay, '
                                'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res


                else:
                    my_respond = {
                        'message': 'data_not_js',
                        'status': 'error',
                        'text': f'Waanu ka xunnahay caawiye, aqoonsigaan "{req.get('helper_id')}" ka mid ma aha caawiyayaasha, '
                                'si caawiye ahaan laguu diiwaangeliyo fadlan la xirriir maamulka. +252617306831'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res

            else:
                my_respond = {
                    'message': 'data_not_js',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay qalad baa dhacay, '
                            'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                }
                res = make_response(jsonify(my_respond), 200)
                return res

        else:
            my_respond = {
                'message': 'data_not_js',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res
    return "Waanu ka xunnahay, waxaan u malaynaynaa in boggani aanu ahayn kan aad rabtay!"


@app.route('/search_helping_topics', methods=['POST'])
def search_helping_topics():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            print(req)

            if not req.get('helper_id') and not req.get('trainee_id'):
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.'
                }
                print('Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # connect to the database
            print('Connecting to the database...')
            connection_status, public = check_public_connection()
            if connection_status:
                print('Connected to the database successfully!')
                # get help requests
                # check if the helper_id is in the helpers table
                flag, topics = public.search_topics(req.get('trainee_id'), req.get('helper_id'))
                if flag:

                    my_respond = {
                        'message': 'data_not_js',
                        'status': 'success',
                        'text': f'Mahadsanid tababbarte, "gacmo wadajir bay wax ku gooyaan" mar kasta waanu isla jiraynaa, waanu isla kobcaynaa waanu is-caawinaynaa. '
                                f'"Haddaynaan is-taakulin tabar yeelan maynee *** Ka tashada cadaawuhu isku tiirsanaada"!',
                        'topics': topics
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res


                else:
                    my_respond = {
                        'message': 'incorrect data or db error.',
                        'status': 'error',
                        'text': f'Waanu ka xunnahay xog lama soo helin. Falan hubi aqoonsiyaasha. Haddii kale la xirriir maamulka. +252617306831. '
                                f'Fiirmo gaar: Aqoonsiga caawiyaha waa aqoonsiga cusub ee loogu diiwaangeliyey caawiye ahaan.'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res

            else:
                my_respond = {
                    'message': 'data_not_js',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay qalad baa dhacay, '
                            'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                }
                res = make_response(jsonify(my_respond), 200)
                return res

        else:
            my_respond = {
                'message': 'data_not_js',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res
    return "Waanu ka xunnahay, waxaan u malaynaynaa in boggani aanu ahayn kan aad rabtay!"

@app.route('/submit_help_feedback', methods=['POST'])
def submit_help_feedback():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            print(req)

            if not req.get('helper_id'):
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay caawiye, fadlan soo gali aqoonsigaaga.'
                }
                print('Waanu ka xunnahay caawiye, fadlan soo gali aqoonsigaaga.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # connect to the database
            print('Connecting to the database...')
            connection_status, public = check_public_connection()
            if connection_status:
                print('Connected to the database successfully!')
                # get help requests
                # check if the helper_id is in the helpers table
                flag, helper_full_name_and_id = public.submit_feedback_help(
                    req.get('feedback'),
                    req.get('trainee_id'),
                    req.get('helper_id'),
                    req.get('request_id'),
                    req.get('stars')
                )
                if flag:
                    my_respond = {
                        'message': 'data_not_js',
                        'status': 'success',
                        'text': f'Mahadsanid tababbarte, "gacmo wadajir bay wax ku gooyaan" mar kasta waanu isla jiraynaa, waanu isla kobcaynaa waanu is-caawinaynaa. '
                                f'"Haddaynaan is-taakulin tabar yeelan maynee *** Ka tashada cadaawuhu isku tiirsanaada"!'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res

                my_respond = {
                    'message': 'data_not_js',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay qalad baa dhacay, '
                            'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                }
                res = make_response(jsonify(my_respond), 200)
                return res

            else:
                my_respond = {
                    'message': 'data_not_js',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay qalad baa dhacay, '
                            'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                }
                res = make_response(jsonify(my_respond), 200)
                return res

        else:
            my_respond = {
                'message': 'data_not_js',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res
    return "Waanu ka xunnahay, waxaan u malaynaynaa in boggani aanu ahayn kan aad rabtay!"


@app.route('/dir_hawl')
def open_submit_page():
    return render_template('public/submit_work.html')


@app.route('/submit_work', methods=['POST'])
def submit_work():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            print(req)

            if not req.get('work_type') or req.get('work_type') == "Dooro hawlmaalmeedka":
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay tababbarte, fadlan soo gali nooca shaqada (Waxqabad, Cashar Naqtiimin ama baraatiko).'
                }
                print('Waanu ka xunnahay tababbarte, fadlan soo gali nooca shaqada (Waxqabad, Cashar Naqtiimin ama baraatiko).')
                res = make_response(jsonify(my_respond), 200)
                return res

            if not req.get('google_drive'):
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan buuxi godka lifaaqa (link-ga) GoogleDrive.'
                }
                print('Fadlan buuxi godka lifaaqa (link-ga) GoogleDrive.')
                res = make_response(jsonify(my_respond), 200)
                return res

            if not req.get('wok_sender_id'):
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan buuxi godka aqoonsiga.'
                }
                print('Fadlan buuxi godka aqoonsiga.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # connect to the database
            print('Connecting to the database...')
            connection_status, public = check_public_connection()
            if connection_status:
                print('Connected to the database successfully!')
                # get help requests

                # filter the ids, the ids are strings, "12,34,5" or could be ",12,34,2" or "12,34,2,". So convert into list of integers
                work_sender_id = [int(i) for i in req.get('wok_sender_id').split(',') if i]

                # check if the ids are in the database
                flag, id_availability = public.check_ids_availability(work_sender_id)
                if flag:
                    # Check if the all ids are not available
                    if not id_availability.get('available_ids'):
                        if len(work_sender_id) > 1:
                            my_respond = {
                                'message': 'data_not_js',
                                'status': 'error',
                                'text': f'Waanu ka xunnahay waa ay qaldanyihiin dhammaan aqoonsiyadiina "{id_availability.get('unavailable_ids')}", fadlan hubiya.'
                            }
                            res = make_response(jsonify(my_respond), 200)
                            return res
                        my_respond = {
                            'message': 'data_not_js',
                            'status': 'error',
                            'text': f'Waanu ka xunnahay tababbarte, aqoosiga aad soo galisay "{work_sender_id}" ma ahan mid jira.'
                        }
                        res = make_response(jsonify(my_respond), 200)
                        return res

                    # Save data
                    for trainee_id in id_availability.get('available_ids'):
                        flag1, _ = public.save_trainee_work(
                            trainee_id,
                            req.get('work_type'),
                            req.get('work_desc'),
                            req.get('google_drive'),
                            req.get('team_work'),
                        )
                        if flag1:
                            print(f"Waa la keydiyey shaqada tababbartaha: Aq{trainee_id}")
                        else:
                            my_respond = {
                                'message': 'data_not_js',
                                'status': 'error',
                                'text': 'Waanu ka xunnahay qalad baa dhacay, marka la gudbinayey waxqabadka.'
                                        'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                            }
                            res = make_response(jsonify(my_respond), 200)
                            return res

                    # check if there are unavailable ids
                    if id_availability.get('unavailable_ids'):
                        unavailable_ids = id_availability.get('unavailable_ids')
                    else:
                        unavailable_ids = False

                    my_respond = {
                        'message': 'Data Saved Successfully!',
                        'status': 'success',
                        'individual_message': f'Fiican tababbarte, hawl laguugu mahadnaqaya ayaad qabatay. Waanu kuu keydinay hawshaada waana laguugu abaalgudayaa.',
                        'team_message': f'Oow, fiican! Waxaanu aad ugu faraxsannahay inaad koox-koox u shaqayseen. "Gacmo wadjir bay wax ku gooyaan". '
                                        f'Waxaad qabateen kooxdiinna hawl la idiinku mahadcelinayo waana   la idiinku abaalgudayaa.',
                        'team_work': req.get('team_work'),
                        'unavailable_ids': unavailable_ids
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res

                else:
                    my_respond = {
                        'message': 'data_not_js',
                        'status': 'error',
                        'text': 'Waanu ka xunnahay qalad baa dhacay, '
                                'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res


            else:
                my_respond = {
                    'message': 'data_not_js',
                    'status': 'error',
                    'text': 'Waanu ka xunnahay qalad baa dhacay, '
                            'fadlan hubi qadkaaga ama la xirriir maamulka. +252617306831'
                }
                res = make_response(jsonify(my_respond), 200)
                return res

        else:
            my_respond = {
                'message': 'data_not_js',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res
    return "Waanu ka xunnahay, waxaan u malaynaynaa in boggani aanu ahayn kan aad rabtay!"
