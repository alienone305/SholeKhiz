from django import forms
from cooperation.models import JobOpportunityModel, ApplicationModel, DelegationRequestModel, RepairManRequestModel

class JobOpportunityForm(forms.ModelForm):
    class Meta():
        model = JobOpportunityModel
        fields = ('job_title','required_skills','descriprion',)
        widgets = {
            'job_title': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'عنوان موقعیت شغلی'},),
            'required_skills': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'مهارت های مورد نیاز'},),
            'descriprion': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات شغلی'},),
        }


class DelegationRequestForm(forms.ModelForm):
    class Meta():
        model = DelegationRequestModel
        fields = ('name','last_name','email','age',
                'province','city','phone_number','cellphone_number','address',
                'area','for_towerdryer','for_package','for_radiator','for_waterheater',
                'has_reservoir','fax_number','sell_prediction_towerdryer','sell_prediction_package',
                'sell_prediction_radiator','sell_prediction_waterheater','attendance','description',
                'ownership_type',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام'},),
            'last_name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام خانوادگی'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'ایمیل'},),
            'age': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'سن'},),
            'province': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'استان'},),
            'city': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شهر'},),
            'phone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن ثابت'},),
            'cellphone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن همراه'},),
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'آدرس'},),
            'area': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'متراژ'},),
            'for_towerdryer': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_package': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_radiator': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_waterheater': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'has_reservoir': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'fax_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن فکس'},),
            'sell_prediction_towerdryer': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'پیش بینی از فروش حوله خشک کن'},),
            'sell_prediction_package': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'پیش بینی از فروش پکیج'},),
            'sell_prediction_radiator': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'پیش بینی از فروش رادیاتور'},),
            'sell_prediction_waterheater': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'پیش بینی از فروش آبگرمکن'},),
            'attendance': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'سابقه کاری'},),
            'ownership_type': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نوع مالکیت ملک'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات دیگر'},),
        }


class ApplicationForm(forms.ModelForm):
    class Meta():
        model = ApplicationModel

        fields = ('name','last_name','email','id_number','age',
                'is_man','is_single','phone_number','cellphone_number','address',
                'college_evidence','field_of_study','college_score','name_of_college','english_mastery',
                'computer_mastery','job_attendance','descriprion','resome',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام'},),
            'last_name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام خانوادگی'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'ایمیل'},),
            'id_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره شناسنامه یا کد ملی'},),
            'age': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'سن'},),
            'is_man': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),

            'is_single': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan'},),
            'phone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن ثابت'},),
            'cellphone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن همراه'},),
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'آدرس'},),
            'college_evidence': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'آخرین مدرک دانشگاهی'},),
            'field_of_study': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'رشته تحصیلی'},),
            'college_score': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نمره ی تحصیلی'},),
            'name_of_college': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام دانشگاه تحصیل'},),
            'english_mastery': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'میزان تسلط بر زبان انگلیسی'},),
            'computer_mastery': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'میزان تسلط بر کامپیوتر'},),
            'job_attendance': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'سوابق کاری'},),
            'descriprion': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات دیگر'},),
            'resome': forms.FileInput(attrs={'class':'fHarmattan','id':'resome','help_text':'رزومه'},),

        }



class RepairManRequestForm(forms.ModelForm):
    class Meta():
        model = RepairManRequestModel

        fields = ('name','last_name','age','province','city',
                'is_single','phone_number','cellphone_number','address',
                'for_towerdryer','for_package','for_radiator','for_waterheater',
                'college_evidence','field_of_study','college_score','name_of_college',
                'has_office','can_travel','attendance','experience',
                'certificates','description',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام'},),
            'last_name': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام خانوادگی'},),
            'age': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'سن'},),
            'province': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'استان'},),
            'city': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شهر'},),
            'is_single': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan'},),
            'phone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن ثابت'},),
            'cellphone_number': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'شماره تلفن همراه'},),
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'آدرس'},),
            'for_towerdryer': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_package': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_radiator': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'for_waterheater': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),

            'college_evidence': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'آخرین مدرک دانشگاهی'},),
            'field_of_study': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'رشته تحصیلی'},),
            'college_score': forms.NumberInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نمره ی تحصیلی'},),
            'name_of_college': forms.TextInput(attrs={'class':'uk-input fHarmattan redC-text','placeholder':'نام دانشگاه تحصیل'},),
            'has_office': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'can_travel': forms.CheckboxInput(attrs={'class':'uk-checkbox fHarmattan '},),
            'attendance': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'سوابق کاری'},),
            'experience': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'تجربیات'},),
            'certificates': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'گواهی ها'},),
            'description': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'4','placeholder':'توضیحات دیگر'},),        }
