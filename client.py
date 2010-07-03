#!/usr/bin/python

########################
# Modify By Freez Meinster
#
import Pyro.core
nguk = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/sh")
print "Input your command:"
com = raw_input()
print nguk.info(com)

