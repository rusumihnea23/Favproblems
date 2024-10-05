def add_student(students:dict,name:str):
    students[name]=[]
def print_student(students:list,name:str):
    if name in students:
        print(f"{name}:")
        avg=0
        if len(students[name])==0:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
        for courses in students[name]:
            print(f"  {courses[0]} {courses[1]}")
            avg=courses[1]+avg
        if len(students[name])>0:
            print(f" average grade {avg/len(students[name])}")
        
    else:
        print(f"{name}: no such person in the database")
def add_course(students:dict,name:str,course:tuple):
    ok=0
    for courses in students[name]:
        if course[0]==courses[0] and course[1]>courses[1]:
            val=courses
            ok=1
            break
        elif course[0]==courses[0] and course[1]<courses[1]:
            ok=2
            break
    if ok==1:
        students[name].remove(val)
        students[name].append(course)

    if course[1]!=0 and course not in students[name] and ok==0:
        students[name].append(course)
    
def summary(students:list):
    averages=[]
    cours=0
    maxavg=0
    maxc=0
    nrstd=len(students)
    for student in students:
        cours=len(students[student])
        if cours>maxc:
            maxc=cours
            name_maxc=student
        avg=0
        for courses in students[student]:
            avg=courses[1]+avg
        avg=avg/len(students[student])
        if avg>maxavg:
            maxavg=avg
            name_avg=student
    print(f"students {nrstd}")
    print(f"most courses completed {maxc} {name_maxc}")
    print(f"best average grade {maxavg} {name_avg}")
        



if __name__=="__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)