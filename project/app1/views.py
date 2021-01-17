from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from .models import Dept, Teachers, Assign, AssignTime, Class, Courses, DAYS_OF_WEEK
from .forms import DeptForm, TeacherForm, ClassForm, CourseForm, AssignForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages


@login_required()
def index(request):
    if request.user.is_staff:
        return render(request, 't_homepage.html')
    if request.user.is_active:
        return render(request, 'homepage.html')
    return render(request, 'logout.html')


def Department(request):
    if request.method == 'POST':
        dept_id = request.POST['dept_id']
        dept_name = request.POST['dept_name']

        from django.contrib import auth
        x = Dept(dept_id=dept_id, dept_name=dept_name)
        x.save()
        print("To add the new Department")
        messages.success(request, 'To Add The Successfully ')
        return render(request, 'Department.html')
    else:
        return render(request, 'Department.html')


def Program(request):
    dept = Dept.objects.all()
    print(dept)
    if request.method == 'POST':
        program_id = request.POST['program_id']
        program_name = request.POST['program_name']
        dept = request.POST['dept']

        x = Class(program_id=program_id, program_name=program_name, Dept_id=dept)
        x.save()
        print("To add the new Program")
        messages.success(request, 'To Add The Successfully ')

        return render(request, 'Program.html')

    else:
        return render(request, 'Program.html', {'dept': dept})


def Course(request):
    program = Class.objects.all()
    print(program)
    if request.method == 'POST':
        course_id = request.POST['course_id']
        course_name = request.POST['course_name']
        program = request.POST['program']

        x = Courses(course_id=course_id, course_name=course_name, program_id=program)
        x.save()
        print("To add the new Courses")
        messages.success(request, 'To Add The Successfully ')

        return render(request, 'Course.html')

    else:
        return render(request, 'Course.html', {'program': program})


def Teacher(request):
    ept = Dept.objects.all()
    if request.method == 'POST':
        teacher_id1 = request.POST['teacher_id']
        teacher_name1 = request.POST['teacher_name']
        dept = request.POST['dept']

        from django.contrib import auth
        x = Teachers(teacher_id=teacher_id1, teacher_name=teacher_name1, Dept_id=dept)
        x.save()
        print("To add the new Program")
        messages.success(request, 'To Add The Successfully ')

        return render(request, 'Teacher.html')

    else:
        return render(request, 'Teacher.html', {'dept': ept})


def assign(request):
    ept = Dept.objects.all()
    course = Courses.objects.all()
    teacher = Teachers.objects.all()
    if request.method == 'POST':
        course_id1 = request.POST['course']
        teacher_name1 = request.POST['teacher']

        from django.contrib import auth
        x = Assign(course_id=course_id1, teacher_id=teacher_name1)
        x.save()
        print("To add the new Assign")
        messages.success(request, 'To Add The Successfully ')

        return render(request, 'assign.html')

    else:
        context = {'course': course, 'teacher': teacher}
        return render(request, 'assign.html', context)


def viewD(request):
    dpt = Dept.objects.all()
    context = {'dpt': dpt}
    return render(request, 'viewD.html', context)


def EditD(request, dept_id):
    post = get_object_or_404(Dept, dept_id=dept_id)
    if request.method == "POST":
        form = DeptForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('viewD')
    else:
        form = DeptForm(instance=post)
    return render(request, 'EditD.html', {'form': form})


def deleteD(request, dept_id):
    post = get_object_or_404(Dept, dept_id=dept_id)
    post.delete()
    return redirect('viewD')


def deleteT(request, teacher_id):
    post = get_object_or_404(Teachers, teacher_id=teacher_id)
    post.delete()
    return redirect('viewT')


def deleteCl(request, program_id):
    post = get_object_or_404(Class, program_id=program_id)
    post.delete()
    return redirect('viewCl')


def deleteCo(request, course_id):
    post = get_object_or_404(Courses, course_id=course_id)
    post.delete()
    return redirect('viewCo')


def viewT(request):
    dpt = Teachers.objects.all()
    context = {'dpt': dpt}
    return render(request, 'viewT.html', context)


def EditT(request, teacher_id):
    post = get_object_or_404(Teachers, teacher_id=teacher_id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('viewT')
    else:
        form = TeacherForm(instance=post)
    return render(request, 'EditT.html', {'form': form})


def viewCl(request):
    dpt = Class.objects.all()
    context = {'dpt': dpt}
    return render(request, 'viewCl.html', context)


def EditCl(request, program_id):
    post = get_object_or_404(Class, program_id=program_id)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('viewCl')
    else:
        form = ClassForm(instance=post)
    return render(request, 'EditCl.html', {'form': form})


def viewCo(request):
    dpt = Courses.objects.all()
    context = {'dpt': dpt}
    return render(request, 'viewCo.html', context)


def EditCo(request, course_id):
    post = get_object_or_404(Courses, course_id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('viewCo')
    else:
        form = CourseForm(instance=post)
    return render(request, 'EditCo.html', {'form': form})


def viewAs(request):
    dpt = Assign.objects.all()
    context = {'dpt': dpt}
    return render(request, 'viewAs.html', context)


def EditAs(request, id):
    post = get_object_or_404(Assign, id=id)
    if request.method == "POST":
        form = AssignForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('viewAs')
    else:
        form = AssignForm(instance=post)
    return render(request, 'EditAs.html', {'form': form})


def timetable1(request):
    qs = Assign.objects.all()
    # fatch the all data in Course
    title_contains_query = request.GET.get('title_contains')  # that contain the input in search
    print(title_contains_query)
    matrix = [['' for i in range(8)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(8):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4:  # breake k liye
                continue
            try:

                if title_contains_query != '' and title_contains_query is not None:
                    qs = qs.filter(course__course_id__istartswith=title_contains_query) and qs.filter(
                        course__course_id__icontains='10')
                    if i + 1 == j:
                        matrix[i][j] = qs[0]
                    elif i + 2 == j:
                        matrix[i][j] = qs[1]
                    elif i + 3 == j:
                        matrix[i][j] = qs[2]
                    elif i + 5 == j:
                        matrix[i][j] = qs[3]
                    elif i + 6 == j:
                        matrix[i][j] = qs[4]
                    elif i == j:
                        matrix[i][j] = qs[4]
                    elif i - 1 == j:
                        matrix[i][j] = qs[3]
                    elif i == 3 and j == 1:
                        matrix[i][j] = qs[0]
                    elif i - 2 == j:
                        matrix[i][j] = qs[2]
                    elif i == 5 and j == 1:
                        matrix[i][j] = qs[1]
                    else:
                        matrix[i][j] = 'empty'
                else:
                    matrix[i][j] = ''

            except Assign.DoesNotExist:

                pass
        t += 1

    context = {'queryset': qs,
               'matrix': matrix,
               }
    return render(request, 'timetable1.html', context)


def timetable2(request):
    qs = Assign.objects.all()
    title_contains_query = request.GET.get('title_contains')
    print(title_contains_query)
    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(course__course_id__icontains=title_contains_query)
        print(qs)
    matrix = [['' for i in range(8)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(8):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4:  # breake k liye
                continue
            try:
                if title_contains_query != '' and title_contains_query is not None:
                    qs = qs.filter(course__course_id__istartswith=title_contains_query) and qs.filter(
                        course__course_id__icontains='20')
                    if i + 1 == j:  # conditions k sath Course to put kiya ja raha hai
                        matrix[i][j] = qs[2]
                    elif i + 2 == j:
                        matrix[i][j] = qs[4]
                    elif i + 3 == j:
                        matrix[i][j] = qs[0]
                    elif i + 5 == j:
                        matrix[i][j] = qs[1]
                    elif i + 6 == j:
                        matrix[i][j] = qs[3]
                    elif i == 2 and j == 6:
                        matrix[i][j] = qs[2]
                    elif i == 3 and j == 7:
                        matrix[i][j] = qs[1]
                    elif i == j:
                        matrix[i][j] = qs[3]
                    elif i == 3 and j == 1:
                        matrix[i][j] = qs[4]
                    elif i - 2 == j:
                        matrix[i][j] = qs[1]
                    elif i - 3 == j:
                        matrix[i][j] = qs[0]
                    else:
                        matrix[i][j] = 'empty'
                else:
                    matrix[i][j] = ''


            except Assign.DoesNotExist:
                pass
            t += 1

    context = {'queryset': qs,
               'matrix': matrix,
               }

    return render(request, 'timetable2.html', context)


def timetable3(request):
    qs = Assign.objects.all()
    # fatch the all data in Course
    title_contains_query = request.GET.get('title_contains')  # that contain the input in search
    print(title_contains_query)
    if title_contains_query != '' and title_contains_query is not None:  # query
        qs = qs.filter(course__course_id__icontains=title_contains_query)
        print(qs)
    matrix = [['' for i in range(8)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(8):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4:  # breake k liye
                continue
            try:
                if title_contains_query != '' and title_contains_query is not None:
                    qs = qs.filter(course__course_id__istartswith=title_contains_query) and qs.filter(
                        course__course_id__icontains='30')
                    if i + 1 == j:  # conditions k sath Course to put kiya ja raha hai
                        matrix[i][j] = qs[3]
                    elif i + 2 == j:
                        matrix[i][j] = qs[2]
                    elif i + 3 == j:
                        matrix[i][j] = qs[1]
                    elif i + 5 == j:
                        matrix[i][j] = qs[4]
                    elif i + 6 == j:
                        matrix[i][j] = qs[0]
                    elif i == j:
                        matrix[i][j] = qs[0]
                    elif i - 1 == j:
                        matrix[i][j] = qs[4]
                    elif i == 3 and j == 7:
                        matrix[i][j] = qs[3]
                    elif i - 3 == j:
                        matrix[i][j] = qs[1]
                    elif i == 5 and j == 1:
                        matrix[i][j] = qs[2]
                    else:
                        matrix[i][j] = 'empty'
                else:
                    matrix[i][j] = ''


            except Assign.DoesNotExist:
                pass
            t += 1

    context = {'queryset': qs,
               'matrix': matrix,
               }

    return render(request, 'timetable3.html', context)


def timetable4(request):
    qs = Assign.objects.all()
    # fatch the all data in Course
    title_contains_query = request.GET.get('title_contains')  # that contain the input in search
    print(title_contains_query)
    if title_contains_query != '' and title_contains_query is not None:  # query
        qs = qs.filter(course__course_id__icontains=title_contains_query)
        print(qs)
    matrix = [['' for i in range(8)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(8):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4:  # breake k liye
                continue
            try:
                if title_contains_query != '' and title_contains_query is not None:
                    qs = qs.filter(course__course_id__istartswith=title_contains_query) and qs.filter(
                        course__course_id__icontains='40')
                    if i + 1 == j:  # conditions k sath Course to put kiya ja raha hai
                        matrix[i][j] = qs[0]
                    elif i + 2 == j:
                        matrix[i][j] = qs[1]
                    elif i + 3 == j:
                        matrix[i][j] = qs[2]
                    elif i + 5 == j:
                        matrix[i][j] = qs[3]
                    elif i + 6 == j:
                        matrix[i][j] = qs[4]
                    elif i == j:
                        matrix[i][j] = qs[4]
                    elif i - 1 == j:
                        matrix[i][j] = qs[3]
                    elif i == 3 and j == 1:
                        matrix[i][j] = qs[0]
                    elif i - 2 == j:
                        matrix[i][j] = qs[2]
                    elif i == 5 and j == 1:
                        matrix[i][j] = qs[1]
                    else:
                        matrix[i][j] = 'empty'
                else:
                    matrix[i][j] = ''


            except Assign.DoesNotExist:
                pass
            t += 1

    context = {'queryset': qs,
               'matrix': matrix,
               }

    return render(request, 'timetable4.html', context)


from django.shortcuts import render

# Create your views here.
