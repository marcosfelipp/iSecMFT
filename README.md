# iSecMFT

1 - Instalar VM com mininet

2 - Para facilitar o uso da VM, você pode colocar a rede da VM no modo Bridge fazer SSH da sua máquina para VM:

Para isso vá ao VirtualBox, clique em "configurações da VM", depois em "Rede". Troque o modo NAT para Bidge.

Inicie a VM e confira o ip atribuído a ela.

Abra o Pronpt e Faça SSH usando o comando:

````bash
ssh -X -v <VM's IP address>
````

3 - Baixe o arquivo de topologia para a VM:

````bash
wget https://raw.githubusercontent.com/marcosfelipp/iSecMFT/master/topo_mn_multiple_sw.py
````

Por padrão coloquei o número de hosts como 16. Você pode mudar para o tanto que desejar, mudando a variável N_HOSTS.

4 - Suba o controlador na VM ou no seu computador(remoto).

Instalação do Ryu:
````
sudo apt-get install python3-pip -y

sudo pip3 install ryu
````

Execução do controlador que tem multiplas tabelas:

````bash
ryu-manager controller_multiple_tables.py
````

Execução do controlador que tem unica tabela:

````bash
ryu-manager controller_single_table.py
````

5 - Configurei as tabelas da seguinte forma: 

TABELA 2: Firewire
TABELA 3: Espelhamento
TABELA 4: Encaminhamento

Você pode alterar como quiser, mudando as variáveis.

6 - Rodar mininet:

````bash
sudo mn --custom topo_mn_multiple_sw.py -v output --switch ovs,protocols=OpenFlow13 --controller=remote,ip=10.0.0.101,port=6633
````

Obs: mude o IP para o IP de onde está rodando o controlador.

7 - Adicionar regras nos switches:

Você pode preencher a tabela de Firewire ou as outras tabelas com o comando "ovs-vsctl add-flow".

Por exemplo, se você quiser adcionar uma regra de bloqueio em determinado host:

````bash
sh ovs-vsctl add-flow s1 table=2 ip,nw_src=10.0.0.2,actions=drop
````

Documentos bons de se ler:

Tutorial de como usar o iperf no mininet:

http://csie.nqu.edu.tw/smallko/sdn/iperf_mininet.htm

Se tiver dúvidas no uso do mininet:

https://github.com/mininet/mininet/wiki/FAQ

http://mininet.org/walkthrough

Dúvidas quanto ao switch, criação de regras...

http://docs.openvswitch.org/en/latest/tutorials/ovs-advanced/