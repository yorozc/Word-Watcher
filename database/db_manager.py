import sqlite3
from classes.word import Word

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
    
    def add_word(self, word: Word) -> None:
        query = """
                INSERT INTO words (term, definition, context_sentence, source_type, source_title, source_location) VALUES (?, ?, ?, ?, ?, ?)
                """
        with sqlite3.connect(self._db_name) as conn:
            c = conn.cursor()

            c.execute(query, (word.term, word.definition, word.context_sentence, word.source_type, word.source_title, word.source_location))
            word.id = c.lastrowid


    # TODO: delete word via: name or id
    def del_word(self):
        pass

    # TODO: edit word via name or id
    def edit_word(self):
        pass

    # TODO: get word via name or id
    # get all words via some metric through the sorting queries below
    def get_word(self):
        pass

    def get_all_words(self) -> list:
        query = """
                SELECT * FROM words;
                """
        with sqlite3.connect(self._db_name) as conn:
            c = conn.cursor()
            c.execute(query)
            word_data = c.fetchall()

        return word_data

    # sorting queries

    def sort_by_alphabet(self):
        pass

    def sort_by_type(self):
        pass

    def sort_by_title(self):
        pass

    def sort_by_date(self):
        pass


