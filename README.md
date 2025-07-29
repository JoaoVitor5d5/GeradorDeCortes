# Gerador de Cortes

Este é um aplicativo em Python de linha de comando que baixa um vídeo do YouTube, transcreve seu áudio, identifica trechos emocionalmente expressivos e gera clipes de vídeo verticais com legendas animadas.

-----

## Como Funciona

O programa automatiza as seguintes etapas:

1.  **Download do Vídeo:** Baixa o vídeo do YouTube usando o link fornecido.
2.  **Transliteração de Áudio:** Converte o áudio do vídeo em texto usando modelos de IA.
3.  **Análise de Emoções:** Identifica segmentos de texto que expressam emoções (como alegria, surpresa, raiva, amor, tristeza, medo) para encontrar os pontos altos.
4.  **Geração de Clipes:** Com base nos segmentos mais expressivos e nas durações configuradas, ele cria clipes de vídeo verticais (formato ideal para Shorts, TikTok, Kwai) com legendas animadas.

-----

## Pré-requisitos

Para utilizar este programa, você precisará ter o **Python** instalado em seu sistema, juntamente com algumas bibliotecas específicas.

1.  **Python 3.8 ou superior:**

      * Baixe e instale a versão mais recente do Python para o seu sistema operacional em [python.org](https://www.python.org/downloads/).
      * **Importante:** Durante a instalação, marque a opção "Add Python to PATH" (Adicionar Python ao PATH) para facilitar o uso no terminal.

2.  **Git (Opcional, mas Recomendado):**

      * Para clonar este repositório facilmente. Baixe em [git-scm.com](https://git-scm.com/downloads).

-----

## Passo a Passo para Utilizar

Siga estas instruções para configurar e executar o projeto:

### 1\. Clonar o Repositório

Abra seu **Prompt de Comando (CMD)** ou **PowerShell** e clone este repositório:

```bash
git clone https://github.com/JoaoVitor5d5/GeradorDeCortes.git
cd GeradorDeCortes # Navegue até a pasta do projeto
```

### 2\. Criar e Ativar um Ambiente Virtual (Recomendado)

É uma boa prática criar um ambiente virtual para gerenciar as dependências do projeto. Isso evita conflitos com outras instalações de Python.

```bash
python -m venv venv
```

**Para ativar o ambiente virtual:**

  * **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
  * **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3\. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas listadas no seu `requirements.txt`:

```bash
pip install -r requirements.txt
```

As dependências incluídas no `requirements.txt` são:

  * `pytube`

  * `moviepy`

  * `openai-whisper`

  * `transformers`

  * `torch`

  * `ffmpeg-python`

  * `numpy`

  * `yt-dlp`

  * **Observação sobre `torch`:** A instalação de `torch` pode ser grande. Para usuários de CPU, a instalação padrão através do `requirements.txt` geralmente funciona. Se você tiver uma **GPU NVIDIA** e quiser aproveitar o desempenho, é altamente recomendado visitar o [site oficial do PyTorch](https://pytorch.org/get-started/locally/) e usar o comando de instalação específico para sua configuração (incluindo CUDA) *antes* de executar `pip install -r requirements.txt`.


### 4\. Executar o Programa

Após instalar as dependências e ter a fonte no local correto, você pode executar o programa.

**Uso:**

```bash
python main.py <LINK_DO_VIDEO_DO_YOUTUBE>
```

Substitua `<LINK_DO_VIDEO_DO_YOUTUBE>` pelo URL completo do vídeo que você deseja processar. **Coloque o link entre aspas duplas (`"`)** para evitar problemas com caracteres especiais.

**Exemplo:**

```bash
python main.py "https://youtu.be/4Z2Im13A_bw?si=XMu0auAhT9o9OjPQ"
```

-----

## Saída

Os clipes de vídeo gerados serão salvos na pasta `output`, que será criada automaticamente na raiz do seu projeto. Os arquivos serão no formato MP4.

-----

## Configurações Padrão

As seguintes configurações estão atualmente fixas no código-fonte em `utils/highlight_segments.py`:

  * **Duração Mínima do Clipe (`min_clip_duration`):** 60 segundos
  * **Número Máximo de Clipes Gerados (`max_results`):** 6

Se desejar alterar esses valores, você precisará editar o arquivo `utils/highlight_segments.py` diretamente.

-----

## Contribuição

Sinta-se à vontade para contribuir com este projeto\! Abra "issues" para relatar bugs ou sugerir melhorias, e "pull requests" com suas contribuições.

-----
