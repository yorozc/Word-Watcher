# tui.py

"""PURELY FOR TESTING FUNCTIONS BEFORE GUI IS CREATED"""

from database.db_manager import DBManager
from classes.word import Word
db_m = DBManager()


def tui_run():
    # print(db_m.get_all_words())
    # print("Add word test:")
    # input_term = input("Insert term: ")
    # input_def = input("Insert definition: ")
    # input_context_sentence = input("Insert context sentence: ")
    # input_source_type = input("Insert source type (book, website, article, paper, other): ")
    # input_source_title = input("Insert source title: ")
    # input_source_location = input("Insert source location (optional): ")

    # new_word = Word(input_term, input_def, input_context_sentence, input_source_type, input_source_title, input_source_location)

    # db_m.add_word(new_word)

    print(db_m.get_all_words())

    word = input("Insert term to get word: ")
    word = db_m.get_word_name(word)

    print(word)


