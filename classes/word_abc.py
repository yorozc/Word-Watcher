from abc import abstractmethod, ABC
from source_type import Source_Type

class WordABC(ABC):

    def __init__(self,
                 term: str, 
                 definition: str,
                 context_sentence: str,
                 source_type: Source_Type,
                 source_title: str,
                 source_location: str
                 ):
        self._id = None
        self.term = term
        self.definition = definition
        self.context_sentence = context_sentence
        self.source_type = source_type
        self.source_title = source_title
        self.source_location = source_location

    # TODO: provide validation before value is set

    @property
    def id(self):
        return self._id 

    @id.setter
    def id(self, _id: int):
        self._id = _id

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term: str):
        self._term = term

    @property 
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        self._definition = definition

    @property
    def context_sentence(self):
        return self._context_sentence

    @context_sentence.setter
    def context_sentence(self, context_sentence: str):
        self._context_sentence = context_sentence

    
