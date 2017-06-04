from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import DefaultController, RemoteController
net = Mininet()
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')
s6 = net.addSwitch('s6')
s7 = net.addSwitch('s7')
s8 = net.addSwitch('s8')
s9 = net.addSwitch('s9')
s10 = net.addSwitch('s10')
s11 = net.addSwitch('s11')
s12 = net.addSwitch('s12')
s13 = net.addSwitch('s13')
s14 = net.addSwitch('s14')
s15 = net.addSwitch('s15')
s16 = net.addSwitch('s16')
h1 = net.addHost('h1')
h2 = net.addHost('h2')
sdn_controller19 = net.addController(
name = 'sdn_controller19',
controller = RemoteController,
ip = '0.0.0.0',
port = 6633)
net.addLink(s1,s2)
net.addLink(s3,s4)
net.addLink(s1,s3)
net.addLink(s2,s4)
net.addLink(s5,s6)
net.addLink(s7,s8)
net.addLink(s5,s7)
net.addLink(s6,s8)
net.addLink(s1,s5)
net.addLink(s2,s6)
net.addLink(s3,s7)
net.addLink(s4,s8)
net.addLink(s9,s10)
net.addLink(s11,s12)
net.addLink(s9,s11)
net.addLink(s10,s12)
net.addLink(s13,s14)
net.addLink(s15,s16)
net.addLink(s13,s15)
net.addLink(s14,s16)
net.addLink(s9,s13)
net.addLink(s10,s14)
net.addLink(s11,s15)
net.addLink(s12,s16)
net.addLink(s1,s9)
net.addLink(s2,s10)
net.addLink(s3,s11)
net.addLink(s4,s12)
net.addLink(s5,s13)
net.addLink(s6,s14)
net.addLink(s7,s15)
net.addLink(s8,s16)
net.addLink(h1,s4)
net.addLink(h2,s9)
net.start()
CLI(net)
