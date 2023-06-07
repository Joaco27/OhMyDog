from .models import *
from django import forms
import datetime as date
from django.core.exceptions import ValidationError 

# Aca creamos los formularios

class Perro_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Perro
        fields = ['nombre','raza', 'edad']
    # Creamos los campos del formulario
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')

    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data
    
    def clean_emailDueño(self):
        data = self.cleaned_data.get('emailDueño')
        ok = Cliente.objects.filter(mail=data).exists()
        if not ok :
            raise ValidationError('El email no pertenece a un dueño')
        return data
    def clean_nombre(self):
        data = self.cleaned_data.get('nombre')
        mail = self.data.get('emailDueño')
        ok = Perro.objects.filter(nombre=data,emailDueño=mail).exists
        print (ok)
        if ok :
            raise ValidationError('El nombre del perro ya se encuentra registrado para ese dueño')
        return data
class Paseador_form(forms.ModelForm):
    class Meta:
        model=Paseador
        fields=['nombre','dni', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    dni = forms.CharField(max_length=8,required=True, label='DNI')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_dni(self):
        data=self.cleaned_data["dni"]
        if len(str(data)) < 8:
            raise ValidationError("DNI no aceptado (debe tener 8 nros)")
        ok = Paseador.objects.filter(dni=data).first()
        if ok is not None:
            raise ValidationError("DNI ya registrado")
        return data
    
class Cuidador_form(forms.ModelForm):
    class Meta:
        model=Cuidador
        fields=['nombre','dni', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    dni = forms.CharField(max_length=8,required=True, label='DNI')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_dni(self):
        data=self.cleaned_data["dni"]
        if len(str(data)) < 8:
            raise ValidationError("DNI no aceptado (debe tener 8 nros)")
        ok = Cuidador.objects.filter(dni=data).first()
        if ok is not None:
            raise ValidationError("DNI ya registrado")
        return data
    
class Turnos_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Turnos
        fields = ['descripcion','raza', 'edad','nombre','perro','motivo','fecha']
    #intentamos inicializar el form antes

    #creamos las choices para perros
    choice=[]
    if Cliente.objects.filter(onLine=True).exists() :
        usr=Cliente.objects.get(onLine=True)
        for i in Perro.objects.filter(nombreD=usr.usuario):
            choice.append((i,i))
    # Creamos los campos del formulario
    descripcion = forms.Textarea()
    nombre = forms.CharField(max_length=15, label='Nombre',widget=forms.HiddenInput,required=False) #hay que sacarlo
    raza = forms.CharField(max_length=15, label='Raza',widget=forms.HiddenInput,required=False) #fuera
    edad = forms.IntegerField(label='Edad',widget=forms.HiddenInput,required=False) #fuera
    perro = forms.ChoiceField(widget= forms.RadioSelect,label='Seleccion su perro',choices=choice)
    motivo = forms.ChoiceField(widget=forms.RadioSelect, label='motivo', choices=[('castrar', 'castrar'), ('vacunar', 'vacunar'), ('revision', 'Revision'), ('otro', 'Otro')])
    fecha = forms.DateField( label='Seleccione la fecha de su turno',
                            widget=forms.DateInput(attrs={"type": "date"}))
    # Clean son validaciones 
    
    def clean_fecha(self):
        data =self.cleaned_data["fecha"]
        fecha = date.datetime.today()

        data_str = data.strftime('%d/%m/%Y')
        data_nueva = date.datetime.strptime(data_str, '%d/%m/%Y')
        if data_nueva < fecha:
            raise ValidationError("Coloque una fecha valida, superior a la fecha actual")
        return data
    
class perroAdopcion_form(forms.ModelForm):
    class Meta:
        model= PerroAdopcion
        fields=['usuario','nombre', 'peso', 'raza', 'descripcion', 'zona', 'castrado']

    usuario= forms.CharField(max_length=30, required=True, label='usuario')
    nombre = forms.CharField(max_length=50, required=True, label='nombre')
    peso = forms.IntegerField(required=True, label='peso')
    #edad = forms.IntegerField(required=True, label='edad')
    zona = forms.CharField(max_length=50, required=True, label='zona')
    raza= forms.CharField(max_length=20, required=True, label='raza')
    descripcion= forms.CharField(max_length=30, required=True, label='description')
    castrado= forms.CharField(max_length=2,required=True, label='castrado')

    def clean_usuario(self):
        data = self.cleaned_data["usuario"]
        ok = Cliente.objects.filter(usuario=data).exists()
        if ok==False:
            raise ValidationError('nombre de usuario no registrado')
        return data
    
class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombreC','usuario','contra','mail','telefono','onLine']
    nombreC = forms.CharField(max_length=40, required=True, label='Nombre Completo')
    usuario = forms.CharField(max_length=20, required=True, label='Nombre de Usuario')
    contra = forms.CharField(max_length=20, required=True, label='Contraseña',widget=forms.PasswordInput)
    mail = forms.EmailField(max_length=30, required=True, label='Mail')
    telefono = forms.IntegerField(required=True, label='Telefono')
    onLine = forms.BooleanField(show_hidden_initial=True,widget=forms.HiddenInput(),required=False)
    
    def clean_usuario(self):
        data = self.cleaned_data["usuario"]
        ok = Cliente.objects.filter(usuario=data).exists()
        if ok==True:
            raise ValidationError('Usuario Ya Registrado')
        return data
    
    def clean_telefono(self):
        data = self.cleaned_data["telefono"]
        ok = Cliente.objects.filter(telefono=data).exists()
        if ok==True:
            raise ValidationError('Telefono Ya Registrado')
        return data
    
    def clean_mail(self):
        data = self.cleaned_data["mail"]
        ok = Cliente.objects.filter(mail=data).exists()
        if ok==True:
            raise ValidationError('Mail Ya Registrado')
        return data

    
class LogIn_form(forms.Form):
    usuario = forms.CharField(max_length=30, required=True, label='Nombre de Usuario')
    contra = forms.CharField(max_length=30, required=True, label='Contraseña',widget=forms.PasswordInput)
    
    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        user = Cliente.objects.filter(usuario=usuario).first()
        if user is None:
            raise ValidationError('Nombre de usuario o contraseña incorrecta')
        return usuario
    
    def clean_contra(self):
        password = self.cleaned_data['contra']
        username = self.cleaned_data.get('usuario')
        if username:
            user = Cliente.objects.filter(usuario=username).first()
            if user is not None and not user.contra==password:
                raise forms.ValidationError('Nombre de usuario o contraseña incorrecta')
        return password
    
class contacto_form(forms.Form):
    usuario = forms.CharField(max_length=40, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True, label='Telefono')
            
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7 or len(str(data)) > 11:
            raise ValidationError("El telefono debe tener entre 7 y 11 caracters")
        return data
    
class perroPerdido_form(forms.Form):
    class Meta:
        model = PerroPerdido
        fields = ['nombre', 'descripcion', 'zona', 'fechaD','imagen']
    def __init__(self, *args, **kwargs):
        opciones = kwargs.pop('opciones', [])
        super(perroPerdido_form, self).__init__(*args, **kwargs)
        self.fields['nombre'] = forms.ChoiceField(choices=[(opcion, opcion) for opcion in opciones],required=True)
       
    
    nombre = forms.ChoiceField()
    descripcion = forms.CharField(max_length=200, required=True, label='Descripcion', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    fechaD = forms.DateField(initial=date.date.today(), required = True, label='Fecha de Desaparicion',
                            widget=forms.DateInput(attrs={"type": "date"}))
    imagen = forms.ImageField(required=True, label="Imagen", widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    def clean_fechaD(self):
        data =self.cleaned_data["fechaD"]
        fecha = date.datetime.today()

        data_str = data.strftime('%d/%m/%Y')
        data_nueva = date.datetime.strptime(data_str, '%d/%m/%Y')
        if data_nueva > fecha:
            raise ValidationError("Coloque una fecha previa a la fecha actual")
        return data
