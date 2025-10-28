# ETL Pipeline Simples (XLSX -> único arquivo)

## Descrição

Pequeno projeto de exemplo que implementa um pipeline ETL em três etapas:

- Extração: lê 50 arquivos Excel (.xlsx) de uma pasta de entrada.
- Transformação: concatena os DataFrames lidos em um único DataFrame.
- Carga: grava o resultado concatenado em um único arquivo de saída.

## Estrutura do projeto

```
pyproject.toml
app/
    main.py            # orquestra extract -> transform -> load
    pipeline/
        extract.py     # lógica de leitura dos .xlsx
        transform.py   # concatenação/limpeza básica
        load.py        # grava o arquivo final em data/output
data/
    input/             # coloque aqui os 50 arquivos .xlsx
    output/            # saída do pipeline
tests/
    test_pipeline.py   # testes automáticos
```

## Contrato (inputs / outputs / erros)

- Inputs:

  - Diretório `data/input` contendo aproximadamente 50 arquivos no formato `.xlsx`.
  - Cada arquivo deve conter uma planilha com colunas compatíveis para concatenação (mesmos nomes/ordens preferencialmente).

- Output:

  - Um arquivo único na pasta `data/output` (nome e formato definido pelo parâmetro de carga; por padrão, por exemplo `output.csv` ou `output.xlsx`).

- Modos de erro / validações:
  - Falha se não houver arquivos `.xlsx` no diretório de entrada.
  - Falha/aviso se os arquivos tiverem esquemas incompatíveis (colunas diferentes). A estratégia atual é levantar erro ou preencher/alinhar colunas dependendo da implementação em `transform.py`.

## Como funciona (resumo técnico)

1. `extract(path)`

   - Varre `path` procurando arquivos `.xlsx`.
   - Lê cada arquivo em um DataFrame e retorna uma lista de DataFrames.

2. `transform(df_list)`

   - Recebe a lista de DataFrames e concatena verticalmente (pandas.concat).
   - Realiza limpeza mínima (remoção de duplicatas, normalização de tipos, tratamento de NaNs) conforme implementado.

3. `load(df, output_path, filename)`
   - Grava o DataFrame resultante em `output_path/filename` no formato escolhido.

## Como rodar

Requisitos

- Python 3.8+ (ver `pyproject.toml`).
- Instale dependências (se houver `requirements.txt`) ou via poetry/poetry install.

Exemplos de execução (no Zsh / Linux):

```zsh
# rodar o pipeline principal
python -m app.main

# rodar os testes automatizados (pytest)
pytest -q
```

Observações:

- `app/main.py` já chama `extract("data/input")`, `transform(...)` e `load(...)` por padrão.
- Verifique que existem ~50 arquivos `.xlsx` em `data/input` antes de rodar.

## Verificação rápida / Debug

- Após rodar `python -m app.main`, verifique se há um arquivo novo em `data/output` com o nome configurado (por exemplo `output.csv` ou `output.xlsx`).
- Se o pipeline imprimir tipos (como `print(type(df_list))`), isso ajuda a confirmar que os dados foram lidos/transformados corretamente.
- Use `pandas` para inspecionar rapidamente: `python -c "import pandas as pd; print(pd.read_csv('data/output/output.csv').shape)"` (ajuste formato se for Excel).

## Edge cases comuns

- Arquivos ausentes: o script deve falhar de forma clara informando que nenhum `.xlsx` foi encontrado.
- Esquemas irregulares: colunas diferentes entre arquivos podem gerar NaNs ou erros. Recomenda-se normalizar colunas antes de concatenar.
- Arquivos corrompidos: captura de exceções ao ler cada arquivo e registro (log) dos arquivos que falharam, sem derrubar toda a execução, pode ser uma melhoria a implementar.

## Melhorias sugeridas (próximos passos)

- Adicionar `requirements.txt` com dependências (pandas, openpyxl, pytest, etc.).
- Log detalhado (biblioteca `logging`) e tratamento de erros por arquivo durante a leitura.
- Suportar variações de formato de saída (CSV/Excel/Parquet) via parâmetro.
- Adicionar CI com execução dos testes e checks de lint.

## Contato e Licença

Projeto de exemplo — gratuito para uso e adaptação. Se quiser, posso:

- Gerar o `requirements.txt` com versões mínimas.
- Implementar logs e tratamento de erros por arquivo.
- Adicionar testes adicionais cobrindo arquivos com esquemas diferentes.

---

README gerado automaticamente para ajudar a rodar e entender o pipeline ETL simples.
