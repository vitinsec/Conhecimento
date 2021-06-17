#!/usr/bin/bash
clear
echo "==================================="
echo "Iniciando as regras de firewall..."
echo "==================================="
echo "Escolha o perfil de gerênciamento."
echo "[ 1 ] - Docker Conf."
echo "[ 2 ] - CTF Like a PRO"
echo "[ 3 ] - Internet Connect"
echo "==================================="
echo "[OP.] => "
read "opera" # Desenvolvimento por etapas
'''
Mind-Set: 
Docker = mac Portas abertas e gerênciamento de requesições aos servidores docker
CTF = mac Portas devem estar fechadas e abertas somente em caso de coneção explicita.
Internet Connect = Change the mac addres and just open web ports 443, no necessary 80.
THink a way to deploy this script at starting. 
'''

#Firewall Rules Creating And Enable to start with PC
