import os, sys, platform
from buildtools import os_utils, cmd, log

SOURCEMOD_DIR = os.environ.get('SOURCEMOD18',os.path.join('..','sourcemod','sourcemod','build','package','addons','sourcemod'))
TF2ITEMS_DIR = os.environ.get('TF2ITEMS',os.path.join('..','sourcemod-tf2items'))
PROJECT_DIR=os.path.abspath(os.getcwd())
PLUGINS_DIR=os.path.join(PROJECT_DIR,'plugins')
SPCOMP='spcomp.exe'
if platform.system() == 'Linux':
	SPCOMP='spcomp'

SPCOMP_FLAGS = [
	'-v0', # No banner
	'-i='+os.path.join(TF2ITEMS_DIR,'pawn'), # tf2items rides the short bus in this list.
	'-i='+os.path.join(PROJECT_DIR,'scripting','include'),
]
def spcomp(filename):
	
	os_utils.ensureDirExists(PLUGINS_DIR,noisy=True)
	basename, ext = os.path.splitext(os.path.basename(filename))
	smxname = basename+'.smx'
	smxpath = os.path.join(PLUGINS_DIR,smxname)
	log.info('SPCOMP  '+smxname)
	cmd([os.path.join(SOURCEMOD_DIR,'scripting',SPCOMP)]+SPCOMP_FLAGS+['-o='+smxpath,filename], critical=True, show_output=True, echo=False)

#log.info('SOURCEMOD18='+SOURCEMOD_DIR)	
#log.info('TF2ITEMS_DIR='+TF2ITEMS_DIR)	
#log.info('SPCOMP='+SPCOMP)	
with os_utils.Chdir(os.path.join(PROJECT_DIR,'scripting')):
	spcomp('tf2itemsinfo.sp')