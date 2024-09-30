# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def greeting():
#     return render_template('greeting.html')

# @app.route('/cards')
# def cards():
#     return render_template('cards.html')

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     call_time = request.form['call_time']  # Get the call time from the form
#     dish = request.form['dish']            # Get the favorite dish from the form
#     return render_template('thank_you.html', call_time=call_time, dish=dish)


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('greeting.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    call_time = request.form['call_time']  # Get the call time from the form
    
    dish = request.form['dish']              # Get the favorite dish from the form
    print(call_time)
    print(dish)
    # Append the data to a text file
    with open('submissions.txt', 'a') as f:
        f.write(f'Call Time: {call_time}, Favorite Dish: {dish}\n')

    return render_template('thank_you.html', call_time=call_time, dish=dish)

if __name__ == "__main__":
    app.run(debug=True)
