# Automação de Cadastro (Python PowerUp)

# pip install pyautogui

import pyautogui
import time


# pyautogui.write -> escrever
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho (hotkey)
pyautogui.PAUSE = 3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# PASSO A PASSO DO SEU PROGRAMA
# Passo 1: Entrar no sistema da empresa
# Abriria o navegador
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

# Entrar no link
pyautogui.write(link)
pyautogui.press('enter')

# Fazer uma pausa maior
time.sleep(6)

# Passopythonimpressiona 2: Fazer login 
# Clicar no campo de emador@gmail.comil
pyautogui.click(x=625, y=507)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab') # Passar para o próximo campo
pyautogui.write("sua senha")
pyautogui.press('tab') # Passar para o botão
pyautogui.click(x=952, y=703)
# fazer uma pausa maior para o site carregar
time.sleep(6)

# Passo 3: Abrir a base de dados  
import pandas

tabela = pandas.read_csv("produtos.csv")    
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=1021, y=362) # clicar no campo do código
    
    # Código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab') # passar para o próximo campo
    
    #Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab') # passar para o próximo campo

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab') # passar para o próximo campo

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab') # passar para o próximo campo

    # Preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab') # passar para o próximo campo

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab') # passar para o próximo campo
    # OBS
    obs = str(tabela.loc[linha, "obs"])  
    if obs != "nan":       
        pyautogui.write(obs)
    pyautogui.press('tab') # passar para o botão enviar

    pyautogui.press('enter') # clicar no enviar

    # Voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
