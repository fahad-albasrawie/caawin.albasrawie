from flask_bcrypt import Bcrypt
from app import app
import mysql.connector
from app.configuration import MyConfiguration
from flask_bcrypt import Bcrypt
import csv
import datetime
from mysql.connector import Error


class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def make_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def my_cursor(self):
        return self.cursor


class Admin:
    def __init__(self, connection):
        try:
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as err:
            print('Something went wrong! Internet connection or database connection.')
            print(f'Error: {err}')

    # select all the help requests and join the trainee table
    # select fullname, help topic, help type, help description, helping status, feedback, stars, helped date
    # joint helper to get the helper full name.
    def get_help_requests(self):
        sql = """SELECT
                help_request.id,
                help_request.trainee_id,
                CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS trainee_fullname,
                help_request.help_type,
                help_request.topic,
                help_request.help_description,
                help_request.helping_status,
                help_request.helper_id,
                CONCAT(helper_trainee.F_name, ' ', helper_trainee.S_name, ' ', helper_trainee.L_name) AS helper_fullname,
                help_request.feedback,
                help_request.stars,
                help_request.helped_date,
                help_request.date_created AS help_request_date
            FROM
                help_request
            JOIN
                trainee ON help_request.trainee_id = trainee.Id
            JOIN
                helper ON help_request.helper_id = helper.id
            JOIN
                trainee AS helper_trainee ON helper.trainee_id = helper_trainee.Id;  
                """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                return True, result
            else:
                return False, 'Waa ay qaldan tahay qormada'
        except Exception as e:
            return False, f'Error: {e}.'

    # get only the pending requests and accepted requests
    def get_pending_and_accepted_requests(self):
        sql = """SELECT
                help_request.id,
                help_request.trainee_id,
                trainee.Phone,
                CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS trainee_fullname,
                help_request.help_type,
                help_request.topic,
                help_request.help_description,
                help_request.helping_status,
                help_request.helper_id,
                CONCAT(helper_trainee.F_name, ' ', helper_trainee.S_name, ' ', helper_trainee.L_name) AS helper_fullname,
                help_request.feedback,
                help_request.stars,
                help_request.helped_date,
                help_request.date_created AS help_request_date
            FROM
                help_request
            JOIN
                trainee ON help_request.trainee_id = trainee.Id
            JOIN
                helper ON help_request.helper_id = helper.id
            JOIN
                trainee AS helper_trainee ON helper.trainee_id = helper_trainee.Id
                WHERE help_request.helping_status = 'pending' or help_request.helping_status = 'accepted';  
                """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                return True, result
            else:
                return False, 'Waa ay qaldan tahay qormada'
        except Exception as e:
            return False, f'Error: {e}.'


    def get_pending_requests(self):
        sql = """SELECT
                help_request.id,
                help_request.trainee_id,
                CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS trainee_fullname,
                help_request.help_type,
                help_request.topic,
                help_request.help_description,
                help_request.helping_status,
                help_request.helper_id,
                CONCAT(helper_trainee.F_name, ' ', helper_trainee.S_name, ' ', helper_trainee.L_name) AS helper_fullname,
                help_request.feedback,
                help_request.stars,
                help_request.helped_date,
                help_request.date_created AS help_request_date
            FROM
                help_request
            JOIN
                trainee ON help_request.trainee_id = trainee.Id
            JOIN
                helper ON help_request.helper_id = helper.id
            JOIN
                trainee AS helper_trainee ON helper.trainee_id = helper_trainee.Id
            WHERE help_request.helping_status = 'pending';  
                """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                return True, result
            else:
                return False, 'Waa ay qaldan tahay qormada'
        except Exception as e:
            return False, f'Error: {e}.'
    def get_accepted_requests(self):
        sql = """SELECT
                help_request.id,
                help_request.trainee_id,
                CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS trainee_fullname,
                help_request.help_type,
                help_request.topic,
                help_request.help_description,
                help_request.helping_status,
                help_request.helper_id,
                CONCAT(helper_trainee.F_name, ' ', helper_trainee.S_name, ' ', helper_trainee.L_name) AS helper_fullname,
                help_request.feedback,
                help_request.stars,
                help_request.helped_date,
                help_request.date_created AS help_request_date
            FROM
                help_request
            JOIN
                trainee ON help_request.trainee_id = trainee.Id
            JOIN
                helper ON help_request.helper_id = helper.id
            JOIN
                trainee AS helper_trainee ON helper.trainee_id = helper_trainee.Id
            WHERE help_request.helping_status = 'accepted';  
                """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                return True, result
            else:
                return False, 'Waa ay qaldan tahay qormada'
        except Exception as e:
            return False, f'Error: {e}.'

    def get_helped_requests(self):
        sql = """SELECT
                help_request.id,
                help_request.trainee_id,
                CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS trainee_fullname,
                help_request.help_type,
                help_request.topic,
                help_request.help_description,
                help_request.helping_status,
                help_request.helper_id,
                CONCAT(helper_trainee.F_name, ' ', helper_trainee.S_name, ' ', helper_trainee.L_name) AS helper_fullname,
                help_request.feedback,
                help_request.stars,
                help_request.helped_date,
                help_request.date_created AS help_request_date
            FROM
                help_request
            JOIN
                trainee ON help_request.trainee_id = trainee.Id
            JOIN
                helper ON help_request.helper_id = helper.id
            JOIN
                trainee AS helper_trainee ON helper.trainee_id = helper_trainee.Id
            WHERE help_request.helping_status = 'helped';  
                """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                return True, result
            else:
                return False, 'Waa ay qaldan tahay qormada'
        except Exception as e:
            return False, f'Error: {e}.'




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


if __name__ == '__main__':
    # Create an instance of the MySQLConnect class

    # # connection to the database
    print('Connecting to the database...')
    connection_status, admin = check_admin_connection()
    if connection_status:
        print('You are connected to the database successfully!')
        # my_hashed_pass = admin.encript_paswrd('1423')
        # print(my_hashed_pass)
        # 30, 49, 80, 40, 97
        flag, _ = admin.get_pending_and_accepted_requests()

        if flag:
            # print(_)
            print(_[0].keys())
            # send_last_phase_email(_)
            # print(len(_))
        else:
            print('False')
            print(_)

    else:
        print(f'Database Connection {admin}')