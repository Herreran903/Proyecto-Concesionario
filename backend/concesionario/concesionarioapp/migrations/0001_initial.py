# Generated by Django 4.2.6 on 2023-11-01 00:28

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
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Género')),
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
            name='Carro',
            fields=[
                ('vin', models.CharField(max_length=17, primary_key=True, serialize=False, unique=True, verbose_name='VIN')),
                ('disponible_para_venta', models.BooleanField(default=True, verbose_name='Disponible para Venta')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
                'ordering': ['vin'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Color')),
                ('nombre_color', models.CharField(max_length=30, unique=True, verbose_name='Nombre del Color')),
                ('porcentanje_incremento_por_color', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Porcentaje de Incremento por Color')),
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
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Porcentaje de Descuento')),
                ('fecha_vencimiento', models.DateField(default=datetime.datetime(2023, 11, 20, 19, 28, 14, 464887), verbose_name='Fecha de Vencimiento')),
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
            name='InventarioRepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad de Repuestos en Inventario')),
            ],
            options={
                'verbose_name': 'Inventario de Repuesto',
                'verbose_name_plural': 'Inventarios de Repuestos',
                'ordering': ['sucursal__nombre_sucursal', 'repuesto__nombre_repuesto'],
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Modelo')),
                ('nombre_modelo', models.CharField(max_length=30, unique=True, verbose_name='Nombre del Modelo')),
                ('anho_modelo', models.IntegerField(blank=True, null=True, verbose_name='Año del Modelo')),
                ('carroceria', models.CharField(blank=True, max_length=30, null=True, verbose_name='Carrocería')),
                ('cilindraje', models.IntegerField(blank=True, null=True, verbose_name='Cilindraje')),
                ('potencia', models.IntegerField(blank=True, null=True, verbose_name='Potencia')),
                ('combustible', models.CharField(blank=True, choices=[('G', 'Gasolina'), ('D', 'Diesel'), ('E', 'Eléctrico'), ('H', 'Híbrido')], max_length=1, null=True, verbose_name='Combustible')),
                ('numero_pasajeros', models.IntegerField(blank=True, null=True, verbose_name='Número de Pasajeros')),
                ('precio_base', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Base')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'ordering': ['nombre_modelo'],
            },
        ),
        migrations.CreateModel(
            name='Orden_Trabajo',
            fields=[
                ('id_orden_trabajo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Orden de Trabajo')),
                ('placa_carro', models.CharField(blank=True, max_length=6, null=True, verbose_name='Placa del Carro')),
                ('comentarios_estado_carro', models.CharField(blank=True, max_length=300, null=True, verbose_name='Comentarios del Estado del Carro')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_entrega_esperada', models.DateField(default=datetime.datetime(2023, 11, 20, 19, 28, 14, 463890), verbose_name='Fecha de Entrega Esperada')),
                ('fecha_entrega_real', models.DateField(blank=True, null=True, verbose_name='Fecha de Entrega Real')),
                ('estado_reparacion', models.CharField(choices=[('P', 'En Proceso'), ('R', 'Retrasada'), ('E', 'A la espera de repuestos'), ('F', 'Finalizada')], default='P', max_length=1, verbose_name='Estado de la Reparación')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.modelo', verbose_name='Modelo')),
            ],
            options={
                'verbose_name': 'Orden de Trabajo',
                'verbose_name_plural': 'Ordenes de Trabajo',
                'ordering': ['id_orden_trabajo'],
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
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Venta')),
                ('fecha_venta', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
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
                ('cargo', models.CharField(choices=[('A', 'Administrador'), ('V', 'Vendedor'), ('J', 'Jefe de taller')], max_length=1, verbose_name='Cargo')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.sucursal', verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['usuario__primer_apellido', 'usuario__primer_nombre'],
            },
        ),
        migrations.CreateModel(
            name='Venta_Carro',
            fields=[
                ('id_venta_carro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Venta del Carro')),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Porcentaje de Descuento')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.carro', verbose_name='Carro')),
                ('extras', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.extra', verbose_name='Extras')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionarioapp.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Carro en la Venta',
                'verbose_name_plural': 'Carros en la Venta',
                'ordering': ['id_venta_carro'],
            },
        ),
        migrations.AddField(
            model_name='venta',
            name='carros',
            field=models.ManyToManyField(through='concesionarioapp.Venta_Carro', to='concesionarioapp.carro', verbose_name='Carros'),
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id_trabajo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Trabajo')),
                ('descripcion_trabajo', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción del Trabajo')),
                ('precio_trabajo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del Trabajo')),
                ('orden_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionarioapp.orden_trabajo', verbose_name='Orden de Trabajo')),
            ],
            options={
                'verbose_name': 'Trabajo en la Orden de Trabajo',
                'verbose_name_plural': 'Trabajos en la Orden de Trabajo',
                'ordering': ['id_trabajo'],
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id_repuesto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Repuesto')),
                ('nombre_repuesto', models.CharField(max_length=30, unique=True, verbose_name='Nombre del Repuesto')),
                ('precio_repuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio del Repuesto')),
                ('descrpcion_repuesto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción del Repuesto')),
                ('modelos', models.ManyToManyField(to='concesionarioapp.modelo', verbose_name='Modelos que pueden usar este repuesto')),
                ('sucursales', models.ManyToManyField(through='concesionarioapp.InventarioRepuesto', to='concesionarioapp.sucursal', verbose_name='Sucursales que tienen este repuesto')),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
                'ordering': ['nombre_repuesto'],
            },
        ),
        migrations.AddField(
            model_name='orden_trabajo',
            name='repuestos_en_orden_trabajo',
            field=models.ManyToManyField(to='concesionarioapp.repuesto', verbose_name='Repuestos en la Orden de Trabajo'),
        ),
        migrations.AddField(
            model_name='inventariorepuesto',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.repuesto', verbose_name='Repuesto'),
        ),
        migrations.AddField(
            model_name='inventariorepuesto',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.sucursal', verbose_name='Sucursal'),
        ),
        migrations.CreateModel(
            name='Cotizacion_Modelo',
            fields=[
                ('id_cotizacion_modelo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Cotización del Modelo')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.color', verbose_name='Color')),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concesionarioapp.cotizacion', verbose_name='Cotización')),
                ('extras', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.extra', verbose_name='Extras')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.modelo', verbose_name='Modelo')),
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
            field=models.ManyToManyField(through='concesionarioapp.Cotizacion_Modelo', to='concesionarioapp.modelo', verbose_name='Modelos'),
        ),
        migrations.AddField(
            model_name='carro',
            name='color_carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.color', verbose_name='Color del Carro'),
        ),
        migrations.AddField(
            model_name='carro',
            name='modelo_carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.modelo', verbose_name='Modelo del Carro'),
        ),
        migrations.AddField(
            model_name='carro',
            name='sucursal_carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.sucursal', verbose_name='Sucursal del Carro'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.empleado', verbose_name='Vendedor'),
        ),
        migrations.AddField(
            model_name='orden_trabajo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='orden_trabajo',
            name='jefe_taller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.empleado', verbose_name='Jefe de Taller'),
        ),
        migrations.AlterUniqueTogether(
            name='inventariorepuesto',
            unique_together={('sucursal', 'repuesto')},
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concesionarioapp.empleado', verbose_name='Vendedor'),
        ),
    ]
