from app.exercise_plan import AvailableEquipment, MuscleGroup, WorkoutType
from app.services import select_exercise

def test_service():
    exercises = select_exercise(
        required_equipment=AvailableEquipment.none,
        muscle_group=MuscleGroup.legs,
        workout_type=WorkoutType.cardio
    )
    assert "jumping jacks" in exercises
    assert "burpees" in exercises
    assert "bent-over row" not in exercises

def test_service_2():
    exercises = select_exercise(
        required_equipment=AvailableEquipment.barbell,
        muscle_group=None,
        workout_type=None
    )
    assert "deadlift" in exercises
    assert "pushups" not in exercises
    assert "bench press" in exercises
