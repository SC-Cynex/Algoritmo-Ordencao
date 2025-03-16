# Análise de Algoritmos de Ordenação

Este projeto tem como objetivo implementar, comparar e analisar a performance de diferentes algoritmos de ordenação. Ele utiliza o padrão **Strategy** para garantir modularidade e extensibilidade, além de ferramentas como **OpenTelemetry** para registro de logs e métricas.

## 📌 Instalação

### 🔧 Pré-requisitos
- Python 3.8 ou superior.
- Gerenciador de pacotes `pip`.

### 📥 Clone do repositório:
```bash
git clone https://github.com/SC-Cynex/Algoritmo-Ordencao
cd Algoritmo-Ordencao
```

### ▶️ Execução dos Algoritmos
Para executar os algoritmos de ordenação e comparar seu desempenho, use o seguinte comando:

```bash
python main.py
```
O programa carregará os dados da pasta dados/, executará cada algoritmo e exibirá métricas como tempo de execução, comparações e trocas.

## 📊 Visualizando Logs e Métricas

**Logs:** Os logs de execução são registrados usando OpenTelemetry e podem ser visualizados na ferramenta configurada (ex: Jaeger, Elasticsearch + Kibana).

**Métricas:** As métricas de desempenho são exportadas para Prometheus e podem ser visualizadas no Grafana.


## 📂 Estrutura do Projeto

```bash
/projeto-ordenacao
├── algoritmos/          # Implementações dos algoritmos de ordenação
├── data/                # Conjuntos de dados gerados
├── logs/                # Logs de execução
├── utils/               # Utilitários (gerador de dados, leitor de dados, logger)
├── main.py              # Ponto de entrada do programa
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
```

## 🛠️ Ferramentas Utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-FFFFFF?&style=for-the-badge&logo=opentelemetry&logoColor=black)

- **Python:** Linguagem de programação utilizada para implementação.

- **OpenTelemetry:** Para coleta de métricas, logs e traces.

- **Jaeger:** Para visualização e análise de traces.
  
![image](https://github.com/user-attachments/assets/213e7b04-c421-4fcf-ac01-a666bfc44155)

## 👨‍💻 Desenvolvedores

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/humberto-peres"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118866895?s=400&u=a12412e21705d58ab604be67c1e1431c80174b64&v=4" width="100px;" alt=""/><br /><sub><b>Humberto Peresd</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/WesllyHn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/117309594?v=4" width="100px;" alt=""/><br /><sub><b>Weslly Neres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/Pellegr1n1"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/119978954?v=4" width="100px;" alt=""/><br /><sub><b>Leandro Pellegrini</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/v0cs"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104214178?v=4" width="100px;" alt=""/><br /><sub><b>Vítor Celestino</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">🚀</a></td>
  </tr>
