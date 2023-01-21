def gradingStudents(grades):
    # Write your code here
    grd =[]
    for grade in grades:
        if grade < 38:
            grd.append(grade)
        else:
            rnd = grade % 5
            if rnd >= 3:
                grade = grade + (5 - rnd)
                grd.append(grade)
            else:
                grd.append(grade)
            
    return grd
               
