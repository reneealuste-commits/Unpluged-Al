// Sisu: Google Doc „OPERATSIOON PEEGEL — OPORD (paranemis-teekond)“. Tekst on võetud dokumendist.
window.OPORD = {
 roles: [ // OLETUS: dokument rolle ei defineeri ("Igaüks on oma üksuse juht"); rollid määravad ainult esimese sammu.
  {id:"algaja",ico:"🌱",name:"Algaja",sub:"Alustan nullist",first:"uni"},
  {id:"vanem",ico:"👪",name:"Vanem",sub:"Mul on lapsed",first:"lapsed"},
  {id:"juht",ico:"🧭",name:"Juht",sub:"Juhin inimesi",first:"juhtimine"},
  {id:"sodur",ico:"🛡️",name:"Sõdur",sub:"Kaitseliit / teenistus",first:"keha"},
  {id:"partner",ico:"🤝",name:"Partner",sub:"Tahan paremat suhet",first:"intiimsus"},
  {id:"kodanik",ico:"🇪🇪",name:"Kodanik",sub:"Tahan aru saada",first:"uni"}
 ],
 situation:[
  ["Sündimuskordaja","1,16 — alla asendusmäära (2,1). Iga põlvkond on väiksem kui eelmine."],
  ["Üksikvanemate vaesus","Eestis on üksikvanemaga pered oluliselt suuremas vaesusriskis kui kahevanemaga pered."],
  ["Valitsuse usaldus","Madal. Inimesed ei usu institutsioonidesse, aga ei tea ka, mida ise teha."],
  ["Eluasemehinnad","Noored ei saa endale kodu lubada. See mõjutab nii sündimust kui ka võimalust juurduda."],
  ["Kaitsekulutused vs perede KPI-d","Riik investeerib kaitsesse, aga perede heaolusse investeeringud ei vasta vajadusele."]
 ],
 context:"Eesti rahvas seisab ristteel. Külm sõda lõppes, aga uued väljakutsed on tulnud: demograafiline langus, vaimne tervis, ühiskondlik killustumine. Lahendus ei tule ülevalt — see tuleb igast kodanikust, kes otsustab oma elu ja oma perega teadlikult töötada.",
 mission:"Taastada Eesti rahva inimlikkus läbi iga kodaniku isikliku paranemis-teekonna.",
 missionPoints:["Iga inimene leiab oma raja, kus ta praegu on.","Iga inimene saab konkreetseid samme, mida teha juba täna.","Iga inimene mõistab, et muutused algavad temast endast, mitte süsteemist."],
 topics:[
  {id:"uni",ico:"🌙",name:"Uni",text:"Matthew Walker, Why We Sleep. Ilma magamata ei toimi miski muu.",card:["Kellaaeg","Keskkond","Rituaal"],cardTitle:"Uni: kellaaeg, keskkond, rituaal."},
  {id:"toit",ico:"🥕",name:"Toit",text:"Lihtne, ehtne, lähedalt. Vähem töödeldud, rohkem ise tehtud.",card:["Nädala menüü","Ostunimekiri","Valmistamine"],cardTitle:"Toit: nädala menüü, ostunimekiri, valmistamine."},
  {id:"keha",ico:"💪",name:"Keha",text:"Liikumine iga päev, isegi 20 minutit. Keha on vaimu alus.",card:["Harjutuste järjekord","Kestus","Sagedus"],cardTitle:"Keha: harjutuste järjekord, kestus, sagedus."},
  {id:"intiimsus",ico:"❤️",name:"Intiimsus",text:"Intiimsuse atlas. Suhted vajavad sama tähelepanu nagu töö.",card:["Igapäevane 10 minutit täielikku tähelepanu"],cardTitle:"Suhted: igapäevane 10 minutit täielikku tähelepanu."},
  {id:"lapsed",ico:"🧒",name:"Lapsed",text:"Montessori lähenemine. Laps ei ole projekt, vaid isiksus.",card:["Vaatlus, mitte juhtimine"],cardTitle:"Lapsed: vaatlus, mitte juhtimine."},
  {id:"juhtimine",ico:"🎖️",name:"Juhtimine",text:"Extreme Ownership (Jocko Willink). Sa ei saa juhtida teisi, kui ei suuda juhtida ennast.",card:null,cardTitle:null}
 ],
 books:[["Keha peab arvet","Bessel van der Kolk (trauma-teadlikkus)"],["Intiimsuse atlas","Eesti suhete klassika"],["Why We Sleep","Matthew Walker"],["Extreme Ownership","Jocko Willink"],["Inimesekeskne juhtimine","Rudolf Staiger"],["Top Shelf Man","R.C."],["12 reeglit eluks","Jordan Peterson"],["Nonviolent Communication","Marshall Rosenberg"],["How to Make Friends and Influence People","Dale Carnegie"]],
 filters:[
  {who:"Beverly Engel",what:"Vaimne ja emotsionaalne vägivald",q:"Kas see, mida ma kuulen või loen, on hooldav või kahjustav?"},
  {who:"Chance Hughes",what:"Ajupesu tehnikad",q:"Kuidas mind püütakse mõjutada?"},
  {who:"Chris Voss",what:"Läbirääkimiste petukaart",q:"Kuidas ma suhtlen keerulistes olukordades?"}
 ],
 logistics:[["Materjalid","OPORD täistekst, PDF-id, taskukaardid, lendlehed, toitumise uurimustöö."],["Platvormid","Google Drive, GitHub (repo Unpluged-Al), earnthetab.com."],["Tugi","Kaitseliit, Ranger School kogemus, kogukond."]],
 command:[["Ülesande koosseis","Kodanikud. Igaüks on oma üksuse juht."],["Viited","Remo Ojaste (Combat Ready), Aarne Ermus, Rene Toomse, Riho Ühtegi."],["Side","OPORD dokument, GitHub, avalikud postitused."]],
 annexP:"Ära toida drama't. Inimene, kes karjub, ei vaja vastust — ta vajab vaikust ja turvalisust. See ei tähenda nõustumist, vaid piiri hoidmist."
};
