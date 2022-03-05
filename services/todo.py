from db import get_db_cursor


def handle_todos(body):
    _, my_cursor = get_db_cursor()
    my_cursor.execute("SELECT * from ToDo WHERE user_id="+str(body['id'])+";")
    results = my_cursor.fetchall()
    my_cursor.close()
    t = []
    for r in results:
        s = {}
        s['id'], s['description'], s['startDate'], s['endDate'] = r[0], r[2], r[3], r[4]
        t.append(s)
    return {'result': t}
