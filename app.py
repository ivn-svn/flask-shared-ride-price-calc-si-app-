from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    def price_calc(a, b):
        price = (float(a) * float(b)) / 100
        return price
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        operation = request.form['operation']
        todiv_per_person = price_calc(num1, num2)
        if operation == 'C1998':
            sum = (todiv_per_person * 9.8) / int(num3)
            sum = str(round(sum, 2)) + ' BGN per person.'
            return render_template('app.html', sum=sum)

        elif operation == 'w124':
            sum = (todiv_per_person * 12) / int(num3)
            sum = str(round(sum, 2)) + ' BGN per person.'
            return render_template('app.html', sum=sum)

        elif operation == 'C2006':
            sum = (todiv_per_person * 7) / int(num3)
            sum = str(round(sum, 2)) + ' BGN per person.'
            return render_template('app.html', sum=sum)

        elif operation == 'VW2002':
            sum = (todiv_per_person * 8) / int(num3)
            sum = str(round(sum, 2)) + ' BGN per person.'
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
