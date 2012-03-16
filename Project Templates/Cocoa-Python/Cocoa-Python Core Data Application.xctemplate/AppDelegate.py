#
#  ___PROJECTNAMEASIDENTIFIER___AppDelegate.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright ___ORGANIZATIONNAME___ ___YEAR___. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *
from CoreData import *

import os

class ___VARIABLE_classPrefix:identifier___AppDelegate(NSObject):
    window = IBOutlet()
    _managedObjectModel = None
    _persistentStoreCoordinator = None
    _managedObjectContext = None
    
    def applicationDidFinishLaunching_(self, sender):
        self.managedObjectContext()

    def applicationSupportFolder(self):
        paths = NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirectory, NSUserDomainMask, YES)
        basePath = paths[0] if (len(paths) > 0) else NSTemporaryDirectory()
        return os.path.join(basePath, "___PROJECTNAMEASIDENTIFIER___")

    def managedObjectModel(self):
        if self._managedObjectModel: return self._managedObjectModel
            
        self._managedObjectModel = NSManagedObjectModel.mergedModelFromBundles_(None)
        return self._managedObjectModel
    
    def persistentStoreCoordinator(self):
        if self._persistentStoreCoordinator: return self._persistentStoreCoordinator
        
        applicationSupportFolder = self.applicationSupportFolder()
        if not os.path.exists(applicationSupportFolder):
            os.mkdir(applicationSupportFolder)
        
        storePath = os.path.join(applicationSupportFolder, "___PROJECTNAMEASIDENTIFIER___.xml")
        url = NSURL.fileURLWithPath_(storePath)
        self._persistentStoreCoordinator = NSPersistentStoreCoordinator.alloc().initWithManagedObjectModel_(self.managedObjectModel())
        
        success, error = self._persistentStoreCoordinator.addPersistentStoreWithType_configuration_URL_options_error_(NSXMLStoreType, None, url, None, None)
        if not success:
            NSApp().presentError_(error)
        
        return self._persistentStoreCoordinator
        
    def managedObjectContext(self):
        if self._managedObjectContext:  return self._managedObjectContext
        
        coordinator = self.persistentStoreCoordinator()
        if coordinator:
            self._managedObjectContext = NSManagedObjectContext.alloc().init()
            self._managedObjectContext.setPersistentStoreCoordinator_(coordinator)
        
        return self._managedObjectContext
    
    def windowWillReturnUndoManager_(self, window):
        return self.managedObjectContext().undoManager()
        
    @IBAction
    def saveAction_(self, sender):
        success, error = self.managedObjectContext().save_(None)
        if not success:
            NSApp().presentError_(error)

    def applicationShouldTerminate_(self, sender):
        if not self._managedObjectContext:
            return NSTerminateNow
            
        if not self._managedObjectContext.commitEditing():
            NSLog(u'Delegate unable to commit editing to terminate')
            return NSTerminateCancel
        
        if not self._managedObjectContext.hasChanges():
            return NSTerminateNow
            
        success, error = self._managedObjectContext.save_(None)
        
        if success:
            return NSTerminateNow
        
        if NSApp().presentError_(error):
            return NSTerminateCancel
        else:
            question = NSLocalizedString(
                u"Could not save changes while quitting. Quit anyway?",
                u"Quit without saves error question message")
            info = NSLocalizedString(
                u"Quitting now will lose any changes you have made since the last successful save",
                u"Quit without saves error question info")
            quitButton = NSLocalizedString(
                "Quit anyway", "Quit anyway button title")
            cancelButton = NSLocalizedString(
                u"Cancel", u"Cancel button title")
            alert = NSAlert.alloc().init().autorelease()
            alert.setMessageText_(question)
            alert.setInformativeText_(info)
            alert.addButtonWithTitle_(quitButton)
            alert.addButtonWithTitle_(cancelButton)
            
            answer = alert.runModal()
    
            if answer == NSAlertAlternateReturn:
                return NSTerminateCancel

        return NSTerminateNow
