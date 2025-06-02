# ⛽ GasStation_App (2025)

A fully functional desktop app for managing a small gas station. This application helps track fuel sales, generate receipts (in both English and Spanish), and back up transaction data — all from a simple local interface.

---

## 🚀 Features

- 🔘 **Two-pump system** with volume and price entry
- 🧾 **Receipt generation** in English or Spanish
- 🧮 **Automatic total calculation** based on liters/gallons sold
- 🗃️ **Sales log saved to CSV** (`sale_log.csv`)
- 🛡️ **Backup file auto-generated** (`sale_log_backup.csv`)
- 🧾 **Printable views** for:
  - Simple receipts
  - Fiscal receipts (`factura fiscal`)
  - Sales history

---

## 🛠️ Tech Stack

- Python 3
- Flask (for local web interface)
- HTML/CSS (templates)
- CSV file handling

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `app.py` | Main application logic |
| `templates/index.html` | Home form to enter sale data |
| `templates/receipt.html` | Printable receipt |
| `templates/factura.html` | Spanish factura |
| `templates/factura_fiscal.html` | Tax-compliant receipt |
| `templates/sales_history.html` | View total past sales |
| `sale_log.csv` | CSV log of all sales |
| `sale_log_backup.csv` | Auto-backup copy of the sales log |
| `app.spec` | Spec file used for EXE generation (with `auto-py-to-exe`) |

---

## 📸 Screenshots

📌 *(Screenshots can be added later for the user interface)*

---

## 💡 How to Run

1. Install dependencies (Flask):

```bash
pip install flask
python app.py
http://127.0.0.1:5000/
auto-py-to-exe
📬 Contact
Built by Ronald Gustavo Pineda
📧 ronald.pneda8@gmail.com
🌍 GitHub Profile


