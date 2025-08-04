"""DESAFIO 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""
def linha(palavra):
    n = len(palavra) + 4
    print(n *'=' )
    print(f'  {palavra}')
    print(n *'=')
linha('Rafaela Bassi')
linha('Curso de Python no curso em vídeo')
linha('Teste')