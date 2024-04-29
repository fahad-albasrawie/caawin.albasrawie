from flask import render_template, session, redirect, url_for, request, make_response, jsonify
from app import app
from app.configuration import MyConfiguration
from app.admin.dashboard_model import Database, Admin


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


@app.route('/maamulka/looxa')
def dashboard():
    # connect to the database
    print('Connecting to the database...')
    connection_status, admin = check_admin_connection()
    data = {}
    if connection_status:

        print('Connected to the database successfully!')
        # get help requests
        flag, help_requests = admin.get_help_requests()
        if flag:
            if not help_requests:
                print('No help requests!')
                data = {
                    'help_requests': []
                }
                return render_template('admin/dashboard.html', data=data)

            # calculate the number of help requests by status
            # Initialize a dictionary to store the count of each status, starting all counts at 0
            status_counts = {'pending': 0, 'accepted': 0, 'helped': 0}
            # Loop through each item in the list
            for item in help_requests:
                # Get the status from the dictionary
                status = item['helping_status']
                # Check if the status is one of the ones we're tracking
                if status in status_counts:
                    # If it is, increment its count
                    status_counts[status] += 1
            print(status_counts)
            data = {
                'help_requests': help_requests[::-1],
                'status_counts': status_counts
            }
            return render_template('admin/dashboard.html', data=data)
        else:
            print('Failed to get the help requests!')
            data = {}
            return render_template('admin/dashboard.html', data=data)

    else:
        print('Failed to connect to the database!')
        return render_template('admin/dashboard.html', data=data)
