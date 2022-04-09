from flask import Flask, render_template
app = Flask(__name__)    




headings = ("First Name", "Last Name", "Full Name")
data = (
    ("Andrew",	"Castellanos",	"Andrew Castellanos"),
    ("Sam",	"Smith",	"Sam Smith"),
    ("Jim",	"Poe",	"Jim Poe"),
)

@app.route("/")
def table():
    return render_template("table.html", headings=headings, data=data)












if __name__=="__main__":       
    app.run(debug=True)  