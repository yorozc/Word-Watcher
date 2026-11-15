import sqlite3

class DBManager:
    def __init__(self):
        self._db_name = "wordRepo.db"

    def create_db(self):

        with sqlite3.connect(self._db_name) as conn:
            c = conn.cursor()

            c.execute(
            """
            CREATE TABLE IF NOT EXISTS words(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                term TEXT NOT NULL,
                definition TEXT NOT NULL,
                context_sentence TEXT NOT NULL,
                source_type TEXT NOT NULL, 
                source_title TEXT NOT NULL,
                source_location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            )

    # basic crud 
    
    def add_word(self):
        pass

    def del_word(self):
        pass

    def edit_word(self):
        pass

    def get_word(self):
        pass

    def get_all_words(self):
        pass

    # sorting queries

    def sort_by_alphabet(self):
        pass

    def sort_by_type(self):
        pass

    def sort_by_title(self):
        pass

    def sort_by_date(self):
        pass


