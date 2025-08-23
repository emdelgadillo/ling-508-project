import mysql.connector


class MysqlRepository:

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db', # to run LOCALLY, this should be localhost
            'port': '3306', # to run LOCALLY, this should be 32000
            'database': 'exercise'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def all_exercises(self) -> dict[str, dict]:
        sql = ("SELECT name, required_equipment, muscle_group, workout_type"
               " FROM exercises")
        self.cursor.execute(sql)
        exercise_dict = {
            name: {
                'required_equipment': required_equipment,
                'muscle_group': muscle_group,
                'workout_type': workout_type
            }
            for (name, required_equipment, muscle_group, workout_type) in self.cursor}
        return exercise_dict

    def match_exercise(self, entry: dict) -> list[str]:
        all_exercises = self.all_exercises()
        matches = []
        for name, values in all_exercises.items():
            if (
                    (entry['required_equipment'] is None or entry['required_equipment'] in values['required_equipment'].split(',')) and
                    (entry['muscle_group'] is None or entry['muscle_group'] in values['muscle_group'].split(',')) and
                    (entry['workout_type'] is None or entry['workout_type'] in values['workout_type'].split(','))
            ):
                matches.append(name)
        return matches