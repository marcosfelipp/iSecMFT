# iSecMFT

1 - Instalar VM do mininet wifi

2 - Para facilitar o uso da VM, você pode colocar a rede da VM no modo Bridge fazer SSH da sua máquina para VM:

Para isso vá ao VirtualBox, clique em "configurações da VM", depois em "Rede". Troque o modo NAT para Bidge.

Inicie a VM e confira o ip atribuído a ela.

Abra o Pronpt e Faça SSH usando o comando:

````bash
ssh -X -v <VM's IP address>
````

3 - Faça o download desse repositório:

````bash
git clone https://github.com/marcosfelipp/iSecMFT.git
````

4 - Instale as dependências:

````bash
cd iSecMFT/mininet_wifi
chmod +x install.sh
./install.sh
````

5 - Execução:

Você pode criar sua própria topologia usando o mininedit:

````bash
python /home/wifi/mininet-wifi/examples/miniedit.py
````
Para salvar clique em File - > Export Level 2 script.

6 - Executar a topologia:

Abra dois terminais.

Em um terminal, rode o controlador:

Execução do controlador que tem multiplas tabelas:

````bash
ryu-manager controller_multiple_tables_mn_wifi.py
````

Execução do controlador que tem unica tabela:

````bash
ryu-manager controller_single_table_mn_wifi.py
````
No outro terminal, rode a topologia que você salvou (obs: você deve estar na pasta onde salvou a topologia):

````bash
sudo python nome_da_topo.py
````
Rode o seguinte comando para conectar o switch ao controlador:

````bash
sh ovs-vsctl set-controller s1 tcp:127.0.0.1:6633
````

7 - Adicionar regras nos switches:

Você pode preencher a tabela de Firewire ou as outras tabelas com o comando "ovs-vsctl add-flow".

Por exemplo, se você quiser adcionar uma regra de bloqueio para o host 2:

````bash
sh ovs-ofctl -O Openflow13 add-flow s1 table=2,ip,nw_src=10.0.0.2,actions=drop
````

8 - Ver regras no switch:

Todas as regras:
```bash
sh ovs-ofctl dump-flows s1 -O OpenFlow13
```
Regras de determinada tabela:
```bash
sh ovs-ofctl dump-flows s1 table=10 -O OpenFlow13
```
## Executar mobility.py
Execute esses dois comandos adicionais. O primeiro comando serve para dar um 'clear' no mininet, apagando as configurações que podem ter ficado em execuções anteriores. O segundo comando ele pausa a rede da VM. Vi que as vezes pode interferir na cominicação dos hosts.

```bash
sudo mn -c
sudo systemctl stop network-manager
```

Agora pode executar:

```bash
sudo python mobility.py
```
Volte para o passo 6 do tutorial (subir o controlador e rodar comando para o switch conectar nele).

Faça o teste para ver se está tudo funcionando:

```bash
h1 ping sta1
```

Tente adicionar um regra de bloqueio e vê se está funcionando:


```bash
sh ovs-ofctl -O Openflow13 add-flow ap1 table=2,ip,nw_src=10.0.0.2,actions=drop

h1 ping sta2
```

O ping deve ser bloqueado pela regra.
