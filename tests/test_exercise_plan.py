from app.exercise_plan import AvailableEquipment, MuscleGroup, WorkoutType, RoundType, Exercise, Rounds, WorkoutPlan

def test_exercise():
    exercise = Exercise(
        name = 'back squat',
        duration = 5,
        required_equipment = [AvailableEquipment.barbell],
        muscle_group = [MuscleGroup.legs],
        workout_type = [WorkoutType.strength])
    assert exercise.name == 'back squat'
    assert exercise.duration == 5
    assert exercise.required_equipment == [AvailableEquipment.barbell]
    assert exercise.muscle_group == [MuscleGroup.legs]
    assert exercise.workout_type == [WorkoutType.strength]

def test_round():
    exercise1 = Exercise(
        name='back squat',
        duration=5,
        required_equipment=[AvailableEquipment.barbell],
        muscle_group=[MuscleGroup.legs],
        workout_type=[WorkoutType.strength]
    )
    exercise2 = Exercise(
        name='deadlift',
        duration=5,
        required_equipment=[AvailableEquipment.barbell],
        muscle_group=[MuscleGroup.back],
        workout_type=[WorkoutType.strength]
    )
    rounds = Rounds(
        round_type = RoundType.circuit,
        round_duration = 20,
        set_quantity = 5,
        exercises=[exercise1, exercise2])
    assert rounds.round_type == RoundType.circuit
    assert rounds.round_duration == 20
    assert rounds.set_quantity == 5
    assert rounds.exercises == [exercise1, exercise2]

def test_workoutplan():
    round1 = Rounds(
        round_type=RoundType.circuit,
        round_duration=20,
        set_quantity=5,
        exercises=[]
    )
    workoutplan = WorkoutPlan(
        name ='Legs and Glutes',
        workout_duration=30,
        rounds=[round1])
    assert workoutplan.name == 'Legs and Glutes'
    assert workoutplan.workout_duration == 30
    assert workoutplan.rounds == [round1]

