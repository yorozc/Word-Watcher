from word_abc import word_ABC
from source_type import SourceType

class Word(word_ABC):

    def __init__(self, term: str, definition: str, context_Sentence: str, source_type: SourceType, source_title: str, source_location: str | None):
        super().__init__(term, definition, context_Sentence, source_type, source_title, source_location)