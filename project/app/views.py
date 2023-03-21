import django_filters

from app.serializers import UniversitySerializer, DepartmentSerializer, AddressSerializer, TeacherSerializer
from app.models import University, Department, Address, Teacher
from rest_framework import viewsets
from app.filters import TeacherFilterBackend


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def perform_create(self, serializer):
        address_data = self.request.data.get('address')
        print(address_data)
        univer_name = self.request.data.get('name')
        a = Address.objects.create(**address_data)
        print(a)
        univer = University.objects.create(address=a, name=univer_name)
        return univer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # filter_backends = (django_filters.FilterSet,)
    filter_class = TeacherFilterBackend

    def perform_create(self, serializer):
        department = self.request.data.pop('department_name')
        name = self.request.data.get('name')
        surname = self.request.data.get('surname')
        surname2 = self.request.data.get('surname2')
        birth = self.request.data.get('birth')
        a = Department.objects.create(name=department)
        teacher = Teacher.objects.create(department=a, name=name, surname=surname, surname2=surname2,
                                         birth=birth)
        return teacher

