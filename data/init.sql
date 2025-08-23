CREATE DATABASE exercise;
use exercise;
CREATE TABLE exercises (
    name VARCHAR(255),
    required_equipment VARCHAR(255),
    muscle_group VARCHAR(255),
    workout_type VARCHAR(255),
    round_type VARCHAR(255),
    PRIMARY KEY (name)
);

INSERT INTO exercises
    (name, required_equipment, muscle_group, workout_type, round_type)
VALUES
    ('push ups', 'none', 'chest', 'strength', 'circuit'),
    ('sit ups', 'none', 'core', 'strength', 'circuit'),
    ('goblet squat', 'dumbbells', 'full body', 'strength', 'circuit'),
    ('burpees', 'none', 'full body', 'cardio', 'circuit'),
    ('rowing', 'rowing machine', 'full body', 'cardio', 'circuit,warm up,cool down'),
    ('jogging', 'none', 'legs', 'cardio', 'circuit,warm up,cool down'),
    ('jumping jacks', 'none', 'legs', 'cardio', 'circuit'),
    ('high knees', 'none', 'legs', 'cardio', 'circuit,warm up'),
    ('bench press', 'barbell', 'upper body', 'strength', 'circuit'),
    ('deadlift', 'barbell', 'legs', 'strength', 'circuit'),
    ('bent-over row', 'dumbbells', 'upper body', 'strength', 'circuit'),
    ('bicep curl', 'dumbbells', 'arms', 'strength', 'circuit'),
    ('mountain climbers', 'none', 'full body', 'cardio', 'circuit'),
    ('squat jumps', 'none', 'legs', 'cardio', 'circuit'),
    ('90/90 hip switch', 'none', 'legs', 'mobility', 'circuit'),
    ('cat cow', 'none', 'chest', 'mobility', 'circuit'),
    ('thread the needle', 'none', 'chest', 'mobility', 'circuit'),
    ('achilles opener', 'none', 'legs', 'mobility', 'circuit'),
    ('horizontal ts', 'none', 'chest', 'mobility', 'circuit'),
    ('seated hamstring stretch', 'none', 'legs', 'flexibility', 'warm up,cool down'),
    ('standing calf stretch', 'none', 'legs', 'flexibility', 'warm up,cool down'),
    ('quad stretch', 'none', 'legs', 'flexibility', 'circuit,cool down'),
    ('butterfly stretch', 'none', 'arms', 'flexibility', 'circuit,cool down'),
    ('triceps stretch', 'none', 'arms', 'flexibility', 'circuit,cool down')
;