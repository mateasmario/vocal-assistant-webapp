from django.shortcuts import render
import pymysql

# Create your views here.

def index_view(request):
    connection = pymysql.connect(host="", user="", password="", database="", cursorclass=pymysql.cursors.DictCursor)

    result = None

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM MESSAGES"
        cursor.execute(sql)

        lst = []

        while True:
            result = cursor.fetchone()
            if result is not None:
                lst.append(result)
            else:
                break

    return render(request, "index.html", {"messages": lst})