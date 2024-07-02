from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 200)
    linkedinLink = models.URLField(max_length = 300, blank = True)

    def __str__(self):
        return f'{self.name}'

class Concept(models.Model):
    name = models.TextField(max_length = 50)
    description = models.TextField(blank = True)

    def __str__(self):
        return f'{self.name}'

class ScientificArea(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.name}'

class Project(models.Model):
    projectImage = models.ImageField(upload_to = 'projeto/projectImage/', blank = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    conceitosAplicados = models.ManyToManyField(Concept, related_name='ProjectConcepts', blank = True)
    youtubeVideo = models.URLField(max_length = 300, blank = True)
    gitHub = models.URLField(max_length = 300, blank = True)

    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name = models.CharField(max_length = 50)
    apresentation = models.TextField(blank = True)
    conceitosAplicados = models.ManyToManyField(Concept, related_name='CourseConcepts', blank = True)

    bachelor = 1
    master = 2
    phd = 3

    choices = [
        (bachelor, "Bachelor's Degree"),
        (master, "Master's Degree"),
        (phd, "PhD")
    ]
    courseType = models.IntegerField(choices = choices, default = bachelor)

    def __str__(self):
        return f'{self.name}'

class Subject(models.Model):
    name = models.CharField(max_length = 300)#
    teacher = models.ManyToManyField(Teacher, related_name='SubjectTeacher')#
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank = True, null = True)#
    apresentacao = models.TextField(blank = True)#
    programa = models.ManyToManyField(Concept, related_name='Programa')#
    curricularIUnitReadableCode = models.CharField(max_length = 300, blank = True)#
    scientificArea = models.ForeignKey(ScientificArea, on_delete=models.CASCADE, blank = True, null = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank = True, null = True)
    ects = models.IntegerField(null=True)#
    year = models.IntegerField()#

    firstSemester = 1
    secondSemester = 2
    semester_choices = [
        (firstSemester, "1st Semester"),
        (secondSemester, "2nd Semester"),
    ]
    semester = models.IntegerField(choices=semester_choices, default=1)

    nota = models.IntegerField(default = 0)#

    def __str__(self):
        return f'{self.name}'


