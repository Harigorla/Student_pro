from django.forms import ModelForm
from .models import StudentRegister, StudentApply, StudentList


class StudentForm(ModelForm):
    class Meta:
        model = StudentRegister
        fields = "__all__"


class StudentApplyForm(ModelForm):
    class Meta:
        model = StudentApply
        fields = "__all__"


class StudentListForm(ModelForm):
    class Meta:
        model = StudentList
        fields = "__all__"
