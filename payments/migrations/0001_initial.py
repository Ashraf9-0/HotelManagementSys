from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_type', models.CharField(
                    choices=[('Mobile Money', 'Mobile Money'), ('Cash', 'Cash')],
                    max_length=20
                )),
                ('payment_date', models.DateField()),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='payments',
                    to='rooms.room'
                )),
            ],
        ),
    ]
