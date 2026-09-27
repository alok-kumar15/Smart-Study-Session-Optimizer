# Smart Study Session Optimizer

A simple Python-based Smart Study Session Optimizer that creates a personalized study plan based on a student's current performance, syllabus completion, subject difficulty, and exam priority.

The program calculates a priority score for each subject and distributes the available study time according to the calculated priorities. It also provides subject-specific study recommendations.


## Project Overview

The Smart Study Session Optimizer solves this problem by:

1.  Taking information about each subject from the user.
2.  Calculating a priority score for every subject.
3.  Allocating study time according to subject priority.
4.  Adding short breaks between study sessions.
5.  Providing personalized study recommendations.
6.  Generating a complete study plan automatically.


## Features

### 1. Subject Priority Calculation

The program calculates a priority score using four factors:

Current performance
Syllabus completion
Subject difficulty
Exam priority

Subjects with lower performance or lower syllabus completion receive a higher priority.

### 2. Automatic Study Time Allocation

Available study time is distributed according to the priority of each subject.

For example:

Subject A → High Priority → More Study Time
Subject B → Medium Priority → Moderate Study Time
Subject C → Low Priority → Less Study Time

### 3. Break Management

The program automatically adds a 10-minute break between study sessions when enough time remains.

### 4. Input Validation

The program checks whether the entered values are valid.

```text

 Input                                Valid Range

Performance                             0–100
Syllabus Completion                     0–100
Difficulty	                             1–5
Exam Priority	                         1–5
Study Time	                        Greater than 0
Number of Subjects                  Greater than 0

```

Invalid input generates an appropriate error message.


## Project Flow

```text

Student Information
       ↓ 
Subject Details
       ↓ 
Performance + Completion
       ↓ 
Difficulty + Exam Priority
       ↓ 
Priority Score Calculation
       ↓ 
Study Time Allocation
       ↓ 
Study Schedule
       ↓ 
Study Recommendations

```


## Technologies Used

This project uses Python programming concepts.

### 1. Development Environment

Visual Studio Code (VS Code)

### 2. Python Concepts Used

1.  Functions
2.  Variables
3.  Lists
4.  Dictionaries
5.  for loops
6.  if-elif-else
7.  User input
8.  Exception handling
9.  Mathematical calculations
10. String formatting

### 3. Python Libraries

1. No external libraries required

2. Uses Python built-in functions

## Steps to install and run the program


## Project Structure

A simple project structure can be:

```text

Smart-Study-Session-Optimizer/ 
│ 
├── study_optimizer.py 
│ 
└── README.md

```

Contains the complete Python program for:

1. Calculating subject priorities
2. Creating the study schedule
3. Generating recommendations
4. Taking user input


## How the Program Works

The project is divided into four main functions.

### 1. calculate_priority()

def calculate_priority(performance, completion, difficulty, exam_priority):

This function calculates the priority score of a subject.

It considers:

```text

Low Performance
        +
Low Completion
        +
High Difficulty
        +
High Exam Priority

```

and converts them into a single priority score.

### 2. create_schedule()

def create_schedule(subjects, total_time):

This function creates the study timetable.

It:

1. Calculates the total priority.
2. Calculates each subject's share of the available time.
3. Allocates study time.
4. Ensures a minimum session time where possible.
5. Adds 10-minute breaks.
6. Displays the final study plan.

### 3. recommendations()

def recommendations(subjects):

This function provides recommendations based on subject performance and other parameters.

### 4. main()

def main():

The main() function controls the complete program.

It:

```text

Gets user input
       ↓
Validates input
       ↓ 
Calculates priority
       ↓  
Stores subject information
       ↓ 
Displays analysis  
       ↓ 
Creates study schedule 
       ↓ 
Provides recommendations

```


## Instruction For Testing

### 1. Run the program using:

python Optimizer.py

The program should start and display:

``` text
=============================================
       SMART STUDY SESSION OPTIMIZER
==============================================
```

### 2. Test Normal Input

Use valid values for all inputs.

Test Input
Available study time: 180
Number of subjects: 3

Subject 1:
Name: Mathematics
Performance: 60
Completion: 50
Difficulty: 4
Exam Priority: 5

Subject 2:
Name: Physics
Performance: 70
Completion: 70
Difficulty: 4
Exam Priority: 4

Subject 3:
Name: English
Performance: 85
Completion: 90
Difficulty: 2
Exam Priority: 2

### 3. Test Priority Calculation

Check whether the priority score is calculated correctly.

For example:

Performance = 60
Completion = 50
Difficulty = 4
Exam Priority = 5

Calculation:

Performance Score = 100 - 60 = 40
Completion Score  = 100 - 50 = 50

Difficulty Score = 4 × 10 = 40
Exam Priority Score = 5 × 10 = 50

Priority Score = 40 + 50 + 40 + 50 = 180

The program should display:

Priority Score: 180

### 4. Test Input Validation

The program should reject values outside the allowed ranges.

Test A: Invalid Performance

Enter:

Performance: 120

Expected output:

Performance must be between 0 and 100.
Test B: Invalid Completion

Enter:

Completion: -10

Expected output:

Completion must be between 0 and 100.
Test C: Invalid Difficulty

Enter:

Difficulty: 6

Expected output:

Difficulty must be between 1 and 5.
Test D: Invalid Exam Priority

Enter:

Exam Priority: 0

Expected output:

Exam priority must be between 1 and 5.

### 5. Test Invalid Text Input

Enter text where a number is required.

Example:

Enter available study time (minutes): abc

Expected output:

Please enter valid numbers.

The program should stop without producing a Python error or traceback.

### 6. Test Study Time Validation

Enter:

Available study time: 0

Expected output:

Study time must be greater than 0.

Also test a negative value:

Available study time: -60

The same validation message should be displayed.

### 7. Test Number of Subjects

Enter:

Number of subjects: 0

Expected output:

Number of subjects must be greater than 0.

Also test a negative number:

Number of subjects: -2

The program should reject the input.

### 8. Test Study Recommendations

Test different subject conditions to verify that the correct recommendation is generated.

Low Performance
Performance: 40

Expected:

Give extra attention because performance is low
Low Syllabus Completion

Use:

Performance: 70
Completion: 40

Expected:

Complete more syllabus before revision.
Difficult Subject

Use:

Performance: 70
Completion: 70
Difficulty: 4

Expected:

This is a difficult subject. Practice regularly.
Normal Subject

Use values such as:

Performance: 80
Completion: 90
Difficulty: 2

Expected:

Continue regular revision.

### 9. Test Break Allocation

Enter multiple subjects and provide enough study time.

For example:

Study Time: 180 minutes
Number of Subjects: 3

The program should display:

Break: 10 minutes

between applicable study sessions.

### 10. Test Minimum Study Time

Use several subjects with a large difference in priority.

Check whether the program attempts to give a minimum of 20 minutes to a subject when sufficient time remains.

The program should also prevent the allocated study time from exceeding the remaining available time.


## Study Time Calculation

The study time for each subject is calculated using its proportion of the total priority:

Study Time =
(Subject Priority / Total Priority) × Total Available Time

The calculated value is rounded to the nearest whole minute.

The program also tries to maintain a minimum study session of 20 minutes when sufficient time is available.


## Objective of the Project

The main objective of this project is to demonstrate how Python can be used to create a simple decision-making system for study planning.

Instead of giving every subject equal study time, the program considers multiple factors and creates a more personalized schedule.


## Future Project Vision

The project can eventually become a complete AI-powered Personal Study Planner.

A possible future architecture:

```text

Student Data
     ↓ 
Performance Tracking
     ↓ 
Subject Analysis
     ↓ 
Priority Calculation
     ↓ 
AI-Based Planning 
     ↓ 
Personalized Schedule
     ↓ 
Progress Tracking 
     ↓ 
Schedule Adjustment

```
