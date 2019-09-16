# iSecMFT

1 - Instalar VM com mininet

2 - Para facilitar o uso da VM, você pode colocar a rede da VM no modo Bridge fazer SSH da sua máquina:

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

Execução do controlador:

````bash
ryu-manager controller.py
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

Documentos bons de se ler:

https://github.com/mininet/mininet/wiki/FAQ
http://mininet.org/walkthrough