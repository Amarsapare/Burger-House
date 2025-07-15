from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    people = db.Column(db.Integer, nullable=False)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(20), nullable=False)
    item = db.Column(db.String(100), nullable=False)

# Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Handle reservation form submission
@app.route('/api/reservation', methods=['POST'])
def make_reservation():
    data = request.json
    # Validate input
    required_fields = ['name', 'email', 'date', 'time', 'people']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing or empty field: {field}'}), 400
    try:
        people_count = int(data['people'])
        if people_count <= 0:
            return jsonify({'error': 'People count must be positive integer'}), 400
    except ValueError:
        return jsonify({'error': 'People count must be an integer'}), 400

    new_reservation = Reservation(
        name=data['name'],
        email=data['email'],
        date=data['date'],
        time=data['time'],
        people=people_count
    )
    try:
        db.session.add(new_reservation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error: ' + str(e)}), 500

    return jsonify({"message": "Reservation received!", "data": data}), 201

# Get all reservations
@app.route('/api/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    results = [
        {
            "id": reservation.id,
            "name": reservation.name,
            "email": reservation.email,
            "date": reservation.date,
            "time": reservation.time,
            "people": reservation.people
        } for reservation in reservations
    ]
    return jsonify(results), 200

# Handle food order submission
@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    # Validate input
    required_fields = ['name', 'student_id', 'item']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing or empty field: {field}'}), 400

    # Validate student_id format (example: must start with 'S' followed by digits, or allow visitor with 'V' prefix)
    student_id = data['student_id']
    if not (student_id.startswith('S') and student_id[1:].isdigit()) and not (student_id.startswith('V') and student_id[1:].isdigit()):
        return jsonify({'error': 'Invalid student ID. Must start with "S" for students or "V" for visitors followed by digits.'}), 400

    new_order = Order(
        student_name=data['name'],
        student_id=student_id,
        item=data['item']
    )
    try:
        db.session.add(new_order)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error: ' + str(e)}), 500

    return jsonify({'message': 'Order placed successfully!', 'data': data}), 201

# Initialize database and run the app
if __name__ == '__main__':
    with app.app_context():
        # Clear all reservations and orders
        db.session.query(Reservation).delete()
        db.session.query(Order).delete()
        db.session.commit()
        db.create_all()
    app.run(debug=True)
