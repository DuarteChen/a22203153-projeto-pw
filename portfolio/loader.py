from portfolio.models import *
import json



Subject.objects.all().delete()
''''
Teacher.objects.all().delete()
Concept.objects.all().delete()
ScientificArea.objects.all().delete()
Project.objects.all().delete()


with open('portfolio/json/professores.json') as f:
    professores = json.load(f)

    for professor in professores:
        print(f"Name: {professor['name']}")
        print(f"LinkedIn Link: {professor['linkedinLink']}")
        print("\n")

        Teacher.objects.create(
            name = professor['name'],
            linkedinLink = professor['linkedinLink']
            )
with open('portfolio/json/areaCientifica.json') as f:
    areas = json.load(f)

    for area in areas:
        print(f"Name: {area['name']}")
        print("\n")

        ScientificArea.objects.create(
            name = area['name']
            )


with open('portfolio/json/concepts.json') as f:
    concepts = json.load(f)

    for concept in concepts:
        print(f"Name: {concept['name']}")
        print(f"Name: {concept['description']}")
        print("\n")

        Concept.objects.create(
            name = concept['name'],
            description = concept['description']
        )


with open('portfolio/json/projetos.json') as f:
    projetos = json.load(f)

    for projeto in projetos:
        print(f"projectImage: {projeto['projectImage']}")
        print(f"Name: {projeto['name']}")
        print(f"Description: {projeto['description']}")
        print(f"ConceitosAplicados: {projeto['conceitosAplicados']}")
        print(f"youtubeVideo: {projeto['youtubeVideo']}")
        print(f"gitHub: {projeto['gitHub']}")
        print("\n")

        project = Project.objects.create(
            projectImage=projeto['projectImage'],
            name=projeto['name'],
            description=projeto['description'],
            youtubeVideo=projeto['youtubeVideo'],
            gitHub=projeto['gitHub']
        )

        # Link conceitosAplicados to the project
        conceitos = projeto['conceitosAplicados']
        for conceito_name in conceitos:
            try:
                conceito = Concept.objects.get(name=conceito_name)
                project.conceitosAplicados.add(conceito)
            except ConceitoAplicado.DoesNotExist:
                print(f"ConceitoAplicado '{conceito_name}' does not exist and will be skipped.")

        project.save()


with open('portfolio/json/projetos.json') as f:
    projetos = json.load(f)

    for projeto in projetos:
        print(f"projectImage: {projeto['projectImage']}")
        print(f"Name: {projeto['name']}")
        print(f"Description {projeto['description']}")
        print(f"ConceitosAplicados: {projeto['conceitosAplicados']}")
        print(f"youtubeVideo: {projeto['youtubeVideo']}")
        print(f"gitHub: {projeto['gitHub']}")
        print("\n")

        Project.objects.create(
            projectImage = projeto['projectImage'],
            name = projeto['name'],
            description = projeto['description'],
            conceitosAplicados = projeto['conceitosAplicados'],
            youtubeVideo = projeto['youtubeVideo'],
            gitHub = projeto['gitHub']
            )

'''
with open('portfolio/json/cadeiras.json') as f:
    subjects_data = json.load(f)

    for subject_data in subjects_data:
        # Extract subject data
        name = subject_data.get('name', '')
        apresentacao = subject_data.get('apresentacao', '')
        curricularIUnitReadableCode = subject_data.get('curricularIUnitReadableCode', '')
        ects = subject_data.get('ects', 0)
        year = subject_data.get('curricularYear', 0)
        semester = subject_data.get('semester', 1)
        teachers_data = subject_data.get('teacher', [])
        programas_data = subject_data.get('programa', [])

        # Create or get Teacher objects
        teachers = [Teacher.objects.get_or_create(name=teacher_name)[0] for teacher_name in teachers_data]

        # Create or get Program objects
        programas = []
        for program in programas_data:
            program_name = program['name']
            description = program.get('description', '')
            program_obj, created = Concept.objects.get_or_create(name=program_name, defaults={'description': description})
            programas.append(program_obj)

        # Get the related project, if specified
        project_name = subject_data.get('project', '')
        project = Project.objects.filter(name=project_name).first()

        # Get scientific area, if specified
        scientific_area = subject_data.get('scientificArea', None)

        # Create Subject object
        subject = Subject.objects.create(
            name=name,
            apresentacao=apresentacao,
            curricularIUnitReadableCode=curricularIUnitReadableCode,
            ects=ects,
            year=year,
            semester=semester,
            scientificArea=scientific_area,
            project=project
        )

        # Add teachers to the many-to-many field
        subject.teacher.add(*teachers)

        # Add programas to the many-to-many field
        subject.programa.add(*programas)



with open('portfolio/json/areasCientifica_cadeiras.json') as f:
    areascientificas = json.load(f)

    for areacientifica, disciplinas in areascientificas.items():
        try:
            scientific_area = ScientificArea.objects.get(name=areacientifica)

            for disciplina in disciplinas:
                try:
                    subject = Subject.objects.get(name=disciplina)
                    subject.scientificArea = scientific_area
                    courseObj = Course.objects.get(name = "Engenharia Informática")
                    subject.course = courseObj
                    subject.save()
                except Subject.DoesNotExist:
                    print(f"Subject '{disciplina}' does not exist.")
        except ScientificArea.DoesNotExist:
            print(f"Scientific area '{areacientifica}' does not exist.")

for subject in Subject.objects.all():
    print(f"{subject.name} - {subject.scientificArea}")

