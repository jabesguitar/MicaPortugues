# Mica Português — Estudo & Desafio

Aplicação educativa para revisão de Português — 6º ano (SAE Digital), organizada a partir das páginas do Livro do Aluno enviadas nesta conversa.

## O que está incluído

- Resumo navegável com crônica de ficção, leitura de **“Amizade & Futebol”**, concordância verbal e produção escrita.
- Complemento **“Ficção e Linguagem”**, identificado como complemento porque esse título não aparece nas fotografias recebidas.
- Quiz principal com 30 perguntas únicas, alternativas embaralhadas e explicação de resposta.
- Sete formatos: quiz, verdadeiro ou falso, associe pergunta e resposta, ligue as colunas, jogo da memória, caça-palavras e palavras cruzadas.
- Três níveis: fácil (1min30 por pergunta, 3 vidas), normal (1min por pergunta, 4 vidas) e difícil (30s por pergunta, 5 vidas).
- A pergunta pulada vai para o fim da fila; não é descartada.
- Dicas, som de acerto/erro, trilhas sintetizadas diferentes por jogo, botão e controle de volume.
- PWA instalável e cache offline da interface principal.

## Abrir localmente

Abra `index.html` em um navegador moderno. Para testar instalação/offline, sirva a pasta por um servidor HTTP local, por exemplo:

```bash
python -m http.server 8080
```

Acesse `http://localhost:8080`.

## Colocar este projeto no repositório GitHub

1. Baixe e extraia o ZIP desta entrega.
2. Abra o repositório `https://github.com/jabesguitar/MicaPortugues`.
3. Clique em **Add file → Upload files**.
4. Abra a pasta `MicaPortugues` extraída e arraste o conteúdo dela (não a pasta externa inteira) para a área de upload. `index.html` deve ficar na raiz do repositório.
5. Clique em **Commit changes**.
6. Depois, abra **Settings → Pages**.
7. Em **Build and deployment**, selecione **Deploy from a branch**, branch `main`, pasta `/ (root)` e clique em **Save**.
8. Abra a URL que o GitHub Pages mostrar.

## Instalar no Android

Depois de publicar o site via HTTPS, abra o endereço no Chrome do Android, use o menu do navegador e selecione **Instalar app** ou **Adicionar à tela inicial**. A interface pode ser usada como aplicativo PWA.

## Sobre APK nativo

Esta entrega é um **PWA instalável**, não um APK Android nativo compilado. O ambiente desta execução não tem Android SDK, Gradle ou ADB configurados para gerar e testar um APK assinado. Para gerar um APK nativo será necessária uma etapa de empacotamento com Capacitor/Android Studio e uma compilação Android.

## Arquivos principais

- `index.html`, `styles.css`, `app.js`: aplicação e launcher.
- `src/questions.js`: banco de perguntas, pares e verdadeiro/falso.
- `docs/RESUMO-PORTUGUES-6ANO.md`: resumo para estudar.
- `manifest.webmanifest` e `sw.js`: instalação PWA e cache offline.
- `assets/icon-1024.png` e `assets/icon-4096.png`: ícone quadrado transparente.
- `assets/launcher-1600x900.png`: arte de apresentação do projeto.
- `test-results/`: validação e evidências de teste.
