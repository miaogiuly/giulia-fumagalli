# Giulia Fumagalli — Sito Personale
## Guida operativa completa

---

## STRUTTURA DEL SITO

```
sito/
├── index.html          ← Home page pubblica
├── login.html          ← Accesso aziendale
├── dashboard.html      ← Dashboard (dopo login)
├── test.html           ← Alpha Test 2026
├── aggiorna_domande.py ← Script per aggiornare domande da Excel
├── assets/
│   ├── foto.png        ← Tua foto profilo
│   └── logo_3a.png     ← Logo Scuola 3A
└── data/
    └── domande.json    ← Domande del test (generate dall'Excel)
```

---

## METTERE IL SITO ONLINE (GitHub Pages)

### Prima volta (10 minuti)

1. Vai su **github.com** e accedi al tuo account
2. Clicca sul **+** in alto a destra → "New repository"
3. Nome: `giulia-fumagalli` (o quello che preferisci)
4. Spunta "Public"
5. Clicca "Create repository"
6. Clicca "uploading an existing file"
7. Trascina tutti i file della cartella `sito/` (incluse le sottocartelle `assets/` e `data/`)
8. Scrivi "Prima versione" nel campo "Commit changes"
9. Clicca "Commit changes"
10. Vai su **Settings** → **Pages**
11. Under "Source" scegli: "Deploy from a branch" → `main` → `/ (root)`
12. Clicca "Save"
13. Dopo 2 minuti il sito è online all'indirizzo:
    `https://TUO-USERNAME.github.io/giulia-fumagalli/`

---

## CREDENZIALI DI ACCESSO AZIENDALE

Le credenziali sono nel file `login.html`, modifica questa parte:

```javascript
const CREDENZIALI = {
  "3a": [
    { id: "3A2026", password: "sicurezza2026" }
  ]
};
```

- Puoi cambiare ID e password come vuoi
- Per aggiungere più utenti aggiungi righe:
  `{ id: "NUOVO_ID", password: "nuova_password" }`

---

## AGGIORNARE LE DOMANDE

Quando vuoi aggiungere/modificare domande nel test:

1. Apri `ALPHA_TEST_2026.xlsx` e fai le modifiche
2. Salva il file Excel nella stessa cartella del sito
3. Apri il Terminale / Prompt dei comandi in quella cartella
4. Digita: `python3 aggiorna_domande.py`
5. Premi Invio
6. Il file `data/domande.json` verrà aggiornato
7. Carica il nuovo `data/domande.json` su GitHub (vedi sotto)

### Come caricare modifiche su GitHub
1. Vai sul tuo repository GitHub
2. Clicca sulla cartella `data/`
3. Clicca su `domande.json`
4. Clicca sull'icona matita ✏️ (Edit)
5. Oppure più semplice: trascina il file nuovo direttamente nel repository

---

## STRUTTURA EXCEL (per aggiungere domande)

| Colonna | Contenuto | Esempio |
|---------|-----------|---------|
| A | ID numerico | 72 |
| B | Fonte | Modulo 1 |
| C | Domanda | Cosa si intende per... |
| D | Opzione A | Risposta A |
| E | Opzione B | Risposta B |
| F | Opzione C | Risposta C |
| G | Opzione D (opz.) | Risposta D |
| H | Risposta corretta | A oppure B oppure C oppure D |
| I | Mescola risposte | SI oppure NO |
| J | Macrotema | Risk Management |

**Macrotemi disponibili:**
- Risk Management
- Security aziendale
- Normativa
- Crisis & emergenze
- Geopolitica
- Sicurezza informazioni

---

## AGGIUNGERE UN'ALTRA AZIENDA

1. Apri `index.html` → aggiungi card nella sezione `.aziende-grid`
2. Apri `login.html` → aggiungi credenziali nell'oggetto `CREDENZIALI`
3. Cambia il parametro `?azienda=` nell'URL del link

---

## CAMBIARE LA FOTO O IL LOGO

- Sostituisci il file `assets/foto.png` con la nuova foto (stesso nome)
- Sostituisci `assets/logo_3a.png` con il nuovo logo (stesso nome)
- Carica i nuovi file su GitHub

---

*Sito costruito con HTML/CSS/JS puro — nessuna dipendenza, funziona ovunque.*
