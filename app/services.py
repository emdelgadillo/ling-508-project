from app.exercise_plan import AvailableEquipment, MuscleGroup, WorkoutType
from db.mysql_repository import MysqlRepository

repo = MysqlRepository()

def select_exercises(
    required_equipment: AvailableEquipment | None,
    muscle_group: MuscleGroup | None,
    workout_type: WorkoutType | None,
):
    filters = {
        'required_equipment': required_equipment.value if required_equipment else None,
        'muscle_group': muscle_group.value if muscle_group else None,
        'workout_type': workout_type.value if workout_type else None,
        'round_type': None  # I will address this later after we meet
    }
    return repo.map_exercise(filters)


