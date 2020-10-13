#!/usr/bin/python

"""
This example shows how to create a Mininet object and add nodes to it manually.
"""
"Importing Libraries"
from statistics import mean
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topolib import TreeTopo
import math 
HOSTS = 100
"Function definition: This is called from the main function"
def firstNetwork():

    tree = TreeTopo( depth=2 , fanout= math.floor(math.sqrt(HOSTS)))
    net = Mininet(topo=tree)
    net.start()

    info( '*** Running the command line interface\n' )
    delay = net.pingAllFull()
    avg_times=[]
    for d in delay:
        avg_times.append(d[2][3])
    print("Average delay : "+ str(mean(avg_times)))
    print(net.pingAll())
    CLI( net )

    info( '*** Closing the terminals on the hosts\n' )


    info( '*** Stopping network' )
    net.stop()

"main Function: This is called when the Python file is run"
if __name__ == '__main__':
    firstNetwork()
