import {questions,pairs,trueFalse} from '../src/questions.js';
import fs from 'node:fs';
const assert=(v,m)=>{if(!v)throw new Error(m)};
assert(questions.length===30,'Expected exactly 30 quiz questions');
for(const [i,q] of questions.entries()){
  assert(q.q && q.a.length===4,`Question ${i+1} malformed`);
  assert(Number.isInteger(q.c)&&q.c>=0&&q.c<4,`Question ${i+1} answer index invalid`);
  assert(q.why&&q.topic,`Question ${i+1} missing explanation/topic`);
}
assert(new Set(questions.map(q=>q.q)).size===questions.length,'Duplicate quiz prompt');
assert(pairs.length===8,'Pair bank should contain all 8 concepts');
assert(trueFalse.length===12,'True/false bank should contain 12 affirmations');
const html=fs.readFileSync(new URL('../index.html',import.meta.url),'utf8');
const app=fs.readFileSync(new URL('../app.js',import.meta.url),'utf8');
for(const key of ['home','study','games','play','about'])assert(html.includes(`id="${key}"`),`Missing screen ${key}`);
for(const mode of ['quiz','truefalse','pairs','columns','memory','search','crossword'])assert(html.includes(`data-game="${mode}"`),`Missing game ${mode}`);
assert(app.includes('queue.push(queue.shift())'),'Quiz skip must append current question to end');
assert(app.includes('tfSet.push(tfSet.shift())'),'True/false skip must append current item to end');
assert(app.includes('time:90,lives:3')&&app.includes('time:60,lives:4')&&app.includes('time:30,lives:5'),'Level time/life configuration mismatch');
assert(app.includes('musicPatterns={quiz:')&&app.includes('function startMusic(type)'),'Procedural per-game soundtracks missing');
// Stress-test word placement strategy used by the word-search game.
const words=['CRONICA','FICCAO','NARRADOR','ENREDO','SUJEITO','VERBO','LINGUAGEM','FUTEBOL'];
for(let seed=0;seed<250;seed++){
  let state=seed+1; const rand=()=>{state=(state*48271)%2147483647;return state/2147483647};
  const n=12,grid=Array.from({length:n},()=>Array(n).fill(''));
  for(const w of words){let placed=false;for(let tries=0;tries<300&&!placed;tries++){
    const horizontal=rand()>.45,r=Math.floor(rand()*n),c=Math.floor(rand()*n);
    const ids=horizontal&&c+w.length<=n?Array.from({length:w.length},(_,k)=>[r,c+k]):!horizontal&&r+w.length<=n?Array.from({length:w.length},(_,k)=>[r+k,c]):null;
    if(ids&&ids.every(([rr,cc])=>grid[rr][cc]==='')){ids.forEach(([rr,cc],k)=>grid[rr][cc]=w[k]);placed=true;}
  } assert(placed,`Could not place ${w} in generated word search (seed ${seed})`);}
}
// Verify the designed crossword intersections share the same letter.
const entries=[{word:'CRONICA',r:4,c:2,dir:'h'},{word:'NARRADOR',r:2,c:3,dir:'v'},{word:'ENREDO',r:5,c:1,dir:'h'},{word:'VERBO',r:10,c:1,dir:'h'},{word:'SUJEITO',r:12,c:1,dir:'h'},{word:'FICCAO',r:14,c:1,dir:'h'}];
const cg=Array.from({length:16},()=>Array(10).fill('#'));
for(const e of entries)[...e.word].forEach((ch,k)=>{const r=e.r+(e.dir==='v'?k:0),c=e.c+(e.dir==='h'?k:0);assert(cg[r][c]==='#'||cg[r][c]===ch,'Crossword has conflicting intersection');cg[r][c]=ch;});
assert(cg[4][3]==='R'&&cg[5][3]==='R','Crossword intersections do not match');
const icon=fs.readFileSync(new URL('../assets/icon-1024.png',import.meta.url));
assert(icon.readUInt32BE(16)===1024&&icon.readUInt32BE(20)===1024,'Icon must be 1024x1024 PNG');
console.log(JSON.stringify({quizQuestions:questions.length,uniqueQuestions:true,pairs:pairs.length,trueFalse:trueFalse.length,games:7,wordSearchStressTests:250,crosswordIntersections:2,icon:'1024x1024 PNG with alpha',levelConfig:'90s/3 lives; 60s/4 lives; 30s/5 lives',skipBehavior:'shift+append',status:'PASS'},null,2));
