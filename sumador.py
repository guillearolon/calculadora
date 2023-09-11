from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def suma():
    resultado = None

    if request.method == 'POST':
        if 'sumador1' in request.form and 'sumador2' in request.form:
            num1 = int(request.form.get('sumador1'))
            num2 = int(request.form.get('sumador2'))
            resultado = num1 + num2

    return render_template('sumador.html', resultado=resultado)

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    resultado_resta = None

    if request.method == 'POST':
        if 'resta1' in request.form and 'resta2' in request.form:
            num1 = int(request.form.get('resta1'))
            num2 = int(request.form.get('resta2'))
            resultado_resta = num1 - num2

    return render_template('sumador.html', resultado_resta=resultado_resta)

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    resultado_multiplicar = None

    if request.method == 'POST':
        if 'multi1' in request.form and 'multi2' in request.form:
            num1 = int(request.form.get('multi1'))
            num2 = int(request.form.get('multi2'))
            resultado_multiplicar = num1 * num2


    return render_template('sumador.html', resultado_multiplicar=resultado_multiplicar)  

@app.route('/dividir', methods=['GET', 'POST'])
def division():
    resultado_division = None
    mensaje_error = None

    if request.method == 'POST':
        if 'div1' in request.form and 'div2' in request.form:
            divi1 = int(request.form.get('div1'))
            divi2 = int(request.form.get('div2'))

            if divi2 != 0:
                resultado_division = divi1 / divi2
            else:
                mensaje_error = "Division por cero no permitida"
                resultado_division = None

    return render_template('sumador.html', resultado_division=resultado_division, mensaje_error=mensaje_error)            

if __name__ == '__main__':
    app.run('localhost', debug=True, port=8000)
