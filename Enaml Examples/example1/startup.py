'''
Created on May 22, 2016
Enaml App entry point
@author: jackaixin
'''

import enaml
from enaml.qt.qt_application import QtApplication

from person_model import Person


if __name__ == '__main__':
    with enaml.imports():
        from person_view import PersonView

    jack = Person(first_name='Jack', last_name='Zhang')

    app = QtApplication()

    view = PersonView(person=jack)
    view.show()

    app.start()