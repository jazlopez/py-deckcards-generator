#!/usr/bin/env bash

# launch libreoffice
# allow localhost connections on port 2002
echo "---------------------------------------------------------"
echo "                      LIBRE OFFICE"
echo "---------------------------------------------------------"
echo "  server will start as background process"
nohup /Applications/LibreOffice.app/Contents/MacOS/soffice \
  --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" > .nohup.server.log 2>&1 &

PID=$(ps -A | grep -m1 'LibreOffice' | awk '{print $1}')

echo "  server is up and running in the background "
echo "    -To stop server process run: "
echo "      $ kill -9 $PID"
