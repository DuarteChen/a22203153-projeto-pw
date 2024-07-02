def divide_subjects_byYear(course):

    cursoPorAno = {}

    for subject in course.subjects.all():
        if subject.year in cursoPorAno:
            cursoPorAno[subject.year].append(subject)
        else:
            cursoPorAno[subject.year] = [subject]

    return cursoPorAno
