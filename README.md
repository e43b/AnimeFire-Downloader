# AnimeFire-Downloader [![Views](https://hits.sh/github.com/e43banifire/hits.svg)](https://github.com/e43b/Anibunker-Downloader/)

Este é um script Python para baixar episódios de animes do site AnimeFire.plus. Ele permite extrair links de episódios de uma página principal de um anime específico e baixar os vídeos em diferentes qualidades disponíveis.

## Funcionalidades

- Extrai automaticamente os links de episódios de uma página principal do AnimeFire.plus.
- Permite escolher a qualidade desejada para o download (SD, HD, F-HD).
- Opção de baixar todas as qualidades disponíveis ou apenas a qualidade preferida.
- Organiza os vídeos baixados em pastas com o nome do anime e número do episódio.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/e43b/AnimeFire-Downloader.git
   ```

2. Instale as dependências:
   ```bash
   cd codes
   ```

3. Execute o script:
   ```bash
   python main.py
   ```

4. Siga as instruções no terminal para inserir o link da página principal do anime, escolher a qualidade desejada e outras opções.

## Exemplo de Uso

```bash
Insira o link da página principal do anime: https://animefire.plus/animes/one-piece-dublado-todos-os-episodios
```

## Configurações adicionais

Nos códigos `codes/ep.py` e `codes/anime.py`, existem algumas variáveis que permitem personalizar alguns aspectos da ferramenta:

### Escolha da Qualidade Desejada

Você pode escolher a qualidade desejada modificando a variável `qualidade_desejada`. Por padrão, ela está configurada para 'F-HD', mas pode ser alterada para uma das seguintes opções: 'SD', 'HD', 'F-HD', ou 'FullHD'.

```python
qualidade_desejada = 'F-HD'  # Pode ser 'SD', 'HD' ou 'F-HD'
```

### Baixar Todas as Qualidades Disponíveis

Você pode optar por baixar todas as qualidades disponíveis para o vídeo configurando a variável `baixar_todas_qualidades` como `True` ou `False`.

```python
baixar_todas_qualidades = False
```

### Cooldown entre Downloads

É recomendável configurar um tempo de espera entre os downloads para evitar bloqueios ou banimentos do servidor. Por padrão, este tempo é de 20 segundos. Você pode ajustar essa configuração conforme necessário.

```python
intervalo_entre_downloads = 20  # Tempo em segundos entre os downloads
```

Certifique-se de configurar essas variáveis de acordo com suas preferências antes de executar o script.


## Contribuições

Este projeto é de código aberto e você é encorajado a contribuir para melhorias e novas funcionalidades. Sinta-se à vontade para enviar sugestões, relatar problemas ou enviar pull requests através do [repositório oficial no GitHub](https://github.com/e43b/AnimeFire-Downloader/).

## Autor

Desenvolvido e mantido por [E43b](https://github.com/e43b), o AnimeFire Downloader visa simplificar o processo de download de animes, proporcionando uma experiência mais acessível e organizada para os fãs de anime.

## Links

- Repositório do Projeto: [https://github.com/e43b/AnimeFire-Downloader/](https://github.com/e43b/AnimeFire-Downloader/)
- Site AnimeFire: [https://animefire.plus/](https://animefire.plus/)

