CREATE DATABASE exercise;
use exercise;
CREATE TABLE exercises (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    required_equipment VARCHAR(255),
    muscle_group VARCHAR(255),
    workout_type VARCHAR(255),
    round_type VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO exercises
    (name, required_equipment, muscle_group, workout_type, round_type)
VALUES
    ('push ups', 'none', 'chest', 'strength', 'circuit'),
    ('goblet squat', 'dumbbells,kettlebells', 'legs,arms', 'strength', 'circuit'),
    ('burpees', 'none', 'legs,core,shoulders,chest,arms', 'cardio,hiit', 'circuit'),
    ('rowing', 'rowing machine', 'core,legs,shoulders', 'cardio', 'circuit,warm up,cool down'),
    ('jogging', 'none,treadmill', 'legs', 'cardio', 'circuit,warm up,cool down'),
    ('jumping jacks', 'none', 'legs', 'cardio,hiit', 'circuit'),
    ('high knees', 'none', 'legs,core', 'cardio,hiit', 'circuit,warm up'),
    ('bench press', 'barbell', 'chest,shoulders,arms', 'strength', 'circuit'),
    ('deadlift', 'barbell', 'legs,core', 'strength', 'circuit'),
    ('bent-over row', 'dumbbells', 'chest,shoulders,arms', 'strength', 'circuit'),
    ('bicep curl', 'dumbbells,resistance bands', 'arms', 'strength', 'circuit'),
    ('mountain climbers', 'none', 'arms,core,legs', 'hiit,cardio', 'circuit'),
    ('squat jumps', 'none', 'legs', 'cardio,hiit', 'circuit'),
    ('90/90 hip switch', 'none', 'legs', 'mobility', 'circuit'),
    ('cat cow', 'none', 'chest', 'mobility', 'circuit'),
    ('thread the needle', 'none', 'chest', 'mobility', 'circuit'),
    ('achilles opener', 'none', 'chest', 'mobility', 'circuit'),
    ('horizontal ts', 'none', 'chest', 'mobility', 'circuit'),
    ('seated hamstring stretch', 'none', 'chest', 'flexibility', 'warm up,cool down'),
    ('standing calf stretch', 'none', 'chest', 'flexibility', 'warm up,cool down'),
    ('quad stretch', 'none', 'chest', 'flexibility', 'circuit,cool down'),
    ('butterfly stretch', 'none', 'chest', 'flexibility', 'circuit,cool down'),
    ('triceps stretch', 'none', 'chest', 'flexibility', 'circuit,cool down')
;