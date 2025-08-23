from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from apps.services import *

def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/search": {"origins": "http://localhost:port"}})

    @app.route('/')
    def doc() -> str:
        app.logger.info("doc - Got request")
        with open("apps/doc.html", "r") as f:
            return f.read()

    @app.route("/search", methods=["GET"])
    @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
    def search_exercise():
        equipment = request.args.get("equipment")
        muscle_group = request.args.get("muscle_group")
        workout_type = request.args.get("workout_type")

        equip = AvailableEquipment(equipment) if equipment else None
        muscle = MuscleGroup(muscle_group) if muscle_group else None
        w_type = WorkoutType(workout_type) if workout_type else None

        exercises = select_exercises(
            required_equipment=equip,
            muscle_group=muscle,
            workout_type=w_type
        )
        app.logger.info(f"/search - Found exercises: {exercises}")
        return jsonify({"exercises": exercises})

    return app


if __name__ == "__main__":
    myapp = create_app()
    myapp.run(host="0.0.0.0")

