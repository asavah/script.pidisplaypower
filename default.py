import os, sys, subprocess
import xbmc, xbmcaddon, xbmcgui

__addon__    = xbmcaddon.Addon()
__addonid__  = __addon__.getAddonInfo('id')
__cwd__      = __addon__.getAddonInfo('path')
__language__ = __addon__.getLocalizedString
__resource__ = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ).encode('utf-8') )

# Hack: Python2/Python3 fix
if sys.version_info.major < 3:
  __cwd__ = __cwd__.decode('utf-8')
  __resource__ = __resource__.decode('utf-8')

sys.path.append(__resource__)

if __name__ == '__main__':
    import gui
    screensaver_gui = gui.Screensaver('dummy.xml', __cwd__, 'default')
    screensaver_gui.doModal()
    del screensaver_gui
