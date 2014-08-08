from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSEvent (TestCase):
    def testConstants(self):
        self.assertEqual(NSLeftMouseDown, 1)
        self.assertEqual(NSLeftMouseUp, 2)
        self.assertEqual(NSRightMouseDown, 3)
        self.assertEqual(NSRightMouseUp, 4)
        self.assertEqual(NSMouseMoved, 5)
        self.assertEqual(NSLeftMouseDragged, 6)
        self.assertEqual(NSRightMouseDragged, 7)
        self.assertEqual(NSMouseEntered, 8)
        self.assertEqual(NSMouseExited, 9)
        self.assertEqual(NSKeyDown, 10)
        self.assertEqual(NSKeyUp, 11)
        self.assertEqual(NSFlagsChanged, 12)
        self.assertEqual(NSAppKitDefined, 13)
        self.assertEqual(NSSystemDefined, 14)
        self.assertEqual(NSApplicationDefined, 15)
        self.assertEqual(NSPeriodic, 16)
        self.assertEqual(NSCursorUpdate, 17)
        self.assertEqual(NSScrollWheel, 22)
        self.assertEqual(NSTabletPoint, 23)
        self.assertEqual(NSTabletProximity, 24)
        self.assertEqual(NSOtherMouseDown, 25)
        self.assertEqual(NSOtherMouseUp, 26)
        self.assertEqual(NSOtherMouseDragged, 27)
        self.assertEqual(NSLeftMouseDownMask, 1 << NSLeftMouseDown)
        self.assertEqual(NSLeftMouseUpMask, 1 << NSLeftMouseUp)
        self.assertEqual(NSRightMouseDownMask, 1 << NSRightMouseDown)
        self.assertEqual(NSRightMouseUpMask, 1 << NSRightMouseUp)
        self.assertEqual(NSMouseMovedMask, 1 << NSMouseMoved)
        self.assertEqual(NSLeftMouseDraggedMask, 1 << NSLeftMouseDragged)
        self.assertEqual(NSRightMouseDraggedMask, 1 << NSRightMouseDragged)
        self.assertEqual(NSMouseEnteredMask, 1 << NSMouseEntered)
        self.assertEqual(NSMouseExitedMask, 1 << NSMouseExited)
        self.assertEqual(NSKeyDownMask, 1 << NSKeyDown)
        self.assertEqual(NSKeyUpMask, 1 << NSKeyUp)
        self.assertEqual(NSFlagsChangedMask, 1 << NSFlagsChanged)
        self.assertEqual(NSAppKitDefinedMask, 1 << NSAppKitDefined)
        self.assertEqual(NSSystemDefinedMask, 1 << NSSystemDefined)
        self.assertEqual(NSApplicationDefinedMask, 1 << NSApplicationDefined)
        self.assertEqual(NSPeriodicMask, 1 << NSPeriodic)
        self.assertEqual(NSCursorUpdateMask, 1 << NSCursorUpdate)
        self.assertEqual(NSScrollWheelMask, 1 << NSScrollWheel)
        self.assertEqual(NSTabletPointMask, 1 << NSTabletPoint)
        self.assertEqual(NSTabletProximityMask, 1 << NSTabletProximity)
        self.assertEqual(NSOtherMouseDownMask, 1 << NSOtherMouseDown)
        self.assertEqual(NSOtherMouseUpMask, 1 << NSOtherMouseUp)
        self.assertEqual(NSOtherMouseDraggedMask, 1 << NSOtherMouseDragged)
        self.assertEqual(NSAnyEventMask, -1)

        self.assertEqual(NSAlphaShiftKeyMask, 1 << 16)
        self.assertEqual(NSShiftKeyMask, 1 << 17)
        self.assertEqual(NSControlKeyMask, 1 << 18)
        self.assertEqual(NSAlternateKeyMask, 1 << 19)
        self.assertEqual(NSCommandKeyMask, 1 << 20)
        self.assertEqual(NSNumericPadKeyMask, 1 << 21)
        self.assertEqual(NSHelpKeyMask, 1 << 22)
        self.assertEqual(NSFunctionKeyMask, 1 << 23)
        self.assertEqual(NSDeviceIndependentModifierFlagsMask, -65536)
        self.assertEqual(NSUnknownPointingDevice, 0)
        self.assertEqual(NSPenPointingDevice, 1)
        self.assertEqual(NSCursorPointingDevice, 2)
        self.assertEqual(NSEraserPointingDevice, 3)
        self.assertEqual(NSPenTipMask, 1)
        self.assertEqual(NSPenLowerSideMask, 2)
        self.assertEqual(NSPenUpperSideMask, 4)

        self.assertEqual(NSWindowExposedEventType, 0)
        self.assertEqual(NSApplicationActivatedEventType, 1)
        self.assertEqual(NSApplicationDeactivatedEventType, 2)
        self.assertEqual(NSWindowMovedEventType, 4)
        self.assertEqual(NSScreenChangedEventType, 8)
        self.assertEqual(NSAWTEventType, 16)
        self.assertEqual(NSPowerOffEventType, 1)
        self.assertEqual(NSMouseEventSubtype, 0)
        self.assertEqual(NSTabletPointEventSubtype, 1)
        self.assertEqual(NSTabletProximityEventSubtype, 2)

        self.assertEqual(NSUpArrowFunctionKey, unichr(0xF700))
        self.assertEqual(NSDownArrowFunctionKey, unichr(0xF701))
        self.assertEqual(NSLeftArrowFunctionKey, unichr(0xF702))
        self.assertEqual(NSRightArrowFunctionKey, unichr(0xF703))
        self.assertEqual(NSF1FunctionKey, unichr(0xF704))
        self.assertEqual(NSF2FunctionKey, unichr(0xF705))
        self.assertEqual(NSF3FunctionKey, unichr(0xF706))
        self.assertEqual(NSF4FunctionKey, unichr(0xF707))
        self.assertEqual(NSF5FunctionKey, unichr(0xF708))
        self.assertEqual(NSF6FunctionKey, unichr(0xF709))
        self.assertEqual(NSF7FunctionKey, unichr(0xF70A))
        self.assertEqual(NSF8FunctionKey, unichr(0xF70B))
        self.assertEqual(NSF9FunctionKey, unichr(0xF70C))
        self.assertEqual(NSF10FunctionKey, unichr(0xF70D))
        self.assertEqual(NSF11FunctionKey, unichr(0xF70E))
        self.assertEqual(NSF12FunctionKey, unichr(0xF70F))
        self.assertEqual(NSF13FunctionKey, unichr(0xF710))
        self.assertEqual(NSF14FunctionKey, unichr(0xF711))
        self.assertEqual(NSF15FunctionKey, unichr(0xF712))
        self.assertEqual(NSF16FunctionKey, unichr(0xF713))
        self.assertEqual(NSF17FunctionKey, unichr(0xF714))
        self.assertEqual(NSF18FunctionKey, unichr(0xF715))
        self.assertEqual(NSF19FunctionKey, unichr(0xF716))
        self.assertEqual(NSF20FunctionKey, unichr(0xF717))
        self.assertEqual(NSF21FunctionKey, unichr(0xF718))
        self.assertEqual(NSF22FunctionKey, unichr(0xF719))
        self.assertEqual(NSF23FunctionKey, unichr(0xF71A))
        self.assertEqual(NSF24FunctionKey, unichr(0xF71B))
        self.assertEqual(NSF25FunctionKey, unichr(0xF71C))
        self.assertEqual(NSF26FunctionKey, unichr(0xF71D))
        self.assertEqual(NSF27FunctionKey, unichr(0xF71E))
        self.assertEqual(NSF28FunctionKey, unichr(0xF71F))
        self.assertEqual(NSF29FunctionKey, unichr(0xF720))
        self.assertEqual(NSF30FunctionKey, unichr(0xF721))
        self.assertEqual(NSF31FunctionKey, unichr(0xF722))
        self.assertEqual(NSF32FunctionKey, unichr(0xF723))
        self.assertEqual(NSF33FunctionKey, unichr(0xF724))
        self.assertEqual(NSF34FunctionKey, unichr(0xF725))
        self.assertEqual(NSF35FunctionKey, unichr(0xF726))
        self.assertEqual(NSInsertFunctionKey, unichr(0xF727))
        self.assertEqual(NSDeleteFunctionKey, unichr(0xF728))
        self.assertEqual(NSHomeFunctionKey, unichr(0xF729))
        self.assertEqual(NSBeginFunctionKey, unichr(0xF72A))
        self.assertEqual(NSEndFunctionKey, unichr(0xF72B))
        self.assertEqual(NSPageUpFunctionKey, unichr(0xF72C))
        self.assertEqual(NSPageDownFunctionKey, unichr(0xF72D))
        self.assertEqual(NSPrintScreenFunctionKey, unichr(0xF72E))
        self.assertEqual(NSScrollLockFunctionKey, unichr(0xF72F))
        self.assertEqual(NSPauseFunctionKey, unichr(0xF730))
        self.assertEqual(NSSysReqFunctionKey, unichr(0xF731))
        self.assertEqual(NSBreakFunctionKey, unichr(0xF732))
        self.assertEqual(NSResetFunctionKey, unichr(0xF733))
        self.assertEqual(NSStopFunctionKey, unichr(0xF734))
        self.assertEqual(NSMenuFunctionKey, unichr(0xF735))
        self.assertEqual(NSUserFunctionKey, unichr(0xF736))
        self.assertEqual(NSSystemFunctionKey, unichr(0xF737))
        self.assertEqual(NSPrintFunctionKey, unichr(0xF738))
        self.assertEqual(NSClearLineFunctionKey, unichr(0xF739))
        self.assertEqual(NSClearDisplayFunctionKey, unichr(0xF73A))
        self.assertEqual(NSInsertLineFunctionKey, unichr(0xF73B))
        self.assertEqual(NSDeleteLineFunctionKey, unichr(0xF73C))
        self.assertEqual(NSInsertCharFunctionKey, unichr(0xF73D))
        self.assertEqual(NSDeleteCharFunctionKey, unichr(0xF73E))
        self.assertEqual(NSPrevFunctionKey, unichr(0xF73F))
        self.assertEqual(NSNextFunctionKey, unichr(0xF740))
        self.assertEqual(NSSelectFunctionKey, unichr(0xF741))
        self.assertEqual(NSExecuteFunctionKey, unichr(0xF742))
        self.assertEqual(NSUndoFunctionKey, unichr(0xF743))
        self.assertEqual(NSRedoFunctionKey, unichr(0xF744))
        self.assertEqual(NSFindFunctionKey, unichr(0xF745))
        self.assertEqual(NSHelpFunctionKey, unichr(0xF746))
        self.assertEqual(NSModeSwitchFunctionKey, unichr(0xF747))

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(NSEventTypeGesture, 29)
        self.assertEqual(NSEventTypeMagnify, 30)
        self.assertEqual(NSEventTypeSwipe, 31)
        self.assertEqual(NSEventTypeRotate, 18)
        self.assertEqual(NSEventTypeBeginGesture, 19)
        self.assertEqual(NSEventTypeEndGesture, 20)

        self.assertEqual(NSEventMaskGesture, 1 << 29)
        self.assertEqual(NSEventMaskMagnify, 1 << 30)
        self.assertEqual(NSEventMaskSwipe, 1 << 31)
        self.assertEqual(NSEventMaskRotate, 1 << 18)
        self.assertEqual(NSEventMaskBeginGesture, 1 << 19)
        self.assertEqual(NSEventMaskEndGesture, 1 << 20)



    def testFunctions(self):
        v = NSEventMaskFromType(NSLeftMouseDown)
        self.assertEqual(v, NSLeftMouseDownMask)

        v = NSEventMaskFromType(NSOtherMouseDown)
        self.assertEqual(v, NSOtherMouseDownMask)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSEvent.isMouseCoalescingEnabled)
        self.assertArgIsBOOL(NSEvent.setMouseCoalescingEnabled_, 0)

    def testMethods(self):
        self.assertResultIsBOOL(NSEvent.isARepeat)
        self.assertResultIsBOOL(NSEvent.isEnteringProximity)

        self.assertArgIsBOOL(NSEvent.keyEventWithType_location_modifierFlags_timestamp_windowNumber_context_characters_charactersIgnoringModifiers_isARepeat_keyCode_, 8)
        self.assertArgHasType(NSEvent.enterExitEventWithType_location_modifierFlags_timestamp_windowNumber_context_eventNumber_trackingNumber_userData_, 8, b'^v')


        self.assertResultHasType(NSEvent.userData, b'^v')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSEvent.addGlobalMonitorForEventsMatchingMask_handler_, 1, b'v@')
        self.assertArgIsBlock(NSEvent.addLocalMonitorForEventsMatchingMask_handler_, 1, b'v@')

if __name__ == "__main__":
    main()