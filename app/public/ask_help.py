from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app
from app.configuration import MyConfiguration
from app.public.ask_help_model import Database, Public


my_configuration = MyConfiguration()
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


@app.route('/')
def index():
    return render_template('public/ask_help.html')


@app.route('/ask_help', methods=['POST'])
def ask_help():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            # print(req)

            # check if the two id field are empty or full
            data = [
                req.get('full_name'), req.get('phone_number'), req.get('trainee_id'),
                req.get('help_type'), req.get('help_topic'), req.get('help_decs')
            ]
            # print(data)
            print(len(req.get('full_name'))>= 60)
            if len(req.get('full_name')) >= 60:
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan yaree xarfaha magacaaga. Ku soo koob wax ka yar 60 xaraf.'
                }
                print('Fadlan yaree xarfaha magacaaga.')
                res = make_response(jsonify(my_respond), 200)
                return res
            if req.get('help_type') not in ['Waxqabad', 'Cashar']:
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan dooro qaybta laguugu caawinayo ama cashar ama waqabad.'
                }
                print('Fadlan dooro qaybta laguugu caawinayo ama cashar ama waqabad.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # print(len(req.get('help_topic')))
            if len(req.get('help_topic')) > 100:
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan yaree xarfaha cinwaanka. Ku soo koob wax ka yar 100 xaraf.'
                }
                print('Fadlan yaree xarfaha cinwaanka. Ku soo koob wax ka yar 100 xaraf.')
                res = make_response(jsonify(my_respond), 200)
                return res

            # print(req.get('help_decs_chars'))
            if int(req.get('help_decs_chars')) < 300:
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Tababbarte, faahfaahintaada ugu yaraan 300 xarfo ku soo koob '
                            'si ay u fududaato inay fahmaan kuwa ku caawinayo.'
                }
                print('Fadlan badi xarfaha faahfaahintaad.')
                res = make_response(jsonify(my_respond), 200)
                return res

            if len(req.get('help_decs_chars')) >= 601:
                my_respond = {
                    'message': 'empty_data',
                    'status': 'error',
                    'text': 'Fadlan warbixinta codsigaaga ku soo koob ugu badnaan 600 xarfo.'
                }
                print('Fadlan warbixinta codsigaaga ku soo koob ugu badnaan 600 xarfo.')
                res = make_response(jsonify(my_respond), 200)
                return res

            for data in data:
                if not data:
                    my_respond = {
                        'message': 'empty_data',
                        'status': 'error',
                        'text': 'Waanu ka xunnahay tababbarte, fadlan buuxi dhammaan xogta.'
                    }
                    print('Waanu ka xunnahay tababbarte, fadlan buuxi dhammaan xogta.')
                    res = make_response(jsonify(my_respond), 200)
                    return res

            # connect to the database
            connection_status, trainee = check_public_connection()
            # Check if the id exists
            # connection_status = False
            if connection_status:
                flag1, _ = trainee.check_id(req.get('trainee_id'))
                # flag1 = False
                if flag1:
                    # check trainee number
                    full_name = trainee.get_trainee_full_name(req.get('trainee_id'))
                    flag2, _ = trainee.check_trainee_number(req.get('trainee_id'), req.get('phone_number'))
                    # flag2 = False
                    if flag2:
                        # save the data
                        flag2, _ = trainee.ask_help(
                            req.get('trainee_id'),
                            req.get('help_type'),
                            req.get('help_topic'),
                            req.get('help_decs'),
                            'pending'
                        )
                        if flag2:
                            print(f'Wanu ka xunnahay, qalad baa salka xogta ka dhacay. {_}.')
                            my_respond = {
                                'message': 'waa la diray codsiga',
                                'status': 'success',
                                'text': f'{full_name[-1]}, waa laguu diray codsigaaga caawinaadda'
                                        ' si dhaqso ah ayaa laguu soo gaari doonaa haddii Eebbe yiraahdo. '
                                        'Waanu jecelnahay inaad aqoonyahan noqotid. Mahadsanid.'
                            }
                            res = make_response(jsonify(my_respond), 200)
                            return res
                        else:
                            print(f'Wanu ka xunnahay, qalad baa salka xogta ka dhacay. {_}.')
                            my_respond = {
                                'message': 'incorrect trainee_id',
                                'status': 'error',
                                'text': f'Waanu ka xunnahay qadlad baa dhacay markaanu gudbinaynay codsigaa, '
                                        'fadlan isku day mar kale ama la xirriir maamulka. +252617306831'
                            }
                            res = make_response(jsonify(my_respond), 200)
                            return res

                    else:
                        print(f'Waanu ka xunnahay lamabrkaagu waa qalad.')
                        my_respond = {
                            'message': 'incorrect trainee_id',
                            'status': 'error',
                            'text': f'Waanu ka xunnahay lambarkaagu ({req.get('phone_number')}) waa qalad, '
                                    'fadlan hubi ama la xirriir maamulka. +252617306831'
                        }
                        res = make_response(jsonify(my_respond), 200)
                        return res
                else:
                    print(f'Waanu ka xunnahay aqoonsigaagu waa qalad.')
                    my_respond = {
                        'message': 'incorrect trainee_id',
                        'status': 'error',
                        'text': 'Waanu ka xunnahay aqoonsigaagu waa qalad, '
                                'fadlan hubi ama la xirriir maamulka. +252617306831'
                    }
                    res = make_response(jsonify(my_respond), 200)
                    return res
            else:
                print(f'BD connection problem! {trainee}')
                my_respond = {
                    'message': 'DB_con_problem',
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
