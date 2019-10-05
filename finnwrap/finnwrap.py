# -*- coding: utf-8 -*-

from spacy.lang.fi import Finnish
from subprocess import Popen, PIPE
from finnwrap.finnpos import Finnpos
import json

class Finnwrap():
    
    def __init__(self, documents):
        self.documents = []
        self.fp = ''
        
        if isinstance(documents, list):
            for i in documents:
                if isinstance(i, str):
                    self.documents.append(i)
                else:
                    raise ValueError('ValueError: List objects need to be of type string.')
        elif isinstance(documents, str):
            self.documents.append(documents)
        else:
            raise ValueError('ValueError: Input needs to be a string or a list.')
        
    
    def analyze(self, docs='all'):
        
        scope = []
        if docs == 'all':
            scope = self.documents
        elif isinstance(docs, list):
            for i in docs:
                if isinstance(i, int):
                    scope.append(self.documents[i])
                else:
                    raise ValueError('ValueError: Input to this method needs to be a list of integers or \'all\'.')
        else:
            raise ValueError('ValueError: Input to this method needs to be a list of integers or \'all\'.')
                    
        
        preprocessed = self._preprocess_input(scope)
        analyzed = []
        
        for doc in preprocessed:
            process = Popen(['ftb-label'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate(input=doc.encode('utf-8'))
            analyzed.append(stdout.decode())
        
        processed = Finnpos(analyzed)
        
        self.fp = processed
    
    
    def _preprocess_input(self, docs):
        nlp = Finnish()
        nlp.add_pipe(nlp.create_pipe('sentencizer'))
        
        documents = []
        
        for doc in docs:
            nlp_doc = nlp(doc)
            sentences = [x for x in nlp_doc.sents]
            sents = []
                
            for sent in sentences:
                spac_obj = nlp(sent.text)
                sents.append(" ".join([tok.text for tok in spac_obj]))
            
            sents = "  ".join(sents)
            sents = sents.replace(" ", "\n")
            documents.append(sents)
        
        return documents

if __name__ == '__main__':
    
    fw = Finnwrap(['Leijat helsingin yllä. Leijat lensivät.', 'Ajatuspaja libera.'])
    fw.analyze()
    print(fw.fp.getJson().decode('utf-8'))