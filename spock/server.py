from flask import Flask, request, render_template_string
import io
import sys
from contextlib import redirect_stdout

app = Flask(__name__)

from SpockInterpreter import SpockInterpreter, process_input

interpreter = SpockInterpreter()
# Assuming you have these imported or defined elsewhere
# from your_module import process_input, interpreter

def run_command(text: str):
    # Capture stdout
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        process_input(interpreter, text)
    
    return captured_output.getvalue()

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Voice Input App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px;
                font-size: 14px;
            }
            textarea {
                width: 90%;
                height: 150px;
                margin-bottom: 10px;
                font-size: 14px;
            }
            button {
                font-size: 16px;
                padding: 8px 16px;
            }
            #result {
                width: 90%;
                word-wrap: break-word;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <textarea id="inputText" placeholder="Enter your text here..."></textarea>
        <button onclick="submitText()">Submit</button>
        <div id="result"></div>

        <script>
            function submitText() {
                const text = document.getElementById('inputText').value;
                fetch('/run', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'text=' + encodeURIComponent(text)
                })
                .then(response => response.text())
                .then(data => {
                    document.getElementById('result').innerText = data;
                });
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/run', methods=['POST'])
def run():
    text = request.form['text']
    result = run_command(text)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)