import os
import requests
from bs4 import BeautifulSoup
import re
import time

# Função para extrair nome da obra e número do episódio a partir do link original
def extrair_info_do_link(link):
    match = re.search(r'animes/([^/]+)/(\d+)', link)
    if match:
        nome_obra = match.group(1)
        numero_episodio = match.group(2)
        return nome_obra, numero_episodio
    return None, None

# Função para modificar o link para o link de download
def modificar_link_para_download(nome_obra, numero_episodio):
    return f'https://animefire.plus/download/{nome_obra}/{numero_episodio}'

# Função para extrair links das qualidades disponíveis
def extrair_links_de_qualidade(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = {}
    qualidade_tags = soup.find_all('a', href=True)
    for tag in qualidade_tags:
        qualidade_texto = tag.text.strip()
        if qualidade_texto in ['SD', 'HD', 'F-HD', 'FullHD']:
            links[qualidade_texto] = tag['href']
    return links

# Função para baixar e salvar o vídeo
def baixar_e_salvar_video(url, caminho_do_arquivo):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        os.makedirs(os.path.dirname(caminho_do_arquivo), exist_ok=True)
        with open(caminho_do_arquivo, 'wb') as f:
            for chunk in resposta.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f'Vídeo salvo em: {caminho_do_arquivo}')
    else:
        print(f'Falha ao baixar o vídeo de {url}')

# Entrada do usuário para links dos episódios
links_episodios = input("Insira os links dos episódios separados por vírgula: ").split(',')

# Qualidade desejada e opção de baixar todas as qualidades
qualidade_desejada = 'F-HD'  # Pode ser 'SD', 'HD' ou 'F-HD'
baixar_todas_qualidades = False

# Intervalo de 20 segundos entre os downloads para evitar sobrecargas
intervalo_entre_downloads = 20

# Processando cada link fornecido pelo usuário
for link_original in links_episodios:
    link_original = link_original.strip()
    
    # Extraindo nome da obra e número do episódio
    nome_obra, numero_episodio = extrair_info_do_link(link_original)
    
    if nome_obra and numero_episodio:
        # Modificando o link para o link de download
        link_download = modificar_link_para_download(nome_obra, numero_episodio)
        print(f'Link de download: {link_download}')
        
        # Fazendo a requisição à página de download
        response = requests.get(link_download)
        if response.status_code == 200:
            html = response.text
            # Extraindo links das qualidades disponíveis
            links_de_qualidade = extrair_links_de_qualidade(html)
    
            if baixar_todas_qualidades:
                for qualidade, link in links_de_qualidade.items():
                    caminho_do_arquivo = f'anime_fire/{nome_obra}/{numero_episodio}_{qualidade.lower()}.mp4'
                    baixar_e_salvar_video(link, caminho_do_arquivo)
            else:
                qualidades_preferidas = ['FullHD', 'F-HD', 'HD', 'SD']
                for qualidade in qualidades_preferidas:
                    if qualidade_desejada == qualidade and qualidade in links_de_qualidade:
                        caminho_do_arquivo = f'anime_fire/{nome_obra}/{numero_episodio}_{qualidade.lower()}.mp4'
                        baixar_e_salvar_video(links_de_qualidade[qualidade], caminho_do_arquivo)
                        break
                else:
                    # Se a qualidade desejada não estiver disponível, baixar a melhor qualidade disponível
                    for qualidade in qualidades_preferidas:
                        if qualidade in links_de_qualidade:
                            caminho_do_arquivo = f'anime_fire/{nome_obra}/{numero_episodio}_{qualidade.lower()}.mp4'
                            baixar_e_salvar_video(links_de_qualidade[qualidade], caminho_do_arquivo)
                            break
        else:
            print('Não foi possível acessar a página de download.')
    else:
        print('Não foi possível extrair as informações do link original.')
    
    # Intervalo de 20 segundos entre os downloads
    print(f'Aguardando {intervalo_entre_downloads} segundos antes de baixar o próximo episódio...')
    time.sleep(intervalo_entre_downloads)
