'''
Created on May 22, 2016
person_model
@author: jackaixin
'''

from atom.api import Atom, Unicode

class Person(Atom):
    first_name = Unicode()
    last_name = Unicode()
