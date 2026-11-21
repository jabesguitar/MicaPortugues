from pathlib import Path
import re
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
css=(root/'styles.css').read_text().splitlines()
css='\n'.join(line for line in css if not line.startswith('@import '))
html=re.sub(r'<link rel="manifest"[^>]*>','',html)
html=re.sub(r'<link rel="icon"[^>]*>','',html)
html=re.sub(r'<link rel="stylesheet"[^>]*>','<style>'+css+'</style>',html)
html=re.sub(r'<script type="module" src="app.js"></script>','',html)
questions=(root/'src/questions.js').read_text().replace('export const ','const ')
app=(root/'app.js').read_text().replace("import {questions,pairs,trueFalse} from './src/questions.js';",'')
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage','--disable-features=AudioServiceOutOfProcess'])
    page=browser.new_page(viewport={'width':1365,'height':950}); page.set_default_timeout(4000)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content(html,wait_until='domcontentloaded',timeout=10000)
    page.add_script_tag(content=questions+'\n'+app)
    assert page.title().startswith('Mica Português')
    assert page.locator('#home').is_visible()
    page.wait_for_timeout(500); page.screenshot(path=str(root/'test-results/launcher-desktop.png'),full_page=True)
    print("stage study",flush=True)
    page.locator('[data-screen="study"]').first.click()
    assert page.locator('#article h3').inner_text()=='Panorama da unidade'
    for tab in ['fiction','language','reading','agreement','special','writing']:
        page.locator(f'[data-article="{tab}"]').click()
        assert page.locator('#article h3').count()==1
    print("stage games",flush=True)
    page.locator('[data-screen="games"]').first.click()
    assert page.locator('.game-card').count()==7
    # Verify each difficulty's timer and initial life count.
    for lvl,tim,lives in [('easy','1:30',3),('normal','1:00',4)]:
        page.locator(f'[data-level="{lvl}"]').click();page.locator('[data-game="quiz"]').click()
        assert page.locator('#timerText').inner_text()==tim
        assert page.locator('.lives').first.inner_text().count('♥')==lives
        page.locator('#exitGame').click();page.locator('[data-screen="games"]').first.click()
    page.locator('[data-level="hard"]').click()
    print("stage quiz",flush=True)
    page.locator('[data-game="quiz"]').click()
    assert page.locator('.answer').count()==4
    assert page.locator('#timerText').inner_text()=='0:30'
    assert page.locator('.lives').first.inner_text().count('♥')==5
    first_q=page.locator('.quiz-question').inner_text()
    skipped=page.evaluate('queue[0].q')
    page.locator('#skipBtn').click()
    assert page.locator('.quiz-question').inner_text()!=first_q
    assert page.evaluate('queue[queue.length-1].q')==skipped
    correct=page.evaluate('queue[0].c')
    page.locator(f'[data-answer="{correct}"]').click()
    page.wait_for_timeout(1450)
    assert page.locator('.quiz-meta').first.inner_text().startswith('Pergunta 2 / 30')
    wrong=(page.evaluate('queue[0].c')+1)%4; page.locator(f'[data-answer="{wrong}"]').click(); page.wait_for_timeout(1450)
    assert page.locator('.lives').first.inner_text().count('♥')==4
    page.locator('#hintBtn').click(); assert 'Dica' in page.locator('#feedback').inner_text()
    page.locator('#soundToggle').click(); assert page.locator('#soundToggle').inner_text()=='♩'; page.locator('#soundToggle').click()
    page.locator('#playVolume').fill('22'); assert page.locator('#volume').input_value()=='22'
    page.wait_for_timeout(400); page.screenshot(path=str(root/'test-results/quiz-desktop.png'),full_page=True)
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click()
    print("stage tf",flush=True)
    page.locator('[data-game="truefalse"]').click()
    assert page.locator('[data-tf]').count()==2
    tf_first=page.evaluate('tfSet[0][0]')
    page.locator('#skipBtn').click()
    assert page.evaluate('tfSet[tfSet.length-1][0]')==tf_first
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click(); page.locator('[data-level="easy"]').click()
    print("stage pairs",flush=True)
    page.locator('[data-game="pairs"]').click()
    assert page.locator('[data-tile]').count()==16
    pair_id=page.locator('[data-side="0"]').first.get_attribute('data-id')
    page.locator(f'[data-side="0"][data-id="{pair_id}"]').click()
    page.locator(f'[data-side="1"][data-id="{pair_id}"]').click()
    assert page.locator('#pairCount').inner_text()=='1 / 8'
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click()
    print("stage columns",flush=True)
    page.locator('[data-game="columns"]').click()
    cid=page.locator('[data-col="l"]').first.get_attribute('data-id')
    page.locator(f'[data-col="l"][data-id="{cid}"]').click()
    page.locator(f'[data-col="r"][data-id="{cid}"]').click()
    assert page.locator('#colCount').inner_text()=='1 / 8'
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click()
    print("stage memory",flush=True)
    page.locator('[data-game="memory"]').click()
    pair=page.evaluate('memoryDeck.slice(0).reduce((m,x,i,a)=>{if(m.i===undefined&&a.some((y,j)=>j!==i&&y.id===x.id))m.i=i;return m},{})')
    i=pair['i']; other=page.evaluate(f'memoryDeck.findIndex((x,j)=>j!=={i}&&x.id===memoryDeck[{i}].id)')
    page.locator(f'[data-mem="{i}"]').click();page.locator(f'[data-mem="{other}"]').click()
    assert page.locator('#memCount').inner_text()=='1 / 8'
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click()
    print("stage search",flush=True)
    page.locator('[data-game="search"]').click()
    assert page.locator('[data-cell]').count()==144
    # Word search: solve all eight words by scanning the generated matrix in 4 directions.
    grid=page.evaluate('searchGrid'); words=page.evaluate('words'); n=len(grid); found={}
    for w in words:
        done=False
        for r in range(n):
            for c in range(n):
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    coords=[(r+dr*k,c+dc*k) for k in range(len(w))]
                    if all(0<=rr<n and 0<=cc<n for rr,cc in coords) and ''.join(grid[rr][cc] for rr,cc in coords)==w:
                        found[w]=[rr*n+cc for rr,cc in coords];done=True;break
                if done:break
            if done:break
        assert done, f'Could not find generated word {w}'
    for w in words:
        for cell in found[w]: page.locator(f'[data-cell="{cell}"]').click()
    assert page.locator('.game-result h3').inner_text()=='Você chegou ao final!'
    page.locator('#exitGame').click(); page.locator('[data-screen="games"]').first.click()
    print("stage crossword",flush=True)
    page.locator('[data-game="crossword"]').click()
    entries=[('CRONICA',4,2,'h'),('NARRADOR',2,3,'v'),('ENREDO',5,1,'h'),('VERBO',10,1,'h'),('SUJEITO',12,1,'h'),('FICCAO',14,1,'h')]
    for word,r,c,d in entries:
        for k,ch in enumerate(word):
            rr=r+(k if d=='v' else 0);cc=c+(k if d=='h' else 0)
            el=page.locator(f'[data-r="{rr}"][data-c="{cc}"]')
            if not el.is_disabled(): el.fill(ch)
        if entries.index((word,r,c,d))<len(entries)-1: assert page.locator('#crossCount').inner_text()==f'{entries.index((word,r,c,d))+1} / 6'
        else: assert page.locator('.game-result h3').inner_text()=='Você chegou ao final!'
    assert page.locator('.game-result h3').inner_text()=='Você chegou ao final!'
    assert errors==[],f'JavaScript errors: {errors}'
    # Mobile viewport layout spot-check.
    mobile=browser.new_page(viewport={'width':390,'height':844})
    mobile.set_content(html,wait_until='domcontentloaded')
    mobile.add_script_tag(content=questions+'\n'+app)
    mobile.wait_for_timeout(500); mobile.screenshot(path=str(root/'test-results/launcher-mobile.png'),full_page=True)
    assert mobile.locator('#home').is_visible()
    print('BROWSER INTERACTION TEST: PASS',flush=True)
    print('Home + all study tabs + 7 modes + all 3 difficulty configurations + lives + quiz skip + true/false skip + hints + audio controls + pair/column/memory/search/crossword completion.')
    print('Desktop errors:',errors)
    browser.close()
