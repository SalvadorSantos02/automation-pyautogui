import pyautogui
import time
#pyautogui.click - clicar em algum lugar
#pyautogui.press - apertar 1 tecla
#pyautogui.write - escrever um texto
#pyautogui.kotkey - apertar duas teclas ao mesmo tempo

pyautogui.PAUSE = 0.5
# 1 entar sistema da empresa

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

site='https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(site)
pyautogui.press('enter')
time.sleep(3)

 
# 2 Fazer login
pyautogui.click(x=571, y=563) 
pyautogui.write('salvadorsantos@gmail.com')

pyautogui.press('tab')
pyautogui.write('abcde') 

pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3) 

#3 Importar base de dados
import pandas as pd
df_produtos =pd.read_csv('produtos.csv')
print(df_produtos)


#4 cadastrar um produto

for linha in df_produtos.index:

    pyautogui.click(x=572, y=395)

    codigo =df_produtos.loc[linha, 'codigo'] 
    pyautogui.write(codigo)

    pyautogui.press('tab')
    marca = df_produtos.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = df_produtos.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(df_produtos.loc[linha, 'categoria']) 
    pyautogui.write(categoria)

    pyautogui.press('tab')
    preco_unitario = str(df_produtos.loc[linha, 'preco_unitario']) 
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')
    custo = str(df_produtos.loc[linha, 'custo']) 
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(df_produtos.loc[linha, 'obs']) 
    if obs != 'nan':    
         
          pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)

#5 Repetir para todos os produtos



#pyautogui - fazer automaçoes com py

