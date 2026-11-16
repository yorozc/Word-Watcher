
from tui.interface import tui_run
from database.db_manager import DBManager

db_m = DBManager()

if __name__ == "__main__":
    db_m.create_db()
    tui_run()