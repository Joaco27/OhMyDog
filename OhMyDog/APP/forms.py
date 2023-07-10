from .models import *
from django import forms
import datetime as date
from django.core.exceptions import ValidationError 

# Aca creamos los formularios

class Perro_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Perro
        fields = ['nombre','raza','sexo','fechaNacimiento']
    # Creamos los campos del formulario
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    opciones = ['Macho','Hembra']
    fechaNacimiento = forms.DateField(label='Fecha de Nacimiento (si no conoce la fecha ingrese una aproximada)'
                                      ,widget=forms.DateInput(attrs={"type": "date"}))
    sexo = forms.ChoiceField(choices=[(l, l) for l in opciones],required=True)
    # Clean son validaciones 
    # Se debe respetar que en el nombre de la validacion este
    # el nombre del campo , osea clean_<nombre de campo>


    usuario = {
        "nombre": "",
        "esCliente": False,
        "esVeterinario": False,
    }

    def clean_fechaNacimiento(self):
        data =self.cleaned_data["fechaNacimiento"]
        fecha = date.datetime.today()

        data_str = data.strftime('%d/%m/%Y')
        data_nueva = date.datetime.strptime(data_str, '%d/%m/%Y')
        if data_nueva > fecha:
            raise ValidationError("Coloque una fecha valida, inferior a la fecha actual")
        return data
    
    # No le llega el mail haciendo esta validacion, por lo q la hago en las views
    # def clean_nombre(self):
    #     data = self.cleaned_data.get('nombre')
    #     mail = self.data.get('emailDueño')
    #     ok = Perro.objects.filter(nombre=data,emailDueño=mail).exists()
    #     print (ok)
    #     if ok :
    #         raise ValidationError('El nombre del perro ya se encuentra registrado para ese dueño')
    #     return data
    
class Paseador_form(forms.ModelForm):
    class Meta:
        model=Paseador
        fields=['nombre','dni', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    dni = forms.CharField(max_length=8,required=True, label='DNI')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=50, required=True, label='Recorrido')
    lista = ["Mañana", "Mediodia", "Tarde", "Noche"]
    disponibilidad = forms.ChoiceField(choices=[(l, l) for l in lista],required=True, label='Disponibilidad')
    
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
    lista = ['A Domicilio','Direccion Particular','A Eleccion del Cliente']
    zona = forms.ChoiceField(choices=[(l, l) for l in lista],required=True, label="Lugar")
    lista = ["Mañana", "Mediodia", "Tarde", "Noche"]
    disponibilidad = forms.ChoiceField(choices=[(l, l) for l in lista],required=True, label='Disponibilidad') 
       
    def clean_dni(self):
        data=self.cleaned_data["dni"]
        if len(str(data)) < 8:
            raise ValidationError("DNI no aceptado (debe tener 8 nros)")
        ok = Cuidador.objects.filter(dni=data).first()
        if ok is not None:
            raise ValidationError("DNI ya registrado")
        return data
    
class Turnos_form(forms.Form):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Turnos
        fields = ['descripcion','perro','motivo','fecha','fHoraria']
    def __init__(self, *args, **kwargs):#definimos una funcion que tiene self, arfs y kwargs
        opciones = kwargs.pop('opciones', [])#traemos las opciones por kwargs.pop
        super(Turnos_form, self).__init__(*args, **kwargs)#llamamos a super de turnos self 
        self.fields['perro'] = forms.ChoiceField(choices=[(opcion, opcion) for opcion in opciones],required=True) #asignamos un tipo y valor a la field perro

    descripcion = forms.CharField(max_length=50, required=True)
    perro = forms.ChoiceField()
    motivo = forms.ChoiceField(widget=forms.RadioSelect, label='motivo', choices=[('castrar', 'castrar'), ('vacunar', 'vacunar'), ('revision', 'Revision'), ('otro', 'Otro')])
    fecha = forms.DateField( label='Seleccione la fecha de su turno',
                            widget=forms.DateInput(attrs={"type": "date"}))
    fHoraria = forms.ChoiceField(widget=forms.RadioSelect, label='Franja Horaria del Turno', choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde')])
    # Clean son validaciones 
    
    def clean_fecha(self):
        data =self.cleaned_data["fecha"]
        fecha = date.datetime.today()

        data_str = data.strftime('%d/%m/%Y')
        data_nueva = date.datetime.strptime(data_str, '%d/%m/%Y')
        if data_nueva < fecha:
            raise ValidationError("Coloque una fecha valida, superior a la fecha actual")
        return data

class perroAdopcion_form(forms.Form):
    class Meta:
        model= PerroAdopcion
        fields=['nombre','descripcion', 'zona']
    def __init__(self, *args, **kwargs):
        opciones = kwargs.pop('opciones', [])
        super(perroAdopcion_form, self).__init__(*args, **kwargs)
        self.fields['nombre'] = forms.ChoiceField(choices=[(opcion, opcion) for opcion in opciones],required=True)
    
    
    nombre = forms.ChoiceField()
    zona = forms.CharField(max_length=50, required=True, label='zona')
    descripcion= forms.CharField(max_length=30, required=True, label='description')


class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombreC','usuario','contra','mail','telefono']
    nombreC = forms.CharField(max_length=40, required=True, label='Nombre Completo')
    usuario = forms.CharField(max_length=20, required=True, label='Nombre de Usuario')
    contra = forms.CharField(max_length=20, required=True, label='Contraseña',widget=forms.PasswordInput)
    mail = forms.EmailField(max_length=30, required=True, label='Mail')
    telefono = forms.IntegerField(required=True, label='Telefono')
    #onLine = forms.BooleanField(show_hidden_initial=True,widget=forms.HiddenInput(),required=False)
    
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
    

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description']
    
    title = forms.CharField(max_length=30,required=True,label="Veterinaria")
    date = forms.DateField( label='Fecha',
                            widget=forms.DateInput(attrs={"type": "date"}), required=True)
    description = forms.CharField(max_length=30, label="Direccion", required=True)
    
    def clean_data(self):
        fecha =self.cleaned_data["date"]
        hoy = date.datetime.today()

        data_str = fecha.strftime('%d/%m/%Y')
        data_nueva = date.datetime.strptime(data_str, '%d/%m/%Y')
        if data_nueva < hoy:
            raise ValidationError("Coloque una fecha posterior a la fecha actual o actual")
        description = self.cleaned_data["description"]
        title = self.cleaned_data["title"]
        e = Event.objects.filter(title=title, date=fecha,description=description).exists()
        if e:
            raise ValidationError("Ya registraste esta VT")
        return description          


    
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
            raise ValidationError("Coloque una fecha previa a la fecha actual o actual")
        return data
class Historial_form(forms.Form):
    class Meta:
        model = Historial
        fields = '__all__'
    nombreP = forms.CharField(max_length=30,required=False,widget=forms.HiddenInput)
    mailD = forms.EmailField(max_length=30 ,required=False,widget=forms.HiddenInput)
    raza = forms.CharField(max_length=30,required=False,widget=forms.HiddenInput)
    edad = forms.IntegerField(required=False,widget=forms.HiddenInput)
    descripcion = forms.CharField( max_length=400,required=True,
                                   widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    fecha = forms.DateField( label='Fecha Actual',
                            widget=forms.DateInput(attrs={"type": "date"}))
    lista = ['NO','SI']
    castrado = forms.ChoiceField(choices=[(l, l) for l in lista],required=True)
    pulsaciones  = forms.CharField(max_length=30,required=True)
    estudios_complementarios = forms.CharField( max_length=400,required=True, 
                                               widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    diagnostico_presuntivo = forms.CharField( max_length=400,required=True, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    tratamiento = forms.CharField( max_length=400,required=True,
                                   widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    proxima_visita = forms.DateField( label='Proxima Visita',
                            widget=forms.DateInput(attrs={"type": "date"}), required=False)
    
    
    
class Donacion_form(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = '__all__'
    causa = forms.CharField(max_length=30, required=True)
    descripcion = forms.CharField( max_length=400,required=True,
                                   widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    objetivo = forms.IntegerField(required=True, label='Objetivo $')
    recaudado = forms.IntegerField(required=False, widget=forms.HiddenInput, initial=0)
    
class Tarjeta_form(forms.Form):
    nombre = forms.CharField(max_length=40, required=True, label="Titular de la Tarjeta")
    numero = forms.IntegerField(required=True)
    mesV = forms.IntegerField(required=True, label="Mes Vencimiento")
    añoV = forms.IntegerField(required=True, label="Año Vencimiento")
    codigo = forms.IntegerField(required=True, label="Codigo de Seguridad")
    monto = forms.IntegerField(required=True)
    
    def clean(self):
        numero = self.cleaned_data['numero']
        ok = Tarjeta.objects.filter(numero=numero).exists()
        if not ok:
            raise ValidationError('Nro de tarjeta incorrecto')  
          
        data = self.cleaned_data['nombre']
        ok = Tarjeta.objects.filter(nombre=data).exists()
        if not ok:
            raise ValidationError('La tarjeta no corresponde a ese dueño') 
           
        data = self.cleaned_data['mesV']
        ok = Tarjeta.objects.filter(numero=numero, mesV=data).exists()
        if not ok:
            raise ValidationError('Revise la fecha de vencimiento')  
          
        data = self.cleaned_data['añoV']
        ok = Tarjeta.objects.filter(numero=numero, añoV=data).exists()
        if not ok:
            raise ValidationError('Revise la fecha de vencimiento')
        
        data = self.cleaned_data['codigo']
        ok = Tarjeta.objects.filter(numero=numero, codigo=data).exists()
        if not ok:
            raise ValidationError('Codigo de seguridad incorrecto')
    
        data = self.cleaned_data['monto']
        t = Tarjeta.objects.get(numero=numero)
        if t.saldo-data < 0:
            raise ValidationError('Saldo Insuficiente')
        return data, numero
#hola
    
