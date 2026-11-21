# Testes e validação — Mica Português

## Resultado

**Resultado: PASSOU.** Validação estática e teste de interação em Chromium realizados em 21/11/2026.

- 30 perguntas do quiz: todas têm quatro alternativas, índice de resposta válido, explicação e tema; não há enunciados duplicados.
- 8 pares para associação, colunas e memória; 12 afirmações de verdadeiro/falso.
- Sete modos identificados e acessíveis pela tela de jogos.
- Níveis conferidos: fácil 90 segundos/3 vidas, normal 60 segundos/4 vidas e difícil 30 segundos/5 vidas.
- Pulo no quiz e em verdadeiro/falso move o item para o fim da fila, sem removê-lo.
- O caça-palavras foi testado em 250 configurações aleatórias para verificar se todas as oito palavras podem ser colocadas sem sobreposição.
- O tabuleiro de palavras cruzadas tem duas interseções verificadas e sem conflito de letras.
- Chromium percorreu o resumo e suas abas, iniciou os sete jogos, acertou pares/colunas/memória, encontrou todas as palavras do caça-palavras e completou as seis pistas das palavras cruzadas.
- Controles de som e volume, dica, acerto e erro foram exercitados.
- Nenhum erro JavaScript foi registrado no teste de navegação automatizado.

## Limites do teste

A validação foi feita com Chromium headless usando o conteúdo local da aplicação. Não substitui testes em celulares Android físicos, diferentes versões de navegadores ou testes de acessibilidade com leitores de tela.

O service worker e o fluxo de instalação PWA foram conferidos estaticamente, mas a publicação real pelo GitHub Pages ainda depende do envio dos arquivos e da ativação de Pages.

**APK:** não foi gerado. O ambiente não tinha Android SDK, Gradle ou ADB configurados. A entrega é um PWA instalável.
