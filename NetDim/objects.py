# NetDim
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

from collections import defaultdict

## Nodes
class Node(object):
    
    class_type = type = "node"
    
    def __init__(
                 self, 
                 name, 
                 x = 100, 
                 y = 100, 
                 longitude = 0, 
                 latitude = 0, 
                 ipaddress = "0.0.0.0",
                 subnetmask = "255.255.255.255"
                 ):
        self.name = name
        self.longitude = int(longitude)
        self.latitude = int(latitude)
        self.ipaddress = ipaddress
        self.subnetmask = subnetmask
        # self id and id of the corresponding label on the canvas
        self.oval = {layer: None for layer in range(3)}
        # image of the node at all three layers: physical, logical and traffic
        self.image = {layer: None for layer in range(3)}
        self.layer_line = {layer: None for layer in range(1, 3)}
        self.lid = None
        self.lpos = None
        self.size = 8
        # position of a node (conversion decimal string to int in case of export)
        self.x = int(float(x))
        self.y = int(float(y))
        # velocity of a node for graph drawing algorithm
        self.vx = 0
        self.vy = 0
        # list of AS to which the node belongs. AS is actually a dictionnary
        # associating an AS to a set of area the node belongs to
        self.AS = defaultdict(set)
        
    def __repr__(self):
        return self.name
        
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __hash__(self):
        return hash(self.name)
        
    def __lt__(self, other):
        return hash(self.name)
        
class Router(Node):
    
    color = "magenta"
    subtype = "router"
    imagex, imagey = 33, 25
    
    def __init__(self, *args):
        self.rt = {}
        super().__init__(*args)
        
class Switch(Node):

    color = "black"
    subtype = "switch"
    imagex, imagey = 54, 36
    
    def __init__(self, *args):
        super().__init__(*args)
        
class OXC(Node):

    color = "pink"
    subtype = "oxc"
    imagex, imagey = 35, 32
    
    def __init__(self, *args):
        super().__init__(*args)
        
class Host(Node):

    color = "blue"
    subtype = "host"
    imagex, imagey = 35, 32
    
    def __init__(self, *args):
        super().__init__(*args)
        
class Regenerator(Node):

    color = "black"
    subtype = "regenerator"
    imagex, imagey = 64, 48
    
    def __init__(self, *args):
        super().__init__(*args)
        
class Splitter(Node):

    color = "black"
    subtype = "splitter"
    imagex, imagey = 64, 50
    
    def __init__(self, *args):
        super().__init__(*args)
        
class Antenna(Node):

    color = "black"
    subtype = "antenna"
    imagex, imagey = 35, 32
    
    def __init__(self, *args):
        super().__init__(*args)
        
class Cloud(Node):

    color = "black"
    subtype = "cloud"
    imagex, imagey = 60, 35
    
    def __init__(self, *args):
        super().__init__(*args)
        
## Links
class Link(object):
    
    class_type = "link"
    
    def __init__(self, name, source, destination, distance=0, bandwidth=0.):
        self.name = name
        self.source = source
        self.destination = destination
        self.distance = int(distance)
        self.bandwidth = float(bandwidth)
        # self id and id of the corresponding label on the canvas
        self.line = None
        self.lid = None
        # self.iid is the id of the interface labels, used to display
        # interfaces specific properties (ip addresses, names, etc) as well
        # as trunk asymmetric (directional) properties (capacity, flow, etc)
        self.ilid = [None]*2
        
    def __repr__(self):
        return self.name
        
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __hash__(self):
        return hash(self.name)

class Trunk(Link):
    
    type = "trunk"
    layer = 0
    dash = ()

    def __init__(
                 self, 
                 interface,
                 name, 
                 source, 
                 destination, 
                 distance = 0., 
                 costSD = 1., 
                 costDS = 1., 
                 capacitySD = 3, 
                 capacityDS = 3, 
                 ipaddressS = None, 
                 subnetmaskS = None,
                 interfaceS = None,
                 ipaddressD = None, 
                 subnetmaskD = None, 
                 interfaceD = None
                 ):
                     
        super().__init__(name, source, destination, distance)
        self.interface = interface
        self.costSD, self.costDS = int(costSD), int(costDS)
        self.capacitySD, self.capacityDS = int(capacitySD), int(capacityDS)
        self.ipaddressS = ipaddressS
        self.subnetmaskS = subnetmaskS
        self.interfaceS = interfaceS
        self.ipaddressD = ipaddressD
        self.subnetmaskD = subnetmaskD
        self.interfaceD = interfaceD
        
        self.trafficSD = self.trafficDS = 0.
        self.wctrafficSD = self.wctrafficDS = 0.
        self.wcfailure = None
        self.flowSD = self.flowDS = 0.
        # list of AS to which the trunks belongs. AS is actually a dictionnary
        # associating an AS to a set of area the trunks belongs to
        self.AS = defaultdict(set)
        
    def __lt__(self, other):
        return hash(self.name)
        
    def __call__(self, property, node):
        dir = (node == self.source)*"SD" or "DS"
        if property in ("subnetmask", "interface", "ipaddress"):
            dir = dir[:-1]
        return getattr(self, property + dir)
        
class Ethernet(Trunk):
    
    color = "blue"
    protocol = subtype = "ethernet"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sntw = None
        
class WDMFiber(Trunk):
    
    color = "orange"
    protocol = subtype = "wdm"
    
    def __init__(self, *args):
        args = list(args)
        if len(args) > 4:
            self.lambda_capacity = args.pop()
        else:
            self.lambda_capacity = 88
        super().__init__(*args)
        
class Route(Link):
    type = "route"
    subtype = type
    dash = (3,5)
    color = "green"
    layer = 1
    
    def __init__(
                 self, 
                 name, 
                 source, 
                 destination, 
                 distance = 0, 
                 path_constraints = [], 
                 excluded_trunks = set(), 
                 excluded_nodes = set(), 
                 path = [], 
                 subnets = set(), 
                 cost = 1.,
                 traffic = 0,
                 AS = None
                 ):
                     
        super().__init__(name, source, destination, distance)
        self.path_constraints = path_constraints
        self.excluded_nodes = excluded_nodes
        self.excluded_trunks = excluded_trunks
        self.path = path
        self.subnets = subnets
        self.cost = cost
        self.traffic = traffic
        self.AS = AS
        # r_path ("recovery path") contains, for each link of the route's path 
        # the associated recovery path, i.e the path of the route if the link 
        # in failure did not exist.
        self.r_path = dict()
        
class Traffic(Link):
    type = "traffic"
    subtype = type
    dash = (7,1,1,1)
    color = "purple"
    layer = 2
    
    def __init__(
                 self, 
                 name, 
                 source, 
                 destination, 
                 subnet = 0, 
                 throughput = 15, 
                 path = []
                 ):
        super().__init__(name, source, destination)
        # throughput in Mbps
        self.throughput = throughput
        self.subnet = subnet
        self.path = path
