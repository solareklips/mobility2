from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                          jobs=jobs,
                          company_name="SolarEklips")

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# NÅET TIL 2:39:41 - SKAL TIL AT CONNECTE
# https://youtu.be/yBDHkveJUf4?si=duRQOHqRL49-ldAQ&t=9581