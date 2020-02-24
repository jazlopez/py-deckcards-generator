import uno
import os

# setup
HOST = 'localhost'
PORT = 2002
TEMPLATE_DIRECTORY = 'templates'
TEMPLATE_NAME = 'card.deck.template.otp'

# connect to soffice shell
# see soffice.server.sh in this repository

localcontext = uno.getComponentContext()
resolver = localcontext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localcontext)
uri = 'uno:socket,host={0},port={1};urp;StarOffice.ComponentContext'.format(HOST, PORT)
ctx = resolver.resolve(uri)
smgr = ctx.ServiceManager

# get the central desktop object
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
model = desktop.getCurrentComponent()

# open presentation
path = uno.systemPathToFileUrl(os.path.join(os.getcwd(), TEMPLATE_DIRECTORY, TEMPLATE_NAME))
doc = desktop.loadComponentFromURL(path, 'default', 0, ())

__version__ = '0.0.0'
__author__ = 'jaziel lopez github.com/jazlopez'
