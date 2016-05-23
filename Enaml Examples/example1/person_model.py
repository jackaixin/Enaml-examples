'''
Created on May 22, 2016
person_model
@author: jackaixin
'''

from atom.api import Atom, Str

class Person(Atom):
    first_name = Str()
    last_name = Str()
