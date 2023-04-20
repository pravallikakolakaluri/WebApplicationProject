from flask import Flask ,render_template,jsonify

app = Flask(__name__)
# print(app)
JB =[
  {
        'id' : 101,
        'company name': 'Tech Mahindra',
        'Title' : 'Data Analyst',
        'Location' : 'Bengaluru,India',
        'Salary' : 'Rs.800000'
    },
    {
        'id' : 102,
        'company name': 'Tcs',
        'Title' : 'Backend Engineer',
        'Location' : 'Bengaluru,India',
        'Salary' : 'Rs.500000'
    },
    {
        'id' : 103,
        'company name': 'infosys',
        'Title' : 'Full Stall Deveploer',
        'Location' : 'Bengaluru,India',
        'Salary' : 'Rs.600000'
    },
    {
        'id' : 101,
        'company name': 'capgimin',
        'Title' : 'SDET',
        'Location' : 'Bengaluru,India',
        'Salary' : 'Rs.400000'
    },
  ]

@app.route("/")
def hi():
    return render_template('home.html',job=JB)
  
@app.route("/api/jobs")
def list_of_jobs():
    return jsonify(JB)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
