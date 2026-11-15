# tui.py

"""PURELY FOR TESTING FUNCTIONS BEFORE GUI IS CREATED"""

from database.db_manager import DBManager
db_m = DBManager()


def run():
    db_m.create_db()