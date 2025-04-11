from thefuzz import fuzz, process


def audio(caminhoArquivo):
    with open(caminhoArquivo, 'rb') as arquivo:
        dadosBinarios = arquivo.read()
        representarBits = ''.join(f'{byte:08b}' for byte in dadosBinarios)

    return representarBits

caminho1 = audio('C:/Users/jose roberto/Downloads/acho que beberei meu uísque puro.mp3')
caminho2 = audio('C:/Users/jose roberto/Downloads/November Rain.mp3')




print(fuzz.partial_ratio(caminho1[:1000], caminho2[:1000]))
print(fuzz.ratio(caminho1[:1000], caminho2[:1000]))
print(fuzz.token_sort_ratio(caminho1[:1000], caminho2[:1000]))

