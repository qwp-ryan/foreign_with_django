from django import forms
from .choices import *
from .models import * #Page, Category, UserProfile
#from .models import PassportInformation, VisaInformation
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = 128,
                           help_text = "Please enter the category name.")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget = forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, help_text = "Please enter the title of the page.")
    url = forms.URLField(max_length = 200, help_text = "Please enter the URL of the page.")
    views = forms.IntegerField(widget = forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    def clean(self):
        cleaned_data=self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://'+url
            cleaned_data['url']=url

            return cleaned_data

    class Meta:
        model = Page
        exclude=('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website','picture')

#  我们自己的外事系统的forms
#

class PersonalInformationForm(forms.ModelForm):
    name = forms.CharField(help_text='姓名', max_length=10 ) #目标是自动把登录人填入
    tel = forms.CharField(max_length=12, help_text='电话')
    email = forms.EmailField(help_text='邮箱')
    gender = forms.ChoiceField(help_text='性别', choices=GENDER_CHOICES)
    department = forms.CharField(help_text='所在部门', max_length=30)
    ID_num = forms.CharField(help_text='18位身份证号', max_length=18)
    Place_of_Birth = forms.ChoiceField(help_text='出生地（省）', choices=PLACE_CHOICES)
    Date_of_Birth = forms.DateField(help_text='出生日期 YYYY-MM-DD')
    duty = forms.ChoiceField(help_text='职务', choices=duty_choices)
    identity = forms.ChoiceField(help_text='对外身份', choices=identity_choices)
    race = forms.ChoiceField(help_text='民族', choices=race_choices)
    political_identity = forms.ChoiceField(help_text='政治面貌', choices=political_choices)
    securety = forms.ChoiceField(help_text='涉密等级', choices=securety_choices)
    status_health = forms.ChoiceField(help_text='健康状况', choices=health_choices)
    emergency_contact_name = forms.CharField(help_text='紧急联系人姓名', max_length=10)
    emergency_contact_tel = forms.CharField(help_text='紧急联系人电话', max_length=11)

    class Meta:
        model=PersonalInformation
        fields=('name',
                'tel',
                'email',
                'gender',
                'department',
                'ID_num',
                'Place_of_Birth',
                'Date_of_Birth',
                'duty',
                'identity',
                'race',
                'political_identity',
                'securety',
                'status_health',
                'emergency_contact_name',
                'emergency_contact_tel')






class PassportInformationForm(forms.ModelForm):
    Passport_number = forms.CharField(help_text='护照号码', max_length=15)
    date_issue = forms.DateField(help_text='颁发日期')
    date_expire = forms.DateField(help_text='过期日期')
    issue_office = forms.CharField(help_text='发证机关', max_length=15)
    issue_place = forms.CharField(help_text='发证地点', max_length=15)
    date_out = forms.DateField(help_text='借出日期')
    date_back = forms.DateField(help_text='归还日期')

    class Meta:
        model = PassportInformation
        exclude = ('person',)


class VisaInformationForm(forms.ModelForm):
    # visa_choices = (
    #     ('A', '一次入境签证'),
    #     ('B', '多次入境签证'),
    # )
    country = forms.CharField(label='国家', max_length=20)
    issue_date = forms.DateField(label='颁发日期')
    expire_date = forms.DateField(label='过期日期')
    visa_class = forms.ChoiceField(label='签证类型', choices=visa_choices)
    visa_file = forms.FileField(label='签证扫描件')
