# -*- coding: utf-8 -*-

import io
import json

class Finnpos():
    
    def __init__(self, docs):        
        
        self.documents = self._interpret_docs(docs)
    
    def _interpret_docs(self, docs):
            
        if isinstance(docs, str):
            return [self._process_doc(docs)]
        elif isinstance(docs, list):
            pr_docs = []
            for doc in docs:
                pr_docs.append(self._process_doc(doc))
            return pr_docs
        
    def _process_doc(self, doc):
            
        pr_doc = self.Doc()
            
        sentences = doc.split("\n\n")
        for sent in sentences:
            if sent == '':
                break
            pr_sent = self.Sent()
            doc = io.StringIO(sent)
        
            while (True):
                line = doc.readline()
                if line == '':
                    break
                pr_sent.tokens.append(self.Token(line))
                
            for tok in pr_sent.tokens:
                pr_sent.sentence += tok.word + ' '
                
            pr_doc.sents.append(pr_sent)
        
        for sent in pr_doc.sents:
            pr_doc.document += sent.sentence + " "
        
        return pr_doc
    
    def getJson(self):
        #module returns a json-object of all of the objects content
        response = {'response':''}
        documents = {'documents':[]}
        
        for doc in self.documents:
            sentences = {'sentences':[]}
            
            for sent in doc.sents:
                tokens = {'tokens':[]}
                
                for tok in sent.tokens:
                    token = {'word':tok.word,
                             'lemma':tok.lemma,
                             'tags':tok.tags}
                    tokens['tokens'].append(token)
                sentences['sentences'].append(tokens)
            documents['documents'].append(sentences)
        response['response'] = documents
        
        return json.dumps(response, indent=4, ensure_ascii=False).encode('utf-8')
    
    class Doc():
        
        def __init__(self):
            self.document = ''
            self.sents = []
            
        def getTokens(self):                    
            return [token for sent in self.sents for token in sent]
                    
    
    class Sent():
        
        def __init__(self):
            self.sentence = ""
            self.tokens = []
            
    
    class Token():
        
        def __init__(self, row):
            self.row = row
            self.word = ''
            self.lemma = ''
            self.tags = {}
            
            self.process_row(row)
            
        def process_row(self, row):
            parts = row.split('\t')
            self.row = row
            self.word = parts[0]
            self.lemma = parts[2]
            
            
#            print(token, lemma)
            for tag in parts[3].split('|'):
                spl_tag = tag.split('=')
                self.tags[spl_tag[0][1:]] = spl_tag[1][:-1]
            
                
            
    
            