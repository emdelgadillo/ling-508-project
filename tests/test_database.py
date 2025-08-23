from db.mysql_repository import *

repo = MysqlRepository()
exercise_entry_one = {
    'required_equipment': 'none',
    'muscle_group': 'legs',
    'workout_type': 'cardio',
}
exercise_entry_two = {
    'required_equipment': 'barbell',
    'muscle_group': None,
    'workout_type': None

}
def test_db():
    exercises =  repo.match_exercise(exercise_entry_one)
    exercises2 = repo.match_exercise(exercise_entry_two)
    assert "jumping jacks" in exercises
    assert "burpees" in exercises
    assert "bent_over row" not in exercises
    assert "deadlift" in exercises2
    assert "pushups" not in exercises2
    assert "bench press" in exercises2


