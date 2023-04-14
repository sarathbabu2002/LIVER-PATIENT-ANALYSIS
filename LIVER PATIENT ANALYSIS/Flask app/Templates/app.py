import pandas as pd

from flask import Flask, request, render_template
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user input and preprocess it
        data = request.form.to_dict()
        data.pop('submit')
        # Make prediction
        prediction = model.predict(data)
        # Render the HTML template with the prediction result
        return render_template('predict.html', prediction=prediction)
    else:
        # Render the prediction form
        return render_template('form.html')

# Define a route for the form
@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

# Run the app
if __name__ == '__main__':
    app.run()