#!/usr/bin/env python
#Author: Vitor Oliveira Souza
#Direito Autorais é free


##
# MAPA MENTAL DE DESENVOLVIMENTO
##
# OBJETIVO: Setup a full wifi cracking with all options
#Network Indentifier - list all host discovery from tcpdump analyses
# Verificar pré requesitos
# Definir interfaces e configurações iniciais 
# Ataques: 
# Cracking wep handshake 
# Deauth Attack


# Previsão de entrega 23 de outubro 

#BIBLIOTECAS
import argparse
import os
import sys
from socket import *

#CONFIGURACAO DE REDE
socks = socket(AF_INET, SOCK_DGRAM)
socks.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#argumentos iniciais
parser = argparse.ArgumentParser()
parser.add_argument("mode", help="TYPE [1] TO ACTIVE | [2] TO PASSIVE")
parser.add_argument("", help"")
#Inicio
