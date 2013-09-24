#-*- coding: utf-8 -*-
#
#  ___PROJECTNAMEASIDENTIFIER___Document.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
#

from Foundation import *
from AppKit import *

class ___VARIABLE_classPrefix:identifier___Document(NSDocument):
    def init(self):
        self = super(___VARIABLE_classPrefix:identifier___Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"___VARIABLE_classPrefix:identifier___Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(___VARIABLE_classPrefix:identifier___Document, self).windowControllerDidLoadNib_(aController)

    def dataOfType_error_(self, typeName, outError):
        return None, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
    
    def readFromData_ofType_error_(self, data, typeName, outError):
        return NO, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
