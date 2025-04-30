## Dashboard de Monitoramento do Preço dos Combustíveis no Brasil

![Image](https://github.com/user-attachments/assets/7ec7c076-8e51-4721-b1db-bc0ab276d5e8)

Este projeto apresenta um **dashboard interativo desenvolvido no Power BI** para acompanhar a evolução dos preços dos combustíveis no Brasil entre 2004 e 2022. A solução combina **Python e Power BI** para automatizar a coleta, tratamento e visualização dos dados.
> 🌐 **Acesse o dashboard online no Power BI Service:**  
[🔗 Ver Dashboard no Power BI Online](https://app.powerbi.com/view?r=eyJrIjoiYmFhNjQ0OTItMjdlYi00ODcyLTllMjQtMjFlNjdhODMxZDI1IiwidCI6IjRjYWNmYzIzLTM0MjItNGY0MC1iMjk0LWEyOGIzNGFkMzI0ZSJ9)

## Objetivo Profissional
Este projeto foi desenvolvido como parte do meu portfólio com o intuito de:
- Demonstrar minha capacidade de **integrar ferramentas** (Python + Power BI);
- Aplicar conhecimentos de **ETL, análise de dados e visualização interativa**;
- Apresentar uma **solução de monitoramento realista, automatizada e escalável**;

## Mini ETL Automatizado (Python)
Foi desenvolvido um script em Python responsável por:
- **Ler múltiplos arquivos CSV** armazenados em uma pasta;
- **Detectar automaticamente o encoding** de cada arquivo (usando `chardet`);
- **Filtrar apenas as colunas relevantes para análise**;
- **Concatenar todos os dados em um único DataFrame**, usado diretamente no Power BI;
- **Permitir atualização automática**: ao adicionar novos arquivos à pasta, o Power BI atualiza o dashboard com os novos dados.

> Acesse o notebook explicativo da ETL:
<a href="https://github.com/Hiagofb/DASHBOARD_COMBUSTIVEL/blob/master/ETL_DADOS_EXPLICANDO.ipynb" target="_blank" style="
  display: inline-block;
  padding: 10px 20px;
  background-color: #2ea44f;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  font-family: sans-serif;
">
📓 ETL_DADOS_EXPLICATIVO.ipynb
</a>

## Sobre os Dados
Os dados utilizados neste projeto referem-se aos **preços de combustíveis no Brasil entre 2004 e 2022**, coletados pela ANP (Agência Nacional do Petróleo) e organizados no Kaggle pelo usuário **samfaraday**.

<a href="https://www.kaggle.com/datasets/samfaraday/preco-gasolina-2004-a-2022-brasil" target="_blank" style="
  display: inline-block;
  padding: 10px 20px;
  background-color: #2ea44f;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  font-family: sans-serif;
">
🔗 Preço da Gasolina (2004 a 2022) – Brasil | Kaggle
</a>

## Como utilizar os dados neste repositório
> ⚠️ Por motivos de tamanho, a pasta com os arquivos de dados **não está incluída** no repositório (está listada no `.gitignore`).

Para reproduzir o projeto com os dados:
1. Acesse o link acima e faça o download do dataset;
2. Crie uma pasta chamada `DADOS` na raiz do projeto;
3. Extraia todos os arquivos CSV do dataset para dentro dessa pasta.
4. Abra o arquivo `.pbix` no Power BI Desktop — o script Python será executado automaticamente no carregamento dos dados.

### Por que os dados não estão incluídos no repositório?

Os arquivos de dados não foram incluídos no repositório devido ao **tamanho total elevado**.  
Como os arquivos CSV são grandes, o conjunto completo ultrapassaria os limites de armazenamento do GitHub, além de dificultar o versionamento e o carregamento do repositório.  
Por isso, os arquivos foram adicionados ao `.gitignore`, e orientações foram fornecidas para que qualquer pessoa possa baixá-los diretamente da fonte original (Kaggle).

---
### Tecnologias & Ferramentas Utilizadas:

<table>
  <tr>
    <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/New_Power_BI_Logo.svg/2048px-New_Power_BI_Logo.svg.png" width="50" height="40"/><br>Power BI</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="40"/><br>Python</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="40" height="40"/><br>Pandas</td>
</table>

---

### 📫 Contato
<div style="display: inline-block"> 
  <a href="https://www.linkedin.com/in/hiago-fernandess/" target="_blank">
  <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
</a> 
  <a href="mailto:hiago_fernandes[at]ymail.com" target="_blank">
  <img src="https://img.shields.io/badge/YahooMail-%236200D8?style=for-the-badge&logo=yahoo&logoColor=white" target="_blank">
</a>
</div>

---

<a href="https://github.com/Hiagofb" target="_blank" style="
  display: inline-block;
  padding: 10px 20px;
  background-color: #0366d6;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  font-family: sans-serif;
">
🔙 Voltar para o Portfólio
</a>
