from rest_framework import serializers
from .models import Course, Topic, Partnership, Instructor, CoursePage

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id', 'title', 'logo_url']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)
    partnerships = PartnershipSerializer(many=True)
    instructors = InstructorSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

class CoursePageSerializer(serializers.ModelSerializer):
    featured_courses = CourseSerializer(many=True)
    top_rated_courses = CourseSerializer(many=True)

    class Meta:
        model = CoursePage
        fields = ['id', 'title', 'featured_courses', 'top_rated_courses']
