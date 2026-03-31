#!/usr/bin/env python3
"""
AGGIORNA DOMANDE ALPHA TEST 2026
==================================
Usa questo script ogni volta che modifichi il file Excel delle domande.

Come usarlo:
1. Modifica ALPHA_TEST_2026.xlsx (aggiungi/modifica domande)
2. Copia il file Excel nella stessa cartella di questo script
3. Esegui: python3 aggiorna_domande.py
4. Il file data/domande.json verrà aggiornato automaticamente
5. Pubblica le modifiche su GitHub (vedi README)

Struttura Excel attesa (colonne):
  A: ID
  B: Fonte
  C: Domanda
  D: Opzione A
  E: Opzione B
  F: Opzione C
  G: Opzione D (opzionale)
  H: Risposta corretta (A / B / C / D)
  I: Mescola le risposte (SI / NO)
  J: Macrotema
"""

import json
import sys
import os

try:
    import openpyxl
except ImportError:
    print("Installo openpyxl...")
    os.system("pip install openpyxl")
    import openpyxl

# Nome del file Excel (modifica se hai un nome diverso)
EXCEL_FILE = "ALPHA_TEST_2026.xlsx"
OUTPUT_FILE = os.path.join("data", "domande.json")

def main():
    if not os.path.exists(EXCEL_FILE):
        print(f"ERRORE: File '{EXCEL_FILE}' non trovato!")
        print(f"Assicurati che il file Excel sia nella stessa cartella di questo script.")
        sys.exit(1)

    print(f"Leggo: {EXCEL_FILE} ...")
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active

    questions = []
    skipped = 0

    for row in ws.iter_rows(min_row=2, values_only=True):
        # Salta righe senza ID
        if row[0] is None:
            continue

        id_, fonte, domanda, a, b, c, d, risposta, mescola, macrotema = (
            row[0], row[1], row[2], row[3], row[4], row[5],
            row[6] if len(row) > 6 else None,
            row[7] if len(row) > 7 else None,
            row[8] if len(row) > 8 else None,
            row[9] if len(row) > 9 else None,
        )

        if not domanda or not risposta:
            skipped += 1
            continue

        opzioni = {"A": str(a) if a else "", "B": str(b) if b else "", "C": str(c) if c else ""}
        if d:
            opzioni["D"] = str(d)

        # Rimuovi opzioni vuote
        opzioni = {k: v for k, v in opzioni.items() if v.strip()}

        questions.append({
            "id": int(id_),
            "fonte": str(fonte or ""),
            "domanda": str(domanda),
            "opzioni": opzioni,
            "risposta": str(risposta).strip().upper(),
            "mescola": str(mescola or "").strip().upper() == "SI",
            "macrotema": str(macrotema or "")
        })

    # Crea cartella data se non esiste
    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Completato!")
    print(f"  Domande importate: {len(questions)}")
    if skipped:
        print(f"  Righe saltate (senza domanda/risposta): {skipped}")
    print(f"  File salvato in: {OUTPUT_FILE}")
    print(f"\nOra pubblica le modifiche su GitHub (vedi README).")

if __name__ == "__main__":
    main()
