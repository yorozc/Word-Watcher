from classes.word_abc import WordABC
from classes.source_type import SourceType

class Word(WordABC):

    def __init__(self, term: str, definition: str, context_sentence: str, source_type: SourceType, source_title: str, source_location: str | None):
        super().__init__(term, definition, context_sentence, source_type, source_title, source_location)