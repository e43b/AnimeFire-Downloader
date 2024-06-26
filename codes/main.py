import os

# Função para limpar a tela do console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para baixar episódios específicos
def baixar_episodios():
    limpar_tela()
    print("Executando script para baixar episódios específicos...")
    os.system('python ep.py')
    input("\nPressione Enter para voltar ao menu...")

# Função para baixar um anime completo
def baixar_anime_completo():
    limpar_tela()
    print("Executando script para baixar um anime completo...")
    os.system('python anime.py')
    input("\nPressione Enter para voltar ao menu...")

# Verificar e instalar as dependências necessárias
def verificar_instalar_dependencias():
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("Bibliotecas necessárias não encontradas.")
        choice = input("Deseja instalar as bibliotecas necessárias? (s/n): ").strip().lower()
        if choice == 's':
            os.system('pip install -r requirements.txt')
        else:
            print("Instalação cancelada. O programa pode não funcionar corretamente.")
            input("\nPressione Enter para continuar...")

# Menu principal
def menu():
    verificar_instalar_dependencias()

    while True:
        limpar_tela()
        print("""
    _          _                _____ _          
   / \   _ __ (_)_ __ ___   ___|  ___(_)_ __ ___ 
  / _ \ | '_ \| | '_ ` _ \ / _ \ |_  | | '__/ _ \
 / ___ \| | | | | | | | | |  __/  _| | | | |  __/
/_/__ \_\_| |_|_|_| |_| |_|\___|_|   |_|_|  \___|
|  _ \  _____      ___ __ | | ___   __ _  __| |  
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |  
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|  

Criado por E43b
GitHub: https://github.com/e43b
Discord: https://discord.gg/GgBbbjDkXu
Repositório do Projeto: https://github.com/e43b/AnimeFire-Downloader/

Com este script, é possível baixar episódios e animes completos do site https://animefire.plus/

Escolha uma opção:
1 - Baixar episódios específicos
2 - Baixar um anime completo
3 - Sair do programa
""")
        opcao = input("Digite sua escolha (1/2/3): ")

        if opcao == '1':
            baixar_episodios()
        elif opcao == '2':
            baixar_anime_completo()
        elif opcao == '3':
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")
            input("Pressione Enter para continuar...")

# Executar o programa
if __name__ == "__main__":
    menu()
