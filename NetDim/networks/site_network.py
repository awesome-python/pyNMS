# NetDim (contact@netdim.fr)

from .base_network import BaseNetwork
from views.insite_view import InSiteView
from objects.objects import *

def overrider(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

class SiteNetwork(BaseNetwork):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # 'nf' is the node factory. Creates or retrieves any type of nodes
    @overrider(BaseNetwork)
    def nf(self, node_type='router', id=None, **kwargs):
        if not id:
            if 'name' not in kwargs:
                name = node_type + str(len(list(self.ftr('node', node_type))))
                kwargs['name'] = name
            else:
                if kwargs['name'] in self.name_to_id:
                    return self.nodes[self.name_to_id[kwargs['name']]]
            id = self.cpt_node
            kwargs['id'] = id
            self.nodes[id] = node_class[node_type](**kwargs)
            self.nodes[id].view = InSiteView(
                                             self.nodes[id], 
                                             kwargs['name'],
                                             self.view.controller,
                                             )
            self.name_to_id[kwargs['name']] = id
            self.cpt_node += 1
        return self.nodes[id]