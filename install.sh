#! /bin/bash

if [ -d $HOME/bin ]; then
   cp resultExtract $HOME/bin/
   cp only3d $HOME/bin/
   cp nodExtract $HOME/bin/
   cp unv2ccx $HOME/bin/
   chmod 755 $HOME/bin/resultExtract 
   chmod 755 $HOME/bin/only3d 
   chmod 755 $HOME/bin/nodExtract 
   chmod 755 $HOME/bin/unv2ccx
else
    echo "Sorry! no $HOME/bin"
fi

   
