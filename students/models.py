from django.db import models

# Группа
class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Кружки
class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Студент
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    clubs = models.ManyToManyField(Club, blank=True)

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"