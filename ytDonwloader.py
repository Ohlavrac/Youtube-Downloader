from PySimpleGUI import PySimpleGUI as pg
from pytube import YouTube
import validLink

#LAYOUT
pg.theme('DarkTeal') #TEMA DA JANELA 

#FORMATO DO LAYOUT
layout = [
    [pg.Text('Link do video para Downlaod', size=(20,1)), pg.Input(key='linkDownload')],
    [pg.Text('Local de Destino', size=(20, 1)), pg.InputText(key='DefaultFolder'), pg.FolderBrowse()],
    [pg.Button('Donwload'), pg.Button('Sair')]
]

#JANELA

window = pg.Window('Youtube Downloader', icon='./icon.ico').layout(layout)

#LER EVENTOS
while True:
    event, action = window.read()
    if event == pg.WINDOW_CLOSED:
        window.close()
        break
    if event == 'Sair':
        window.close()
        break

    if event == 'Donwload':
        link = str(action['linkDownload'])
        folder = str(action['DefaultFolder']) 
        if action['linkDownload'] == '' or validLink.validLinkfunc(link) == False: #VERIFICA SE O INICIO DO LINK É VALIDO
            pg.popup('O link informado é invalido')

        if validLink.validLinkfunc(link) == True:
            YouTube(f'{link}').streams.filter(only_audio=True).first().download(r"{}".format(folder)) #PASSA A LOCALIZAÇÃO DA PASTA PARA O DOWNLOAD
            yt = YouTube(f'{link}')
            yt.streams

            pg.popup('Download completo com sucesso')

