# 📊 Aula 2 - Análise de dados

> Projeto de Análise de Dado com Python, com o objetivo de identificar padrões de cancelamento em uma empresa de serviços por assinatura e investigar fatores associados à desistência dos clientes.

## 📌 Sobre o Projeto

O estudo apresenta um cenário onde uma empresa com mais de 800 mil clientes identificou um alto volume de cancelamento dos serviços. Com o objetivo de compreender os principais motivos em torno do alto índice de cancelamento, foi feita uma analise da base de dados de clientes dessa empresa utilizando Python, permitindo identificar padrões de comportamento, investigar indicadores e avaliar um cenário hipotético de redução desse índice.

O projeto faz parte do minicurso Jornada Python oferecido pela Hashtag Treinamentos, com o intuito de aprender fundamentos básicos de análise e tratamento de dados utilizando as bibliotecas Pandas e Plotly.

## 🎯 Objetivos

- Analisar a base de dados e compreender as características dos clientes.
- Realizar o tratamento e a preparação dos dados para análise.
- Identificar a quantidade e o percentual de clientes que cancelaram o serviço.
- Investigar fatores associados ao cancelamento por meio de gráficos e indicadores.
- Avaliar como a aplicação de determinados filtros altera o percentual de cancelamento da base analisada.

## ⚙️ Etapas do Projeto

**1. Importação dos Dados**

Importação da base de dados em formato CSV utilizando a biblioteca Pandas, possibilitando a manipulação e a análise das informações.

**2. Visualização e Exploração dos Dados**

Análise inicial da estrutura da base de dados, identificação das informações disponíveis e remoção da coluna CustomerID, por não ser necessária para as análises realizadas.

**3. Tratamento dos Dados**

Verificação dos tipos de dados e remoção de registros com valores ausentes, utilizando o método dropna() do Pandas, para preparar a base para as próximas etapas.

**4. Análise Inicial**

Identificação da quantidade de clientes que cancelaram e que permaneceram no serviço, além do cálculo do percentual de cada grupo em relação à base analisada.

**5. Análise Detalhada**

Criação de gráficos interativos com Plotly para investigar a relação entre as características dos clientes e o cancelamento do serviço.

Foram analisados três indicadores principais:

- Ligações para o Call Center: investigação da relação entre a quantidade de ligações realizadas pelos clientes e o cancelamento.
- Dias de atraso no pagamento: análise da relação entre os atrasos nos pagamentos e a desistência do serviço.
- Duração do contrato: comparação dos cancelamentos de acordo com a modalidade de contratação.

**6. Simulação de um Cenário de Redução de Cancelamentos**

Aplicação de filtros na base de dados para excluir os clientes que possuem determinadas características associadas a maiores índices de cancelamento:

- Contratos com duração mensal.
- Clientes com mais de 4 ligações para o Call Center.
- Clientes com mais de 20 dias de atraso no pagamento.

Após a aplicação dos filtros, foi calculado novamente o percentual de cancelamento para avaliar a mudança em relação à base original.

## 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e ferramentas foram utilizadas no desenvolvimento:

- **Python:** linguagem de programação utilizada para o desenvolvimento do projeto.
- **Pandas:** biblioteca utilizada para importação, manipulação, tratamento e análise dos dados.
- **Plotly Express:** biblioteca utilizada para a criação de gráficos interativos.
- **Jupyter Notebook:** ambiente utilizado para desenvolver e documentar as etapas da análise.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram praticados os seguintes conceitos:

- Importação e leitura de arquivos CSV.
- Exploração e tratamento de dados com Pandas.
- Identificação e remoção de valores ausentes.
- Análise exploratória de dados (EDA).
- Cálculo de quantidades e percentuais.
- Criação e interpretação de gráficos interativos.
- Identificação de padrões e relações entre variáveis.
- Aplicação de filtros para segmentação de dados.
- Comparação de indicadores antes e depois da aplicação de filtros.

--- 

## 👩‍💻 Autora

**Eliana Silva Nascimento**

- [GitHub](https://github.com/elianasilvanascimentoweb061)
- [LinkedIn](https://www.linkedin.com/in/eliana-da-silva-nascimento-728121250/)
