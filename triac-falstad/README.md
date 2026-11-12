# Atividade prática — Eletrônica de Potência (TRIAC)

SENAI SSP · Técnico em Eletrônica · 2026
Aluno: Leonardo Fossati de Souza Nunes

Montagem e simulação de dois circuitos de acionamento de carga CA com TRIAC
no simulador Falstad, com relatório respondendo às questões conceituais Q1–Q4.

## Entregáveis

- `../Relatorio_TRIAC_Leonardo_Fossati.pdf` — relatório final (12 páginas)
- `../Links_Circuitos_Falstad.txt` — os dois links dos circuitos
- `links.txt` — idem

## Circuitos

| Arquivo | Descrição |
|---|---|
| `parte_A_chave_estatica.txt` | Parte A — chave estática CA (TRIAC + chave + fonte CC de 5 V + resistor de gate de 100 Ω) |
| `parte_B_dimmer_diac.txt` | Parte B — controle de potência por ângulo de fase (rede RC 10 kΩ + 250 kΩ + 100 nF e DIAC) |
| `variantes/` | Mesmos circuitos com a chave aberta e com o potenciômetro em várias posições, usados para as capturas |

Os arquivos estão no formato de texto do Falstad e podem ser carregados em
**File > Import from Text**.

## Capturas

`shots_hd/` — capturas em alta resolução do simulador em execução, usadas como
figuras do relatório.

## Reprodução

- `lzstring.py` — implementação de `compressToEncodedURIComponent` do lz-string,
  usada para gerar os links `?ctz=` do Falstad
- `genurl.py` — gera o link a partir de um arquivo de circuito:
  `python3 genurl.py parte_A_chave_estatica.txt`
- `snap.js` — abre um link no Falstad e captura a tela (Playwright)
- `relatorio.html` / `topdf.js` — fonte do relatório e geração do PDF
