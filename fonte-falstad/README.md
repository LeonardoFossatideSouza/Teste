# Atividade prática — Eletrônica de Potência (Fonte Chaveada Flyback)

SENAI SSP · Técnico em Eletrônica · 2026 · valor 10 pontos
Aluno: Leonardo Fossati de Souza Nunes

Montagem e simulação de uma fonte chaveada flyback de 12 V / 1 A com operação
bivolt automática (127 V / 220 V) e malha de realimentação, no simulador Falstad.

## Entregáveis

- `../Relatorio_Fonte_Chaveada_Leonardo_Fossati.pdf` — relatório final
- `../Links_Circuitos_Fonte_Chaveada.txt` — links dos circuitos
- `links.txt` — idem

## Circuitos

| Arquivo | Descrição |
|---|---|
| `fonte_127V.txt` | Circuito principal — entrada 180 V de pico (rede 127 V) |
| `fonte_220V.txt` | Mesmo circuito com entrada de 311 V de pico (rede 220 V) |
| `variantes/220V_carga_leve.txt` | 220 V com a carga trocada de 12 Ω para 120 Ω |
| `variantes/roteiro_literal.txt` | Montagem literal do roteiro (amp-op ±15 V, sem compensação) — não regula |
| `variantes/mosfet_potencia.txt` | Principal com MOSFET de potência (β = 5), usado na comparação de ondulação |

### Topologia

Rede CA → ponte de 4 diodos → capacitor de barramento 47 µF → transformador
flyback (1 mH, relação 0,1, acoplamento 0,99, pontos invertidos) chaveado por
MOSFET canal N com snubber RC 10 kΩ + 10 nF → diodo rápido → capacitor de
saída 470 µF → carga 12 Ω.

Controle: divisor 10 k/10 k na saída → amplificador de erro (referência 6 V,
capacitor de compensação 100 nF, excursão limitada a 0 … −5 V) → comparador PWM
contra rampa dente de serra de 20 kHz → resistor de 100 Ω → gate.

Os arquivos estão no formato de texto do Falstad e podem ser carregados em
**File > Import from Text**.

## Capturas

`shots_hd/` — capturas em alta resolução do simulador em execução:

- `E1_127V.png` — operação em 127 V AC
- `E2_220V.png` — teste bivolt em 220 V AC
- `E3_carga_leve.png` — variação de carga (120 Ω)
- `E4_roteiro_literal.png` — montagem literal, travada em 100 % de razão cíclica
- `E5_mosfet_potencia.png` — comparação com MOSFET de potência

## Reprodução

- `lzstring.py` — `compressToEncodedURIComponent` do lz-string, para gerar os links `?ctz=`
- `genurl.py` — gera o link: `python3 genurl.py fonte_127V.txt`
- `snap.js` — abre um link no Falstad e captura a tela (Playwright)
- `finalizar.py` — injeta links e netlist no relatório
- `relatorio.html` / `topdf.js` — fonte do relatório e geração do PDF

Cada simulação precisa de ~170 s de execução no navegador para atingir o regime
permanente (passo de cálculo de 1 µs).
