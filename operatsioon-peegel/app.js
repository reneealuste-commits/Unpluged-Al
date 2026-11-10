(function(){
const D=window.OPORD,KEY="peegel_v1",$=s=>document.querySelector(s),app=$("#app");
let S=JSON.parse(localStorage.getItem(KEY)||"null")||{role:null,m:{},topics:{},cards:{},filters:{},books:{},facts:{},commit:{},p:null};
const save=()=>{localStorage.setItem(KEY,JSON.stringify(S));xp();};
const M=[
 {n:1,id:"olukord",t:"Olukord",s:"Aus pilt sellest, kus me oleme"},
 {n:2,id:"ulesanne",t:"Põhiülesanne",s:"Miks me seda teeme"},
 {n:3,id:"taide",t:"Täideviimine",s:"Põhialused, kirjandus, filtrid"},
 {n:4,id:"teenindus",t:"Teenindus ja logistika",s:"Mis sul kasutada on"},
 {n:5,id:"juhtimine",t:"Juhtimine ja side",s:"Igaüks on oma üksuse juht"}];
const role=()=>D.roles.find(r=>r.id===S.role);
const topic=id=>D.topics.find(t=>t.id===id);
const cnt=o=>Object.values(o).filter(Boolean).length;
function xp(){const tot=5+D.topics.length+D.filters.length+D.books.length;
 const got=cnt(S.m)+cnt(S.topics)+cnt(S.filters)+cnt(S.books);const p=Math.round(got/tot*100);
 $("#xpfill").style.width=p+"%";$("#xptext").textContent=p+"%";}
const unlocked=n=>n===1||S.m[M[n-2].id];
function go(v,a){S.view=v;S.arg=a;localStorage.setItem(KEY,JSON.stringify(S));render();window.scrollTo(0,0);}
document.addEventListener("click",e=>{const g=e.target.closest("[data-go]");if(g)go(g.dataset.go,g.dataset.arg);});
$("#reset").onclick=()=>{if(confirm("Kustutan kogu progressi sellest seadmest?")){localStorage.removeItem(KEY);location.reload();}};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function check(group,key,label,sub){const on=!!S[group][key];
 return `<label class="check ${on?"on":""}"><input type="checkbox" data-g="${group}" data-k="${esc(key)}" ${on?"checked":""}><span><b>${esc(label)}</b>${sub?`<br><small class="muted">${esc(sub)}</small>`:""}</span></label>`;}
app.addEventListener("change",e=>{const i=e.target;if(i.dataset.g){S[i.dataset.g][i.dataset.k]=i.checked;save();render(true);}});
function finish(id){S.m[id]=true;save();const i=M.findIndex(x=>x.id===id);go(i===4?"done":"map");}
const V={
home(){const r=role();return `
 <div class="card"><div class="kicker">OPORD · paranemis-teekond</div>
 <h1>Operatsioon „Peegel“</h1>
 <p class="quote">${esc(D.mission)}</p>
 <p class="muted">Viis operatsiooniosa nagu viis missiooni: Olukord → Põhiülesanne → Täideviimine → Teenindus → Juhtimine. Progress jääb sinu seadmesse.</p></div>
 ${r?`<button class="btn" data-go="map">Jätka teekonda (${esc(r.name)})</button>`:""}
 <h2 style="margin-top:22px">${r?"Vaheta rolli":"Vali oma lähtepunkt"}</h2>
 <p class="muted">Kus sa praegu oled? Roll määrab, millest sinu esimene samm algab.</p>
 <div class="grid">${D.roles.map(x=>`<button class="opt ${S.role===x.id?"sel":""}" data-role="${x.id}"><span class="ico">${x.ico}</span><b>${x.name}</b><small>${x.sub}</small></button>`).join("")}</div>`;},
brief(){const r=role(),t=topic(r.first);return `
 <div class="card"><div class="kicker">Käsk vastu võetud · ${esc(r.name)}</div>
 <h1>Sinu esimene samm: ${t.ico} ${t.name}</h1><p>${esc(t.text)}</p>
 ${t.card?`<h3>Taskukaart</h3><p>${esc(t.cardTitle)}</p>`:""}
 <p class="muted">Iga inimene saab konkreetseid samme, mida teha juba täna.</p></div>
 <button class="btn" data-go="topic" data-arg="${t.id}">Ava taskukaart ja tee see täna</button>
 <button class="btn ghost" data-go="map">Vaata kogu operatsiooni kaarti</button>`;},
map(){const r=role();return `
 <div class="kicker">Operatsiooni kaart${r?" · "+esc(r.ico+" "+r.name):""}</div><h1>Viis missiooni</h1>
 ${M.map(m=>{const d=S.m[m.id],u=unlocked(m.n);const cur=u&&!d;
 return `<div class="card mission ${d?"done":cur?"cur":"lock"}" ${u?`data-go="${m.id}" role="button" tabindex="0" style="cursor:pointer"`:""}>
 <div class="badge">${d?"✓":u?m.n:"🔒"}</div><div><b>${m.n}. ${m.t}</b><br><small class="muted">${m.s}</small></div></div>`;}).join("")}
 ${r?`<button class="btn ghost" data-go="topic" data-arg="${r.first}">⚡ Minu esimene samm: ${esc(topic(r.first).name)}</button>`:""}`;},
olukord(){const all=D.situation.every((_,i)=>S.facts[i]);return `
 <div class="kicker">Missioon 1</div><h1>Olukord</h1><p class="muted">Hetke-analüüs: mitte süüdistused, vaid tulemused. Puuduta iga kaarti, kui oled selle läbi lugenud.</p>
 ${D.situation.map((f,i)=>check("facts",i,f[0],f[1])).join("")}
 <div class="card"><h3>Kontekst</h3><p>${esc(D.context)}</p><p class="quote">Tulemused räägivad, mitte kavatsused. See ei ole kellegi süüdistamine — see on aus pilt sellest, kus me oleme.</p></div>
 <p class="muted">Ära usu neid numbreid pimesi — kontrolli ise.</p>
 <button class="btn" id="fin" data-id="olukord" ${all?"":"disabled"}>Olukord selge ✓</button>`;},
ulesanne(){const all=D.missionPoints.every((_,i)=>S.commit[i]);return `
 <div class="kicker">Missioon 2</div><h1>Põhiülesanne</h1>
 <div class="card"><p class="quote" style="font-size:1.15rem">${esc(D.mission)}</p></div>
 <p>See tähendab — kinnita iga punkt:</p>
 ${D.missionPoints.map((p,i)=>check("commit",i,p)).join("")}
 <button class="btn" id="fin" data-id="ulesanne" ${all?"":"disabled"}>Võtan ülesande vastu ✓</button>`;},
taide(){const r=role(),n=cnt(S.topics),f=cnt(S.filters);const ok=n>=1&&f>=D.filters.length;return `
 <div class="kicker">Missioon 3</div><h1>Täideviimine</h1>
 <h3>3.1 Teadlikkus (põhialused) · ${n}/${D.topics.length}</h3>
 <div class="grid">${D.topics.map(t=>`<button class="opt ${S.topics[t.id]?"sel":""}" data-go="topic" data-arg="${t.id}"><span class="ico">${t.ico}</span><b>${t.name}${S.topics[t.id]?" ✓":""}${r&&r.first===t.id?" ⚡":""}</b><small>${esc(t.text.split(".")[0])}</small></button>`).join("")}</div>
 <h3>3.3 Filtrid (kuidas mõelda) · ${f}/${D.filters.length}</h3>
 ${D.filters.map(x=>check("filters",x.who,x.who+" — "+x.what,x.q)).join("")}
 <h3>3.2 Kohustuslik kirjandus · ${cnt(S.books)}/${D.books.length}</h3><p class="muted">Märgi loetuks, kui oled raamatu läbi töötanud.</p>
 ${D.books.map(b=>check("books",b[0],b[0],b[1])).join("")}
 <p class="muted">${ok?"":"Missiooni lõpetamiseks: vähemalt üks põhialus tehtud ja kõik kolm filtrit läbi mõeldud."}</p>
 <button class="btn" id="fin" data-id="taide" ${ok?"":"disabled"}>Täideviimine käivitatud ✓</button>`;},
topic(id){const t=topic(id)||D.topics[0];const done=!!S.topics[t.id];return `
 <button class="link" data-go="taide">← Täideviimine</button>
 <div class="card"><div class="kicker">Põhialus</div><h1>${t.ico} ${t.name}</h1><p>${esc(t.text)}</p></div>
 ${t.card?`<div class="card"><h3>📇 Taskukaart</h3><p class="muted">Lihtne, prinditav kaart. Pane täna paika:</p>${t.card.map(c=>check("cards",t.id+":"+c,c)).join("")}</div>`
 :`<div class="card"><h3>📇 Taskukaart</h3><p>Sa ei saa juhtida teisi, kui ei suuda juhtida ennast. Alusta iseendast — mis on täna sinu vastutus?</p><p class="muted">(Juhtimise taskukaarti OPORD-is eraldi ei ole.)</p></div>`}
 <button class="btn" data-done="${t.id}">${done?"✓ Tehtud — tühista":"Tegin selle täna ✓"}</button>
 <button class="btn ghost" data-go="taide">Järgmine põhialus</button>`;},
teenindus(){return `
 <div class="kicker">Missioon 4</div><h1>Teenindus ja logistika</h1>
 ${D.logistics.map(l=>`<div class="card"><h3>${l[0]}</h3><p>${esc(l[1])}</p></div>`).join("")}
 <p class="muted">Kontrolli allikaid ise. Ära usu mind.</p>
 <button class="btn" id="fin" data-id="teenindus">Varustus olemas ✓</button>`;},
juhtimine(){const p=S.p;const fb={a:["bad","Karjumine vastu toidab drama't. Lisa P: inimene, kes karjub, ei vaja vastust."],b:["","Õige. Ta vajab vaikust ja turvalisust. See ei tähenda nõustumist, vaid piiri hoidmist."],c:["bad","See ei tähenda nõustumist. Hoia piiri."]};return `
 <div class="kicker">Missioon 5</div><h1>Juhtimine ja side</h1>
 ${D.command.map(l=>`<div class="card"><h3>${l[0]}</h3><p>${esc(l[1])}</p></div>`).join("")}
 <div class="card"><div class="kicker">Lisa P · Trauma-teadlikkus</div><h2>„Haukuv koer“</h2>
 <p><b>Olukord:</b> keegi karjub sinu peale. Mida teed?</p>
 ${[["a","Karjun vastu ja selgitan, miks ta eksib"],["b","Jään vaikseks, loon turvalisuse ja hoian oma piiri"],["c","Nõustun kõigega, et ta rahuneks"]].map(o=>`<button class="opt ${p===o[0]?"sel":""}" style="margin:8px 0" data-pick="${o[0]}">${o[1]}</button>`).join("")}
 ${p?`<div class="fb ${fb[p][0]}">${fb[p][1]}</div>`:""}
 <p class="quote" style="margin-top:12px">${esc(D.annexP)}</p></div>
 <button class="btn" id="fin" data-id="juhtimine" ${p==="b"?"":"disabled"}>Võtan juhtimise üle ✓</button>`;},
done(){return `<div class="card" style="text-align:center"><div class="stamp">OPERATSIOON KÄIVITATUD</div>
 <h1 style="margin-top:18px">Sa oled oma üksuse juht.</h1><p>Kõik viis missiooni on läbitud. Nüüd algab igapäevane töö: põhialused, taskukaardid, kirjandus.</p>
 <p class="quote">Ära usu mind. Kaitse oma uskumusi. Tee uuringud.</p><p class="muted">See on kutse, mitte käsk. Iga samm on sinu oma.</p></div>
 <button class="btn" data-go="taide">Jätka põhialustega</button>
 <button class="btn ghost" id="share">Jaga teekonda</button>`;}
};
app.addEventListener("click",e=>{const t=e.target.closest("button");if(!t)return;
 if(t.dataset.role){S.role=t.dataset.role;save();go("brief");}
 else if(t.id==="fin")finish(t.dataset.id);
 else if(t.dataset.done){S.topics[t.dataset.done]=!S.topics[t.dataset.done];save();render(true);}
 else if(t.dataset.pick){S.p=t.dataset.pick;save();render(true);}
 else if(t.id==="share"){const d={title:"Operatsioon „Peegel“",text:"Ära usu mind. Kaitse oma uskumusi. Tee uuringud.",url:location.href.split("#")[0]};
  if(navigator.share)navigator.share(d).catch(()=>{});else{navigator.clipboard&&navigator.clipboard.writeText(d.url);t.textContent="Link kopeeritud ✓";}}});
app.addEventListener("keydown",e=>{if(e.key==="Enter"&&e.target.dataset.go)e.target.click();});
function render(keep){let v=S.view||"home";if(!S.role&&v!=="home")v="home";
 const m=M.find(x=>x.id===v);if(m&&!unlocked(m.n))v="map";
 const y=window.scrollY;app.innerHTML=V[v](S.arg);if(keep)window.scrollTo(0,y);}
xp();render();
})();
