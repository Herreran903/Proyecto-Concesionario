# Generated by Django 4.2.6 on 2023-12-08 20:19

import concesionarioapp.managers
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cedula', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Cédula')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('primer_nombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('segundo_nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Nombre')),
                ('primer_apellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('segundo_apellido', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Apellido')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección')),
                ('ciudad', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ciudad')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], null=True, verbose_name='Género')),
                ('is_active', models.BooleanField(default=True, verbose_name='Usuario activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuario parte del staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Usuario es superusuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['primer_apellido', 'primer_nombre'],
            },
            managers=[
                ('objects', concesionarioapp.managers.AdministradorUsuarios()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Color')),
                ('nombre_color', models.CharField(max_length=30, unique=True, verbose_name='Nombre del Color')),
                ('hexadecimal_color', models.CharField(max_length=7, unique=True, verbose_name='Hexadecimal del Color')),
                ('porcentaje_incremento_por_color', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Porcentaje de Incremento por Color')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colores',
                'ordering': ['nombre_color'],
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id_cotizacion', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Cotización')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de Creación')),
                ('fecha_vencimiento', models.DateField(default=datetime.date(2023, 12, 28), verbose_name='Fecha de Vencimiento')),
            ],
            options={
                'verbose_name': 'Cotización',
                'verbose_name_plural': 'Cotizaciones',
                'ordering': ['id_cotizacion'],
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id_extra', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Extra')),
                ('nombre_extra', models.CharField(max_length=30, unique=True, verbose_name='Nombre del Extra')),
                ('descripcion_extra', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción del Extra')),
            ],
            options={
                'verbose_name': 'Extra',
                'verbose_name_plural': 'Extras',
                'ordering': ['nombre_extra'],
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Modelo')),
                ('nombre_modelo', models.CharField(max_length=60, unique=True, verbose_name='Nombre del Modelo')),
                ('anho', models.IntegerField(verbose_name='Año del Modelo')),
                ('carroceria', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Station Wagon', 'Station Wagon'), ('Pickup', 'Pickup'), ('SUV', 'SUV'), ('Van', 'Van'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Roadster', 'Roadster'), ('Camion', 'Camion'), ('Camioneta', 'Camioneta'), ('Bus', 'Bus'), ('Minivan', 'Minivan'), ('Microbus', 'Microbus'), ('Micro', 'Micro'), ('Tracto Camion', 'Tracto Camion'), ('Trailer', 'Trailer')], null=True, verbose_name='Carrocería')),
                ('cilindraje', models.IntegerField(verbose_name='Cilindraje')),
                ('potencia', models.IntegerField(verbose_name='Potencia')),
                ('combustible', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Electrico', 'Electrico'), ('Hibrido', 'Hibrido'), ('Gas', 'Gas'), ('Gas Natural', 'Gas Natural'), ('Gas Licuado', 'Gas licuado')], verbose_name='Combustible')),
                ('numero_pasajeros', models.IntegerField(verbose_name='Número de Pasajeros')),
                ('precio_base', models.IntegerField(verbose_name='Precio Base')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'ordering': ['id_modelo'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Sucursal')),
                ('nombre_sucursal', models.CharField(max_length=30, unique=True, verbose_name='Nombre de la Sucursal')),
                ('direccion_sucursal', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección de la Sucursal')),
                ('ciudad_sucursal', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ciudad de la Sucursal')),
                ('telefono_sucursal', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono de la Sucursal')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['nombre_sucursal'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False, unique=True, verbose_name='VIN')),
                ('disponible_para_venta', models.BooleanField(default=True, verbose_name='Disponible para Venta')),
                ('color_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.color')),
                ('modelo_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.modelo')),
                ('sucursal_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.sucursal')),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
                'ordering': ['vin'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Venta')),
                ('fecha_venta', models.DateField(verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id_venta'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['usuario__primer_apellido', 'usuario__primer_nombre'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_ingreso', models.DateField(blank=True, null=True, verbose_name='Fecha de Ingreso')),
                ('fecha_retiro', models.DateField(blank=True, null=True, verbose_name='Fecha de Retiro')),
                ('salario_base', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Salario')),
                ('tipo_sangre', models.CharField(blank=True, max_length=3, null=True, verbose_name='Tipo de Sangre')),
                ('eps', models.CharField(blank=True, max_length=30, null=True, verbose_name='EPS')),
                ('arl', models.CharField(blank=True, max_length=30, null=True, verbose_name='ARL')),
                ('cargo', models.CharField(choices=[('Gerente', 'Gerente'), ('Vendedor', 'Vendedor'), ('Jefe de Taller', 'Jefe de taller')], verbose_name='Cargo')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.sucursal')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['usuario__primer_apellido', 'usuario__primer_nombre'],
            },
        ),
        migrations.CreateModel(
            name='Venta_Vehiculo',
            fields=[
                ('id_venta_vehiculo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Venta del Vehiculo')),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Porcentaje de Descuento')),
                ('extra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.extra')),
                ('vehiculo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.vehiculo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionarioapp.venta')),
            ],
            options={
                'verbose_name': 'Vehículo en la Venta',
                'verbose_name_plural': 'Vehículos en la Venta',
                'ordering': ['id_venta_vehiculo'],
            },
        ),
        migrations.CreateModel(
            name='Cotizacion_Modelo',
            fields=[
                ('id_cotizacion_modelo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Cotización del Modelo')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.color')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionarioapp.cotizacion')),
                ('extra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.extra')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.modelo')),
            ],
            options={
                'verbose_name': 'Modelo en la Cotización',
                'verbose_name_plural': 'Modelos en la Cotización',
                'ordering': ['id_cotizacion_modelo'],
            },
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='modelos',
            field=models.ManyToManyField(through='concesionarioapp.Cotizacion_Modelo', to='concesionarioapp.modelo'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.empleado'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.cliente'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.empleado'),
        ),
    ]
