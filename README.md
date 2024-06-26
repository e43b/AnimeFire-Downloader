# AnimeFire-Downloader

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
qualidade_desejada = 'F-HD'  # Pode ser 'SD', 'HD', 'F-HD', ou 'FullHD'
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

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias ou correções.

## Autor

Seu Nome <seu.email@example.com>

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

### Explicação do `README.md`:

- **Título e Descrição**: Informa o nome do projeto e uma breve descrição do que ele faz.
- **Funcionalidades**: Lista as principais funcionalidades oferecidas pelo script.
- **Requisitos**: Indica os requisitos necessários para executar o script.
- **Como Usar**: Instruções para clonar o repositório, instalar dependências e executar o script.
- **Exemplo de Uso**: Exemplo de como seria a interação com o script no terminal.
- **Contribuições**: Incentiva contribuições para o projeto.
- **Autor**: Informações sobre o autor do projeto.
- **Licença**: Especifica a licença sob a qual o projeto está disponível.

Certifique-se de adaptar as seções conforme necessário para o seu projeto específico. Isso proporcionará uma boa orientação para os usuários interessados no seu script de download de episódios de animes do AnimeFire.
