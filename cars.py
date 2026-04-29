import sqlite3

DATABASE = 'cars_database.db'


def print_all_cars():
    speed = input('What speed: ')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = 'SELECT car_name,top_speed FROM cars WHERE top_speed > ?;'
        cursor.execute(sql, (speed,))
        results = cursor.fetchall()
        # print results so they look good

        for car in results:
            print(f'Car name: {car[0]}    Top speed: {car[1]}')


if __name__ == '__main__':
    print_all_cars()
