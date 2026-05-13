from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})


from .models import Student, Group

def add_student(request):
    groups = Group.objects.all()

    if request.method == "POST":
        group_id = request.POST.get("group")
        group = Group.objects.get(id=group_id)

        Student.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            age=request.POST.get("age"),
            group=group,
            photo=request.FILES.get("photo")
        )
        return redirect("student_list")

    return render(request, "students/add_student.html", {"groups": groups})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Student

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "students/register.html", {"form": form})

from .models import Student, Group
from django.shortcuts import render, redirect

def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    groups = Group.objects.all()

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.age = request.POST.get("age")

        group_id = request.POST.get("group")
        student.group = Group.objects.get(id=group_id)

        if request.FILES.get("photo"):
            student.photo = request.FILES.get("photo")

        student.save()
        return redirect("student_list")

    return render(request, "students/edit_student.html", {
        "student": student,
        "groups": groups
    })

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect("student_list")

def student_list(request):
    query = request.GET.get("q")

    if query:
        students = Student.objects.filter(last_name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, "students/index.html", {"students": students})

def student_list(request):
    group_id = request.GET.get("group")

    students = Student.objects.all()
    groups = Group.objects.all()

    if group_id:
        students = students.filter(group_id=group_id)

    return render(request, "students/index.html", {
        "students": students,
        "groups": groups
    })

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, "students/detail.html", {"student": student})