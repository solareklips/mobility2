from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

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

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return jsonify(job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# NÅET TIL 3:27:33 - SKAL TIL RENDER.COM
# https://youtu.be/yBDHkveJUf4?si=hTzRSp2RQYrdrLSV&t=12453