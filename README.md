# Project Overview
This is a program that tracks the workout exercises of the user. 

## Objectives
- Ask user for exercise type and number of sets
- Request for calorie data from API
- Process calorie data
- Post exercise details to spreadsheet API
  
## Results
The program first asks the user for the exercise type and number of sets. 

Next, the program requests calorie data from the nutritionix API. 

Finally, the calorie and exercise data is loaded to a spreadsheet for easy accessability.

## Process
```mermaid
flowchart TD
start(((START)))
input_exercise[Request User for exercise name]
input_sets[Request User for number of sets]
exercise_info[Request calorie data from API]
spreadsheet[Load exercise details to spreadsheet]
finish(((END)))

start --> input_exercise
input_exercise --> input_sets
input_sets --> exercise_info
exercise_info --> spreadsheet
spreadsheet --> finish
