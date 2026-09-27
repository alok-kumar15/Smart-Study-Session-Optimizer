# Problem Statement

Students often have limited study time and multiple subjects to prepare for. Giving the same amount of time to every subject may not be effective because different subjects have different levels of difficulty, syllabus completion, performance, and exam importance.

The Smart Study Session Optimizer is developed to provide a simple way to prioritize subjects and distribute available study time. The program takes the student's current performance, syllabus completion, subject difficulty, and exam priority as input. It then calculates a priority score for each subject and uses these scores to generate a study schedule.

The program also provides basic recommendations to help students identify subjects that may require additional attention.


# Scope of the Project

The scope of this project is limited to creating a command-line based study planning system using Python.

The program can:

1. Accept available study time from the user.
2. Accept information for multiple subjects.
3. Calculate a priority score for each subject.
4. Allocate study time based on the calculated priority.
5. Add 10-minute breaks between applicable study sessions.
6. Display subject priority information.
7. Provide basic study recommendations based on performance, syllabus completion, and difficulty.
8. Validate the entered values within predefined ranges.

The current project does not include permanent data storage, user accounts, graphical interfaces, online synchronization, or AI-based recommendations.


# Target Users

The primary target users are:

1. School students who need help organizing study time among different subjects.
2. College students who want a simple way to prioritize subjects before examinations.
3. Students preparing for examinations with limited available study time.
4. Beginner Python learners who want to understand how Python can be used to build a practical application.

The program is designed for users who want a simple and easy-to-use study planning tool without requiring complex software or technical knowledge.


# High-Level Features

## 1. Subject Information Input

The program allows users to enter:

Subject name
Current performance
Syllabus completion percentage
Subject difficulty
Exam priority

## 2. Priority Score Calculation

The program calculates a priority score using:

Performance
Syllabus completion
Difficulty
Exam priority

A higher priority score indicates that the subject receives a larger share of the available study time.

## 3. Automatic Study Schedule

The program distributes the user's available study time among the entered subjects according to their priority scores.

## 4. Break Allocation

The program adds a 10-minute break between study sessions when sufficient time remains.

## 5. Study Recommendations

The program provides simple recommendations based on the subject information. For example, subjects with low performance are recommended for additional attention, while difficult subjects are recommended for regular practice.

## 6. Input Validation

The program checks whether user inputs are within the expected ranges and displays an error message when invalid values are entered.

## 7. Command-Line Interface

The entire application operates through the Python command line, making it simple to run and use without additional software or external Python libraries.