import mysql.connector


class MysqlRepository:

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', # to run LOCALLY, this should be localhost
            'port': '32000', # to run LOCALLY, this should be 32000
            'database': 'exercise'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def find_exercise(self) -> list[dict]:
        sql = ("SELECT * "
               "FROM exercises")
        self.cursor.execute(sql)
        exercise_dict = [{'id': id,
                    'name': name,
                    'required_equipment': required_equipment,
                    'muscle_group': muscle_group,
                    'workout_type': workout_type,
                    'round_type': round_type,
                    } for (id, name, required_equipment, muscle_group, workout_type, round_type) in self.cursor]
        return exercise_dict

    def map_exercise(self, entry: dict) -> list[str]:
        all_exercises = self.find_exercise()
        matches = []
        for x in all_exercises:
            if (
                    (entry['required_equipment'] is None or entry['required_equipment'] in x['required_equipment'].split(',')) and
                    (entry['muscle_group'] is None or entry['muscle_group'] in x['muscle_group'].split(',')) and
                    (entry['workout_type'] is None or entry['workout_type'] in x['workout_type'].split(',')) and
                    (entry['round_type'] is None or entry['round_type'] in x['round_type'].split(','))
            ):
                matches.append(x['name'])
        return matches