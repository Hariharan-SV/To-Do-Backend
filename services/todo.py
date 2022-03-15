from db import get_db_cursor


def handle_todos(body):
    _, my_cursor = get_db_cursor()
    my_cursor.execute("SELECT * from ToDo WHERE user_id="+str(body['id'])+";")
    results = my_cursor.fetchall()
    my_cursor.close()
    t = []
    for r in results:
        s = {}
        s['id'], s['description'], s['startDateTime'], s['endDateTime'] = r[0], r[2], r[3], r[4]
        t.append(s)
    return {'result': t}

def handle_todo_add(body):
    mydb, my_cursor = get_db_cursor()
    my_cursor.execute("INSERT INTO ToDo(user_id,description,start_date_time,end_date_time) VALUES ('"
    +str(body['id'])+"','"+str(body['description'])+"','"+str(body['startDateTime'])+"','"+str(body['endDateTime'])+"');")
    results = my_cursor.fetchall()
    my_cursor.close()
    mydb.commit()
    return {'result': results}

def handle_todo_edit(body):
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
