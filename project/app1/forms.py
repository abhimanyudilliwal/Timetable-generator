from django import forms

from .models import Dept, Teachers,Class,Courses,Assign


class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ('dept_id', 'dept_name',)
        widgets = {
            'Dept_id': forms.TextInput(attrs={'class': 'main'}),
            'Dept_name': forms.TextInput(attrs={'class': 'main'}),

        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('teacher_id', 'teacher_name','Dept')
        widgets={
            'teacher_id':forms.TextInput(attrs={'class':'main'}),
            'teacher_name': forms.TextInput(attrs={'class': 'main'}),
            'Dept': forms.Select(attrs={'class': 'option'})
        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('program_id', 'program_name', 'Dept')
        widgets = {
            'program_id': forms.TextInput(attrs={'class': 'main'}),
            'program_name': forms.TextInput(attrs={'class': 'main'}),
            'Dept': forms.Select(attrs={'class': 'option'})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('course_id', 'course_name', 'program')
        widgets = {
            'course_id': forms.TextInput(attrs={'class': 'main'}),
            'course_name': forms.TextInput(attrs={'class': 'main'}),
            'program': forms.Select(attrs={'class': 'option'})
        }


class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ('course', 'teacher',)
        widgets = {
            'course': forms.TextInput(attrs={'class': 'main'}),
            'teacher': forms.TextInput(attrs={'class': 'main'}),

        }