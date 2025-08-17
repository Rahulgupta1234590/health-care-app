from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory data (use database later)
patients = [
    {"id": 1, "name": "John Doe", "age": 30, "condition": "Flu"},
    {"id": 2, "name": "Jane Smith", "age": 25, "condition": "Fever"}
]

appointments = [
    {"id": 1, "patient": "John Doe", "doctor": "Dr. Adams", "date": "2025-08-15"},
    {"id": 2, "patient": "Jane Smith", "doctor": "Dr. Brown", "date": "2025-08-17"}
]

doctors = [
    {"id": 1, "name": "Dr. Adams", "specialty": "Cardiology"},
    {"id": 2, "name": "Dr. Brown", "specialty": "Neurology"}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/patients")
def list_patients():
    return render_template("patients.html", patients=patients)

@app.route("/patients/add", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        condition = request.form.get("condition")
        new_id = max([p['id'] for p in patients]) + 1 if patients else 1
        patients.append({"id": new_id, "name": name, "age": int(age), "condition": condition})
        return redirect(url_for('list_patients'))
    return render_template('add_patient.html')

@app.route("/doctors")
def list_doctors():
    return render_template("doctors.html", doctors=doctors)

@app.route("/appointments")
def list_appointments():
    return render_template("appointments.html", appointments=appointments)

@app.route("/appointments/book", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        patient = request.form.get('patient')
        doctor = request.form.get('doctor')
        date = request.form.get('date')
        new_id = max([a['id'] for a in appointments]) + 1 if appointments else 1
        appointments.append({"id": new_id, "patient": patient, "doctor": doctor, "date": date})
        return redirect(url_for('list_appointments'))
    return render_template('book_appointment.html', patients=patients, doctors=doctors)

if __name__ == "__main__":
    app.run(debug=True)
