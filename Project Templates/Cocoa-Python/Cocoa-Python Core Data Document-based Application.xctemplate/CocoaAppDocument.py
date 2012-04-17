#-*- coding: utf-8 -*-
#
#  ___PROJECTNAMEASIDENTIFIER___Document.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright ___ORGANIZATIONNAME___ ___YEAR___. All rights reserved.
#

from Foundation import *
from CoreData import *
from AppKit import *

class ___VARIABLE_classPrefix___Document(NSPersistentDocument):
    def init(self):
        self = super(___VARIABLE_classPrefix___Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"___VARIABLE_classPrefix___Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(___VARIABLE_classPrefix___Document, self).windowControllerDidLoadNib_(aController)
        # user interface preparation code
