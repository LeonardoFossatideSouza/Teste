# Atividade prática — Eletrônica de Potência (Conversor DC/DC Step-Up Boost)

SENAI SSP · Técnico em Eletrônica · 2026
Aluno: Leonardo Fossati de Souza Nunes

Montagem e simulação de um conversor DC/DC elevador (Boost) no simulador Falstad,
com relatório respondendo às questões de análise e discussão.

## Entregáveis

- `../Relatorio_Boost_Leonardo_Fossati.pdf` — relatório final (13 páginas)
- `../Links_Circuitos_Boost.txt` — os dois links dos circuitos
- `links.txt` — idem

## Circuitos

| Arquivo | Descrição |
|---|---|
| `boost_principal.txt` | Circuito 1 — Boost com MOSFET de potência (β = 5, Rds(on) ≈ 24 mΩ). Reproduz os valores previstos no roteiro. |
| `boost_mosfet_padrao.txt` | Circuito 2 — mesmo circuito com o MOSFET nos parâmetros de fábrica do Falstad (β = 0,02, Rds(on) = 5,88 Ω). |
| `variantes/D_*.txt` | Circuito 2 nas três razões cíclicas pedidas (25 / 50 / 75 %) |
| `variantes/ideal_D_*.txt` | Circuito 1 nas três razões cíclicas |
| `variantes/ripple_*.txt` | Circuito 1 a 1 kHz e 10 kHz, com osciloscópio em acoplamento AC para medir o ripple |
| `variantes/sem_carga.txt` | Circuito 1 com o resistor de carga removido (saída em aberto) |

Topologia: fonte CC 12 V → indutor 10 mH → nó de comutação (dreno do MOSFET N +
anodo do diodo) → diodo → capacitor 100 µF ‖ resistor 100 Ω. Gate acionado por
fonte quadrada de 1 kHz, ±10 V.

Os arquivos estão no formato de texto do Falstad e podem ser carregados em
**File > Import from Text**.

## Capturas

`shots_hd/` — capturas em alta resolução do simulador em execução:

- `C1_D0{25,50,75}.png` — Circuito 1 nas três razões cíclicas
- `C2_D0{25,50,75}.png` — Circuito 2 nas três razões cíclicas
- `ripple_{1,10}kHz.png` — comparação do ripple
- `sem_carga_t*.png` — saída em aberto, em três instantes

## Reprodução

- `lzstring.py` — implementação de `compressToEncodedURIComponent` do lz-string,
  usada para gerar os links `?ctz=` do Falstad
- `genurl.py` — gera o link a partir de um arquivo de circuito:
  `python3 genurl.py boost_principal.txt`
- `snap.js` — abre um link no Falstad e captura a tela (Playwright)
- `relatorio.html` / `topdf.js` — fonte do relatório e geração do PDF
