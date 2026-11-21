# Guia de instalação e publicação — Mica Português

## 1. Uso no computador

Extraia o pacote ZIP. Abra `index.html` no Chrome, Edge ou Firefox. Para instalação PWA e cache offline, use um servidor HTTP local (`python -m http.server 8080`) e acesse `http://localhost:8080`.

## 2. Publicação no GitHub Pages

1. Envie o conteúdo da pasta `MicaPortugues` para a raiz da branch `main` do repositório `jabesguitar/MicaPortugues`.
2. Confirme que `index.html` está na raiz, junto de `app.js`, `styles.css` e `manifest.webmanifest`.
3. Acesse **Settings → Pages**.
4. Escolha **Deploy from a branch**, branch `main` e diretório `/ (root)`.
5. Salve e aguarde o GitHub Pages exibir o endereço HTTPS.

## 3. Android

No Android, acesse o endereço HTTPS publicado pelo Chrome. Abra o menu e escolha **Instalar app** ou **Adicionar à tela inicial**. O aplicativo pode abrir em janela própria e usar o cache PWA após o primeiro carregamento.

## 4. APK nativo

O projeto incluído não é um APK. A geração de APK exigirá uma etapa adicional com Capacitor ou outro empacotador Android, Android SDK, Gradle e assinatura. Esses componentes não estavam configurados neste ambiente, portanto nenhum APK foi compilado nem assinado nesta entrega.
