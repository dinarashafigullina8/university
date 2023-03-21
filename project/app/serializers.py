from django.db.models import Count
from django.forms import model_to_dict
from rest_framework import serializers
from django.http import JsonResponse

from app.models import University, Address, Department, Teacher


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'street', 'house')


class UniversitySerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = University
        fields = ('name', 'address')


class DepartmentSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Department
        fields = ('number', 'name')

    def get_number(self, obj: Department):
        return Teacher.objects.filter(department=obj).count()


class TeacherSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_name = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = ('name', 'surname', 'surname2', 'birth', 'department', 'department_name')

    def create(self, validated_data):
        numbers_data = validated_data.pop('department')
        a = Department.objects.create(**numbers_data)
        teacher = Teacher.objects.create(department=a, **validated_data)
        return teacher
