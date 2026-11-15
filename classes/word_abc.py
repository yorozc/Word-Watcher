from abc import abstractmethod, ABC

class word_ABC(ABC):

    def __init__(self,
                 term: str, 
                 definition: str,
                 context_sentence: str,
                 source_type: str,
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
    def id(self, _id):
        self._id = _id

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term):
        self._term = term

    @property 
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, definition):
        self._definition = definition

    @property
    def context_sentence(self):
        return self._context_sentence

    @context_sentence.setter
    def context_sentence(self, context_sentence):
        self._context_sentence = context_sentence
