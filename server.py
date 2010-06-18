#!/usr/bin/python

import os
import Pyro.core

class Sh(Pyro.core.ObjBase):
        def __init__(self):
                Pyro.core.ObjBase.__init__(self)
        def info(self, com):
                shell = os.popen(com)
                nguk = shell.read()
                return nguk
        

def main():
    Pyro.core.initServer()
    daemon=Pyro.core.Daemon()
    uri=daemon.connect(Sh(),"sh")

    print "The daemon runs on port:",daemon.port
    print "The object's uri is:",uri

    daemon.requestLoop()
    
if __name__=="__main__":
    main()

