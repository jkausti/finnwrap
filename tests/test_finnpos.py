#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_finnpos
----------------------------------

Tests for `finnpos` module.
"""

import pytest


from finnwrap.finnpos import Finnpos


test_doc_enc = b'Leijat\t_\tleija\t[POS=NOUN]|[NUM=PL]|[CASE=NOM]\t_\nhelsingin\t_\thelsinki\t[POS=NOUN]|[NUM=SG]|[CASE=GEN]\t_\nyll\xc3\xa4\t_\tyll\xc3\xa4\t[POS=ADPOSITION]\t_\n.\t_\t.\t[POS=PUNCTUATION]\t_\n\nLeijat\t_\tleija\t[POS=NOUN]|[NUM=PL]|[CASE=NOM]\t_\nlensiv\xc3\xa4t\t_\tlent\xc3\xa4\xc3\xa4\t[POS=VERB]|[VOICE=ACT]|[MOOD=INDV]|[TENSE=PAST]|[PERS=PL3]\t_\n.\t_\t.\t[POS=PUNCTUATION]\t_\n\n'
test_doc_dec = test_doc_enc.decode('utf-8')


def create_object():
    test_doc_enc = b'Leijat\t_\tleija\t[POS=NOUN]|[NUM=PL]|[CASE=NOM]\t_\nhelsingin\t_\thelsinki\t[POS=NOUN]|[NUM=SG]|[CASE=GEN]\t_\nyll\xc3\xa4\t_\tyll\xc3\xa4\t[POS=ADPOSITION]\t_\n.\t_\t.\t[POS=PUNCTUATION]\t_\n\nLeijat\t_\tleija\t[POS=NOUN]|[NUM=PL]|[CASE=NOM]\t_\nlensiv\xc3\xa4t\t_\tlent\xc3\xa4\xc3\xa4\t[POS=VERB]|[VOICE=ACT]|[MOOD=INDV]|[TENSE=PAST]|[PERS=PL3]\t_\n.\t_\t.\t[POS=PUNCTUATION]\t_\n\n'
    test_doc_dec = test_doc_enc.decode('utf-8')
    
    fp = Finnpos(test_doc_dec)
    return fp

def test_object():
    
    fp = create_object()
    print(type(fp.documents))
    assert len(fp.documents) != 0
#@pytest.fixture
#def response():
#    """Sample pytest fixture.
#    See more at: http://doc.pytest.org/en/latest/fixture.html
#    """
#    # import requests
#    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
#
#
#def test_content(response):
#    """Sample pytest test function with the pytest fixture as an argument.
#    """
#    # from bs4 import BeautifulSoup
#    # assert 'GitHub' in BeautifulSoup(response.content).title.string
# -*- coding: utf-8 -*-