#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_finnwrap
----------------------------------

Tests for `finnwrap` module.
"""

import pytest

from finnwrap.finnwrap import Finnwrap
from finnwrap.finnpos import Finnpos


def test_init_strandlistinputs():
    
    input_str = 'This is a document.'
    input_list = ['This string is inside a list.', 'This is the second string.']

    fw1 = Finnwrap(input_str)
    fw2 = Finnwrap(input_list)
    
    assert type(fw1.documents) == type(fw2.documents)

def test_init_integerinput():
    
    input_int = 45
    
    with pytest.raises(ValueError) as err:
        fw1 = Finnwrap(input_int)
    
    assert 'ValueError' in str(err.value)

def test_init_with_mixed_type_list():
    
    input_list_int = ['This is a string but the next one is an int.', 45]
    
    with pytest.raises(ValueError) as err:
        fw1 = Finnwrap(input_list_int)
    
    assert 'ValueError' in str(err.value)
    
def test_analyze_all_docs():
    
    fw = Finnwrap(['Leijat helsingin yllä. Tämä on toinen lause.', 'Tämä on toinen dokumentti.'])
    fw.analyze()
    
    assert type(fw.fp) == Finnpos

def test_analyze_some_docs():
    
    fw = Finnwrap(['Leijat helsingin yllä. Tämä on toinen lause.', 'Tämä on toinen dokumentti.'])
    fw.analyze(docs = [0])
    
    assert len(fw.fp.documents) == 1

#def test_analyze():
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
