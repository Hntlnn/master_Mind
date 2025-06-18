# 🧪 Testrapport – Mastermind

**Auteur:** Hirad  
**Datum:** 18 juni 2025  
**Bestand getest:** `master_Mind.py`  
**Testscript:** `test_mastermind.py`  
**Testtool:** `unittest` (Python 3)

---

## ✅ Uitgevoerde testen

| Testnaam             | Beschrijving                                                   | Resultaat |
|----------------------|----------------------------------------------------------------|-----------|
| `test_perfect_guess` | Volledige juiste gok (4 zwart)                                 | Geslaagd ✅ |
| `test_partial_guess` | Vier juiste cijfers, verkeerde volgorde (4 wit)                | Geslaagd ✅ |
| `test_mixed_feedback`| Mix van juiste en verkeerde cijfers (bijv. 1 zwart, 2 wit)     | Geslaagd ✅ |
| `test_no_match`      | Volledig foutieve gok (0 zwart, 0 wit)                         | Geslaagd ✅ |

---

## 📝 Conclusie

Alle tests zijn succesvol uitgevoerd en geslaagd.  
De functie `get_feedback()` werkt correct onder meerdere scenario’s.  
Het script geeft geen fouten of onverwacht gedrag.

**Status:** ✔️ Geslaagd en functioneel  
