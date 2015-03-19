import os, sys, subprocess
import xbmc, xbmcgui, xbmcaddon

__addon__    = sys.modules[ '__main__' ].__addon__
__addonid__  = sys.modules[ '__main__' ].__addonid__
__cwd__      = sys.modules[ '__main__' ].__cwd__
__skindir__  = xbmc.getSkinDir().decode('utf-8')
__skinhome__ = xbmc.translatePath( os.path.join( 'special://home/addons/', __skindir__, 'addon.xml' ).encode('utf-8') ).decode('utf-8')
__skinxbmc__ = xbmc.translatePath( os.path.join( 'special://xbmc/addons/', __skindir__, 'addon.xml' ).encode('utf-8') ).decode('utf-8')

class Screensaver(xbmcgui.WindowXMLDialog):
    def __init__( self, *args, **kwargs ):
        pass

    def onInit(self):
        self._is_powered = True
        self.Monitor = MyMonitor(action = self._power_on)
        self._power_toggle()

    def _power_on(self):
        self._power_toggle()
        self.close()

    def _power_toggle(self):
        if self._is_powered:
            arg2 = '0'
        else:
            arg2 = '1'
        try:
            cmd = subprocess.Popen(['vcgencmd', 'display_power', arg2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = cmd.communicate()
            xbmc.log(msg="%s: vcgencmd returned %s" % ( __addonid__, repr(out) ), level=xbmc.LOGDEBUG)
            if not err:
                self._is_powered = not self._is_powered
            else:
                xbmc.log(msg="%s: vcgencmd returned %s" % ( __addonid__, repr(err) ), level=xbmc.LOGERROR)
        except:
            xbmc.log(msg="%s: Exception running vcgencmd" % ( __addonid__ ), level=xbmc.LOGERROR)


class MyMonitor(xbmc.Monitor):
    def __init__( self, *args, **kwargs ):
        self.action = kwargs['action']

    def onScreensaverDeactivated(self):
        self.action()