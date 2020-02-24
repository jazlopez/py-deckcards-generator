#!/usr/bin/env bash

# launch libreoffice
# allow localhost connections on port 2002
/Applications/LibreOffice.app/Contents/MacOS/soffice \
  --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager"