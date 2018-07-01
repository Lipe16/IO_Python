# -*- coding: UTF-8 -*-
#Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato txt.

texto = input("Digite um texto para o arquivo: ")
nome = input("Digite um nome para o arquivo: ")

nome = nome + ".txt"
arquivo = open(nome, "w")
arquivo.write(texto)



