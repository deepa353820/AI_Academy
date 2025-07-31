from django.db import models
import uuid

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Partnership(models.Model):
    title = models.CharField(max_length=255)
    logo_url = models.URLField()

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    course_type = models.CharField(max_length=50)  # 'Short Course', 'Course', 'Specialization'
    skill_level = models.CharField(max_length=50)  # 'Beginner', 'Intermediate'
    featured_image = models.URLField()
    landing_page = models.URLField()
    topics = models.ManyToManyField(Topic, related_name='courses')
    partnerships = models.ManyToManyField(Partnership, related_name='courses')
    instructors = models.ManyToManyField(Instructor, related_name='courses')

    def __str__(self):
        return self.title

class CoursePage(models.Model):
    title = models.CharField(max_length=255)
    featured_courses = models.ManyToManyField(Course, related_name='featured_in_pages')
    top_rated_courses = models.ManyToManyField(Course, related_name='top_rated_in_pages')

    def __str__(self):
        return self.title
