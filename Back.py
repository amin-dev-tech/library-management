import mysql.connector
import warnings
from colorama import Fore, Style
import pandas as pd

warnings.filterwarnings("ignore")


cnx = mysql.connector.connect(
    host="sql12.freemysqlhosting.net",
    database="sql12643974",
    user="sql12643974",
    password="KPCRCymhU1",
)
cursur = cnx.cursor()

if cnx.is_connected():
    print(Fore.GREEN + "Succesfuly Connected To MySQL\n")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + "Error Occured Connecting To MySQL !")
    print(Style.RESET_ALL)


# cursur.execute(
#     "CREATE TABLE Library (BookName varchar(50), Author varchar(50), Year int, ISBN int)"
# )


def selectAll():
    result = pd.read_sql("SELECT * FROM Library", con=cnx)
    return result


def insert_new(arg1, arg2, arg3, arg4):
    sql = f"INSERT INTO Library (BookName, Author, Year, ISBN) VALUES ('{arg1}', '{arg2}', '{arg3}', '{arg4}')"

    cursur.execute(sql)
    cnx.commit()

    print(cursur.rowcount, "record inserted.")


def search(isbn):
    result = pd.read_sql(
        f"SELECT * FROM Library WHERE '{int(isbn)}' = Library.ISBN", con=cnx
    )
    return result


def delete(isbn):
    sql = f"DELETE FROM Library WHERE '{int(isbn)}' = Library.ISBN"

    cursur.execute(sql)
    cnx.commit()
