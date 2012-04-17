#-*- coding: utf-8 -*-
#
#  main.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright ___ORGANIZATIONNAME___ ___YEAR___. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import ___VARIABLE_classPrefix:identifier___AppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
