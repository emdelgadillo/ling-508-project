# Exercise Search
You can search for exercises using the "Find an Exercise" interface. 
Just select the options you want from the dropdown menus for the equipment you have available, which muscle group you want to target, and what workout type you would like and click "Submit".
The page will display the possible exercises for the selected criteria if there are any available in a formatted list, for example
Here are the exercises that match your criteria: high knees, jogging, jumping jacks, squat jumps

The API can be called directly without the UI, using a GET request, but you must pass the params in the URL.
An example endpoint is `http://localhost:5000/search?equipment={insert selection here}&muscle_group={insert selection here}&workout_type={insert selection here}`.