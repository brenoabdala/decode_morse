'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro.
'''

from dotenv import load_dotenv
import json
import os
import sys
import datetime

def decode_morse(msg, dictionary):

    retorno = '' #Variavel de saida

    morse_words = msg.split('  ') #Quebra a mensagem original em N palavras

    for word in morse_words: #Para cada palavra na mensagem
        morse_letters = word.split(' ') #Quebra a palavra em N letras
        for letter in morse_letters: #Para cada letra na palavra
            retorno += dictionary[letter] #Traduz a letra de morse com base no dict
        retorno += ' ' #Separa as palavras da saida por espaco

    return retorno.strip()


def save_clear_msg_csv_hdr(filename, output):
    header = 'mensagem;datetime\n' #Cabecalho de saida

    if(os.path.exists(filename)): #Verifica se arquivo de saida ja existe
        with open(filename, 'a') as arq:
            row = output + ';' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '\n'
            arq.write(row) #Se sim, adiciona uma linha
    else:
        with open(filename, 'a') as arq:
            row = output + ';' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '\n'
            arq.write(header + row)  #Se nao, adiciona cabecalho + uma linha

if __name__ == "__main__":

    #Importa as variaveis de ambiente do .env
    load_dotenv() 

    #Converte o de-para do .env para uma variavel dict
    morse_dictionary = json.loads(os.getenv('dict_morse')) 

    #Le o texto de entrada em morse
    input_text = sys.argv[1] 

    #Saida traduzida
    output_text = decode_morse(input_text, morse_dictionary) 

    #Obtem o nome do arquivo de saida do .env
    filename = os.getenv('file_path') 

    #Escreve em arquivo csv
    save_clear_msg_csv_hdr(filename, output_text) 