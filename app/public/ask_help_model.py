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


class Public:
    def __init__(self, connection):
        try:
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as err:
            print('Something went wrong! Internet connection or database connection.')
            print(f'Error: {err}')

    def check_id(self, trainee_id):
        sql = """
                SELECT F_name FROM trainee WHERE id = %s
                """
        try:
            self.cursor.execute(sql, (trainee_id,))
            result = self.cursor.fetchall()
            if len(result) > 0:
                print(f'Haa, wuu jiraa aqoonsiga. {(trainee_id)}.')
                return True, result
            else:
                return False, 'Lama helin aqoonsiga.'

        except Exception as e:
            print('Waanu ka xunnahay qalad baa dhacay maan soo helaynaya aqoonsiga.')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    # check if the number exists
    def check_trainee_number(self, trainee_id, trainee_number):
        sql = """
                SELECT Phone FROM trainee WHERE id = %s
                """
        try:
            self.cursor.execute(sql, (trainee_id,))
            result = self.cursor.fetchone()
            if len(result) > 0:

                # check the numer: use the last 7 digits
                print(result[0].replace(" ", ""))
                print(str(result[0].replace(" ", "")[-7:]), str(trainee_number[-7:]))
                if str(result[0].replace(" ", "")[-7:]) == str(trainee_number[-7:]):
                    print(f'Haa, wuu jiraa lambarka. {result}.')
                    return True, result
                else:
                    return False, 'Lama helin lambarka tababbartaha.'
            else:
                return False, f'lama helin lambarka tababbartaha. Aq{(trainee_id)}.'

        except Exception as e:
            print('Waanu ka xunnahay qalad baa dhacay markii aan soo helaynay lambarka.')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def ask_help(self, trainee_id, help_type, topic,
                 help_description, helping_status,
                 helper_id=1, feedback='', stars=0, helped_date=''):
        sql = """
                INSERT INTO help_request(trainee_id, help_type, topic,
                 help_description, helping_status,
                 helper_id, feedback, stars, helped_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        try:
            self.cursor.execute(sql, (trainee_id, help_type, topic,
                                      help_description, helping_status,
                                      helper_id, feedback, stars, helped_date))
            self.connection.commit()
            print('Waa la keydiyey codsiga tababbartaha Aq(trainee_id)')
            return True, f'Waa la keydiyey codsiga tababbartaha Aq(trainee_id)!'

        except Exception as e:
            print('Waa la keydiyey codsiga tababbartaha Aq(trainee_id)')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def allow_help(self, helper_id, trainee_id, request_id):
        sql = """
                UPDATE help_request SET helping_status = 'accepted', helper_id = %s
                WHERE trainee_id = %s AND id = %s
                """
        try:
            self.cursor.execute(sql, (helper_id, trainee_id, request_id))
            self.connection.commit()
            print('Waa la oggolaaday codsiga tababbartaha Aq(trainee_id)')
            return True, f'Waa la keydiyey codsiga tababbartaha Aq(trainee_id)!'

        except Exception as e:
            print('Waa la oggolaaday codsiga tababbartaha Aq(trainee_id)')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def submit_feedback_help(self, feedback, trainee_id, helper_id, request_id, stars):
        sql = """
                UPDATE help_request SET helping_status = 'helped', helper_id = %s, feedback = %s, stars = %s
                WHERE trainee_id = %s AND id = %s 
                """
        try:
            self.cursor.execute(sql, (helper_id, feedback, stars, trainee_id, request_id))
            self.connection.commit()
            print('Waa la caawiyey tababbartaha Aq(trainee_id)')
            return True, f'Waa la keydiyey codsiga tababbartaha Aq(trainee_id)!'

        except Exception as e:
            print('Waa la caawiyey tababbartaha Aq(trainee_id)')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    # Trainee can, sometimes, help his/her self
    def i_helped_myself(self, trainee_id, helper_id, request_id, feedback):
        sql = """
                UPDATE help_request SET helping_status = 'accepted', helper_id = %s, feedback = %s
                WHERE trainee_id = %s AND request_id = %s
                """
        try:
            self.cursor.execute(sql, (trainee_id, helper_id, request_id, feedback))
            self.connection.commit()
            print('Waa la oggolaaday codsiga tababbartaha Aq(trainee_id)')
            return True, f'Waa la keydiyey codsiga tababbartaha Aq(trainee_id)!'

        except Exception as e:
            print('Waa la oggolaaday codsiga tababbartaha Aq(trainee_id)')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def save_trainee_work(self, trainee_id, work_type, work_desc, materials, team_work):
        sql = """
                INSERT INTO trainee_work(trainee_id, work_type, work_desc, materials,
                 team_work) 
                VALUES (%s, %s, %s, %s, %s)
                """
        try:
            self.cursor.execute(sql, (trainee_id, work_type, work_desc, materials, team_work))
            self.connection.commit()
            print('Waa la keydiyey shaqada uu qabtay tababbartaha Aq(trainee_id)')
            return True, f'Waa la keydiyey shaqada uu qabtay tababbartaha Aq(trainee_id)!'

        except Exception as e:
            print('Waa la keydiyey shaqada uu qabtay tababbartaha Aq(trainee_id)')
            print(f'Error: {e}')
            return False, f'Error: {e}.'

    def get_trainee_full_name(self, id):
        # concatinate the first name, second name and last name when reading the data usinf CONCAT function
        sql = """
                SELECT CONCAT(F_name, ' ', S_name, ' ', L_name) AS FullName FROM trainee WHERE id = %s
                """
        try:
            self.cursor.execute(sql, (id,))
            result = self.cursor.fetchone()
            if result:
                return True, result[0]
            else:
                return False, None
        except Exception as e:
            return False, f'Error: {e}.'

    # write a functiion that checks if the tarinee is in the helper table by tarinee id. I mean I will pass trainee id
    def check_helper_and_return_fullname(self, helper_id):
        # concatinate the first name, second name and last name when reading the data usinf CONCAT function
        sql = """
                SELECT helper.Id, CONCAT(trainee.F_name, ' ', trainee.S_name, ' ', trainee.L_name) AS contact_name
                FROM helper
                JOIN trainee ON helper.trainee_id = trainee.Id
                WHERE helper.trainee_id = %s;
                """
        try:
            self.cursor.execute(sql, (helper_id,))
            result = self.cursor.fetchone()
            if result:
                return True, result
            else:
                return False, None
        except Exception as e:
            return False, f'Error: {e}.'

    def search_topics(self, trainee_id, helper_id):
        # concatenate the first name, second name and last name when reading the data using CONCAT function
        sql = """SELECT id, topic FROM help_request WHERE trainee_id = %s AND helper_id = %s AND helping_status = 'accepted';
                """
        try:
            self.cursor.execute(sql, (trainee_id, helper_id,))
            result = self.cursor.fetchall()
            if result:
                result = [dict(zip([key[0] for key in self.cursor.description], row)) for row in result]
                print("Waa la soo helay cinwaanada")
                return True, result
            else:
                return False, 'Lama soo helin cinwaannada'
        except Exception as e:
            return False, f'Error: {e}.'

    # create a function that takes one parameter (list of ids) and returns the unavailable ids else true
    # the function takes a list of ids and returns the unavailable ids
    def check_id_availability(self, id_list):
        # Assuming 'available_ids' is a table containing all available IDs
        placeholders = ', '.join(['%s'] * len(id_list))  # Create placeholders for SQL query
        sql = f"""SELECT id FROM trainee WHERE id IN ({placeholders});"""
        try:
            self.cursor.execute(sql, tuple(id_list))
            result = self.cursor.fetchall()
            # Extract the found IDs from the query result
            found_ids = [row[0] for row in result]
            unavailable_ids = [id_ for id_ in id_list if id_ not in found_ids]
            if unavailable_ids:
                print("These IDs are unavailable:", unavailable_ids)
                return False, unavailable_ids
            else:
                return True, "All IDs are available"
        except Exception as e:
            return False, f'Error: {e}'

    def check_ids_availability(self, id_list):
        # Assuming 'available_ids' is a table containing all available IDs
        placeholders = ', '.join(['%s'] * len(id_list))  # Create placeholders for SQL query
        sql = f"""SELECT id FROM trainee WHERE id IN ({placeholders}) AND status = 1;"""
        try:
            self.cursor.execute(sql, tuple(id_list))
            result = self.cursor.fetchall()
            # Extract the found IDs from the query result
            found_ids = [row[0] for row in result]
            unavailable_ids = [id_ for id_ in id_list if id_ not in found_ids]
            available_ids = [id_ for id_ in id_list if id_ in found_ids]

            # Returning a dictionary with available and unavailable IDs
            return True, {
                'available_ids': available_ids,
                'unavailable_ids': unavailable_ids
            }
        except Exception as e:
            return False, {'error': f'Error: {e}'}


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
        trainee = Public(mysql_connect.connection)

        return True, trainee
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'


if __name__ == '__main__':
    # Create an instance of the MySQLConnect class

    # # connection to the database
    print('Connecting to the database...')
    connection_status, public = check_admin_connection()
    if connection_status:
        print('You are connected to the database successfully!')
        # my_hashed_pass = admin.encript_paswrd('1423')
        # print(my_hashed_pass)
        # 30, 49, 80, 40, 97
        flag, _ = public.check_ids_availability([1000])

        if flag:
            # print(_)
            print(type(_), _)
            # send_last_phase_email(_)
            # print(len(_))
        else:
            print('False')
            print(_)

    else:
        print(f'Database Connection {public}')
