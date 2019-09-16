from mininet.topo import Topo

N_HOSTS = 16


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        switch = self.addSwitch('s1')

        for i in range(N_HOSTS):
            host = self.addHost('h' + str(i))
            self.addLink(host, switch)


topos = {'mytopo': (lambda: MyTopo())}