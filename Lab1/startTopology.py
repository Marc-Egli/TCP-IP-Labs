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
HOSTS = 35
"Function definition: This is called from the main function"
def firstNetwork():

    "Create an empty network and add nodes to it."
    net = Mininet()
    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    hosts = []
    hosts.append(net.addHost( 'RO1'))
    switches = []
    for i in range(0,HOSTS) :
        hosts.append(net.addHost( 'PC'+str(i), ip='10.10.'+str(i)+'.1/24'))
        switches.append(net.addSwitch( 's'+str(i)+'R' ))
        net.addLink(hosts[-1],switches[-1])
        net.addLink(hosts[0],switches[-1])

    

    
    hosts[0].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    info( '*** Starting network\n')
    net.start()
    for i in range(0,HOSTS):
        hosts[0].cmd('ip addr add 10.10.'+ str(i)+ '.4/24 dev RO1-eth'+str(i))
        hosts[i+1].cmd('ip route add default via 10.10.'+ str(i)+ '.4')
    
    hosts[0].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    hosts[0].cmd('ip addr del 10.0.0.1/8 dev RO1-eth0')

   
    info( '*** Running the command line interface\n' )
    delay = net.pingAllFull()
    avg_times=[]
    for d in delay:
        avg_times.append(d[2][3])
    print("Average delay : "+ str(mean(avg_times)))
    print(net.pingAll())
    CLI( net )

    info( '*** Closing the terminals on the hosts\n' )
    
    for host in hosts :
        host.cmd("killall xterm")
   


    info( '*** Stopping network' )
    net.stop()

"main Function: This is called when the Python file is run"
if __name__ == '__main__':
    setLogLevel( 'info' )
    firstNetwork()
