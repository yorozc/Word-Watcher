from abc import abstractmethod, ABC
from source_type import SourceType

class WordABC(ABC):

    def __init__(self,
                 term: str, 
                 definition: str,
                 context_sentence: str,
                 source_type: SourceType,
                 source_title: str,
                 source_location: str | None
                 ):
        self.id = None
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
        if isinstance(_id, int):
            self._id = _id

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term: str):
        if not isinstance(term, str):
            raise TypeError("Term must be a string.")

        if len(term) == 0:
            raise ValueError("Term cannot be empty.")
        
        self._term = term

    @property 
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        if not isinstance(definition, str):
            raise TypeError("Definition must be a string.")

        if len(definition) == 0:
            raise ValueError("Definition cannot be empty.")

        self._definition = definition

    @property
    def context_sentence(self):
        return self._context_sentence

    @context_sentence.setter
    def context_sentence(self, context_sentence: str):
        if not isinstance(context_sentence, str):
            raise TypeError("Context sentence must be a string.")

        if len(context_sentence) == 0:
            raise ValueError("Context sentence cannot be empty.")
        self._context_sentence = context_sentence

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter 
    def source_type(self, source_type: SourceType):
        if not isinstance(source_type, (SourceType, str)):
            raise TypeError("source_type must be of type SourceType(or string).")

        self._source_type = source_type

    @property
    def source_title(self):
        return self._source_title

    @source_title.setter
    def source_title(self, source_title: str):
        if not isinstance(source_title, str):
            raise TypeError("source_title must be a string.")

        if len(source_title) == 0:
            raise ValueError("source_title cannot be empty.")
        
        self._source_title = source_title

    @property
    def source_location(self):
        return self._source_location

    @source_location.setter
    def source_location(self, source_location: str):
        if not isinstance(source_location, str) and source_location is not None:
            raise TypeError("Description must be a string or None.")
        
        self._source_location = source_location
    
