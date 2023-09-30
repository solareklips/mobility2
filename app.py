from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                          jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not Found", 404
    
  return render_template('jobpage.html', 
                        job=job)

@app.route("/job/<id>/apply")
def apply_to_job(id):

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# NÅET TIL 3:58:58 - arbejder i app.py med app.route(...apply)
# https://youtu.be/yBDHkveJUf4?si=jCnbC-sCk9ziIT8b&t=14338