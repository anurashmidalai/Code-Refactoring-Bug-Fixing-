from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

# Updated to handle both GET and POST methods
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Changed from request.args.get to request.form.get, as it's a POST request
        note = request.form.get("note")
        if note:  # Added check for empty note
            notes.append(note)
        # Added redirect to prevent form resubmission on page refresh
        return redirect(url_for('index'))  
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)