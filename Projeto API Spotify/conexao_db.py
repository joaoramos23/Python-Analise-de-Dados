import pyodbc

def connect_db(DATABASE):
    connect_data = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-H8S3ID2;"
        f"Database={DATABASE};"
        "UID=sa;"
        "PWD=klo5s871", autocommit=True)
    print("Conexão Concluida!")
    return connect_data


def create_cursor(connect):
    cursor_data = connect.cursor()
    return cursor_data
