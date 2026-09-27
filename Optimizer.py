def calc_priority(performance, completion, difficulty, exam_priority):
    performance_score = 100 - performance
    completion_score = 100 - completion
    priority = performance_score + completion_score
    priority = priority + difficulty * 10
    priority = priority + exam_priority * 10
    return priority

def schedule(subjects, total_time):
    tot_priority = sum(subject["priority"] for subject in subjects)
    
    print("\n==================================")
    print("         SMART STUDY PLAN")
    print("===================================")
    
    remaining_time = total_time

    for i in range(len(subjects)):
        subject = subjects[i]
        study_time = (subject["priority"] / tot_priority) * total_time
        study_time = round(study_time)
        if study_time < 20:
            study_time = 20
    
        if study_time > remaining_time:
            study_time = remaining_time

            if remaining_time >= 20:
                study_time = remaining_time
            else:
                study_time = 0
        
        if study_time > 0:
            print(f"\nSession {i+1}")
            print(f"Subject: {subject['name']}")
            print(f"Study Time: {study_time} minutes")
            print(f"Priority Score: {round(subject['priority'], 2)}")
            
            remaining_time = remaining_time - study_time

            if i < len(subjects) - 1 and remaining_time > 10:
                print("Break: 10 minutes")
                remaining_time = remaining_time - 10
                print("\n==================================")
        
        if remaining_time <= 0:
            break

def recommendation(subjects):
    print("\n--------STUDY RECOMMENDATIONS--------")
    
    for subject in subjects:
        if subject["performance"] < 60:
            print(f"{subject['name']}: Give extra attention because performance is low")

        elif subject["completion"] < 50:
            print(f"{subject['name']}: Complete more syllabus before revision.")

        elif subject["difficulty"] > 3:
            print(f"{subject['name']}: This is a difficult subject. Practice regularly.")

        else:
            print(f"{subject['name']}: Continue regular revision.")

def main():
    print("\n=============================================")
    print("            SMART STUDY SESSION OPTIMIZER")
    print("==============================================")

    try:
        total_time = int(input("\nEnter the time you have for studying (minutes): "))
        if total_time <= 0:
            print("You don't have time.")
            return

        number = int(input("Enter number of subjects: "))
        if number <= 0:
            print("Wow, you don't have any subject.")
            return

    except ValueError:
        print("This number is not valid here.")
        return

    subjects = []

    for i in range(number):
        print("\n----------------------------------------------")
        print(f"Subject {i + 1}")
        print("-----------------------------------------------")

        name = input("Enter subject name: ")

        try:
            performance = float(input("Enter current performance (0-100): "))
            syllabus_completed = float(input("Enter syllabus completed (0-100): "))
            difficulty_level = int(input("Enter difficulty level (1-5): "))
            exam_priority = int(input("Enter exam priority (1-5): "))

            if not (0 <= performance <= 100):
                print("Performance must be between 0 and 100.")
                return

            if not (0 <= syllabus_completed <= 100):
                print("Syllabus completed must be between 0 and 100.")
                return

            if not (1 <= difficulty_level <= 5):
                print("Difficulty level must be between 1 and 5.")
                return

            if not (1 <= exam_priority <= 5):
                print("Exam priority must be between 1 and 5.")
                return

        except ValueError:
            print("Please enter valid values.")
            return

        priority = calc_priority(
            performance,
            syllabus_completed,
            difficulty_level,
            exam_priority
        )
        
        subject = {
            "name": name,
            "performance": performance,
            "completion": syllabus_completed,
            "difficulty": difficulty_level,
            "exam_priority": exam_priority,
            "priority": priority
        }

        subjects.append(subject)

    print("\n==============================================")
    print("         SUBJECT PRIORITY ANALYSIS")
    print("==============================================")

    for subject in subjects:
        print(f"\nSubject: {subject['name']}")
        print(f"Performance: {subject['performance']}%")
        print(f"Syllabus Completed: {subject['completion']}%")
        print(f"Difficulty Level : {subject['difficulty']}/5")
        print(f"Exam Priority: {subject['exam_priority']}/5")
        print(f"Priority Score: {round(subject['priority'], 2)}")

    schedule(subjects, total_time)
    recommendation(subjects)

    print("\nStudy plan generated successfully!")

main()
