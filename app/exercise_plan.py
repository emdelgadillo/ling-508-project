from enum import Enum

class AvailableEquipment(Enum):
    none = "none"
    barbell = "barbell"
    dumbbells = "dumbbells"
    kettlebells = "kettlebells"
    resistance_bands = "resistance bands"
    bodyweight = "bodyweight"
    machine = "machine"

class MuscleGroup(Enum):
    chest = "chest"
    back = "back"
    legs = "legs"
    shoulders = "shoulders"
    arms = "arms"
    core = "core"

class WorkoutType(Enum):
    cardio = "cardio"
    strength = "strength training"
    hiit = "high-intensity interval training"
    mobility = "mobility"
    flexibility = "flexibility"

class RoundType(Enum):
    warmup = "warm up"
    circuit = "circuit"
    cooldown = "cool down"

class Exercise:
    def __init__(self, name: str, duration: int, required_equipment: list[AvailableEquipment], muscle_group: list[MuscleGroup], workout_type: list[WorkoutType]):
        self.name = name
        self.duration = duration
        self.required_equipment = required_equipment
        self.muscle_group = muscle_group
        self.workout_type = workout_type

class Rounds:
    def __init__(self, round_type: RoundType, round_duration: int, set_quantity: int, exercises: list[Exercise]):
        self.round_type = round_type
        self.round_duration = round_duration
        self.set_quantity = set_quantity
        self.exercises = exercises

class WorkoutPlan:
    def __init__(self, name: str, workout_duration: int, rounds: list[Rounds]):
        self.name = name
        self.workout_duration = workout_duration
        self.rounds = rounds
