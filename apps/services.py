from apps.exercise_plan import AvailableEquipment, MuscleGroup, WorkoutType
from db.mysql_repository import MysqlRepository

repo = MysqlRepository()

def select_exercises(
    required_equipment: AvailableEquipment | None,
    muscle_group: MuscleGroup | None,
    workout_type: WorkoutType | None,
):
    workout_types = workout_type.value if workout_type else None
    if workout_types == "strength training":
        workout_types = "strength"

    filters = {
        'required_equipment': required_equipment.value if required_equipment else None,
        'muscle_group': muscle_group.value if muscle_group else None,
        'workout_type': workout_types
    }
    return repo.match_exercise(filters)


