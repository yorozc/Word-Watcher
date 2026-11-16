# tui.py

"""PURELY FOR TESTING FUNCTIONS BEFORE GUI IS CREATED"""

from database.db_manager import DBManager
db_m = DBManager()


def tui_run():
    db_m.create_db()