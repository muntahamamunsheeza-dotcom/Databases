# Import the libraries to connect to the database and present the information in tables
import sqlite3
from easygui import easygui

# This is the filename of the database to be used
DB_NAME = 'music_lesson.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(easygui(results,headings))
    db.close()

# Import the libraries to connect to the database and present the information in tables
import sqlite3
from easygui import easygui

# This is the filename of the database to be used
DB_NAME = 'music_lesson.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" music_lesson "
           "LEFT JOIN school_id ON music_lesson.school_id = school_id.school_id "
           "LEFT JOIN parent_surname_id ON music_lesson.parent_surname_id = parent_surname_id.parent_surname_id "
           "LEFT JOIN lesson_day_id ON music_lesson.lesson_day_id = lesson_day_id.lesson_day_id "
            "LEFT JOIN instrument_id ON music_lesson.instrument_id = instrument_id.instrument_id "
            "LEFT JOIN child_surname_id ON music_lesson.child_surname_id = child_surname_id.child_surname_id")
def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(easygui(results,fields.split(",")))
    db.close()  



make = input('Which lesson days info do you want to see: ')
print_parameter_query("model, top_speed", "make = ? ORDER BY top_speed DESC",make)


menu_choice = ''
while menu_choice != 'Z':
    try:
        ask = input('Type a letter for the following information and press "Z" to exit ')
    except ValueError:
        print('Invalid, please try again')
    menu_choice = input('Welcome to the music lessons database\n\n'
                        'Type the letter for the information you want\n'
                        'A: Information for the monday lesson for children\n' \
                        'B: Gives all the children information for music lessons/n' \
                        'C: Inofrmation of children who is doing Friday lessons\n' \
                        'D: Inofrmation for Tuesday lessons\n' \
                        'E: Information for Thursday lessons\n')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('monday_lessons')
    elif menu_choice == 'B':
        print_query('child_info')
    elif menu_choice == 'C':
        print_query('friday_lessons')
    elif menu_choice == 'D':
        print_query('thrusday_lessons')
    elif menu_choice == 'E':
        print_query('tuesday_lessons')
    
    


