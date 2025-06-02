from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv
import shutil
import webbrowser
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    lang = request.args.get('lang', 'es')
    return render_template('index.html', lang=lang)

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    pump = request.form['pump']
    amount = float(request.form['amount'])
    price_per_liter = float(request.form['price_per_liter'])
    attendant = request.form['attendant']
    factura_type = request.form['factura_type']
    lang = request.form.get('lang', 'es')

    now = datetime.now()
    liters = round(amount / price_per_liter, 2)
    total_amount = round(liters * price_per_liter, 2)

    with open('sale_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            now.strftime('%Y-%m-%d'),
            now.strftime('%H:%M:%S'),
            pump,
            liters,
            price_per_liter,
            total_amount,
            attendant
        ])

    if factura_type == 'fiscal':
        return redirect(f"/receipt?pump={pump}&liters={liters}&price_per_liter={price_per_liter}&total={total_amount}&attendant={attendant}&lang={lang}")
    else:
        return render_template('factura.html',
                               pump=pump,
                               liters=liters,
                               price_per_liter=price_per_liter,
                               total=total_amount,
                               date=now.strftime('%Y-%m-%d'),
                               time=now.strftime('%H:%M:%S'),
                               attendant=attendant,
                               lang=lang)

@app.route('/receipt')
def receipt():
    pump = request.args.get('pump')
    liters = request.args.get('liters')
    price_per_liter = request.args.get('price_per_liter')
    total = request.args.get('total')
    attendant = request.args.get('attendant')
    lang = request.args.get('lang', 'es')

    return render_template('receipt.html',
                           pump=pump,
                           liters=liters,
                           price_per_liter=price_per_liter,
                           total=total,
                           date=datetime.now().strftime('%Y-%m-%d'),
                           time=datetime.now().strftime('%H:%M:%S'),
                           attendant=attendant,
                           lang=lang)

@app.route('/sales_history')
def sales_history():
    rows = []
    total_sales = 0
    with open('sale_log.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
            total_sales += float(row[5])
    return render_template('sales_history.html', sales=rows, total_sales=total_sales)

@app.route('/reset')
def reset_sales():
    open('sale_log.csv', 'w').close()
    return redirect('/')

@app.route('/restore')
def restore_sales():
    shutil.copy('sale_log_backup.csv', 'sale_log.csv')
    return redirect('/')

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)


