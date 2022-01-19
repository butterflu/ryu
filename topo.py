#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import subprocess

def projectNet():

    net = Mininet()
    
    controller = net.addController(name='c0' ,
                         controller=RemoteController ,
                         ip='127.0.0.1',
                         port=6633)

    info('...Dodawanie urzadzen...\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')
    h5 = net.addHost('h5', ip='10.0.0.5')
    sw = net.addSwitch('sw1')

    info('...Dodawanie polaczen...\n')
    net.addLink(h1, sw)
    net.addLink(h2, sw)
    net.addLink(h3, sw)
    net.addLink(h4, sw)
    net.addLink(h5, sw)



    info('...Uruchamianie sieci...\n')
    net.start()

    info('...Konfiguracja switcha...\n')
    interfaces = ['sw1-eth1', 'sw1-eth2', 'sw1-eth3', 'sw1-eth4', 'sw1-eth5']

    info('...Uruchamianie CLI...\n')
    info('  #open a terminal for s1 and type the following commands\n  #ovs-vsctl del-port s1-eth3 \novs-vsctl add-port s1 s1-eth3 -- --id=@p get port s1-eth3 -- --id=@m create mirror name=m0 select-all=true output-port=@p -- set bridge s1 mirrors=@m\n')

    CLI( net )

    info('...Zatrzymywanie sieci...\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    projectNet()

