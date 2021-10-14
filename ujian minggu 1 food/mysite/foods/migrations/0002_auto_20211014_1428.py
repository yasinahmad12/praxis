# Generated by Django 3.2.8 on 2021-10-14 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='minum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(default='', max_length=30)),
                ('nama', models.CharField(default='', max_length=30)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='lapar',
            new_name='makan',
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namamakan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makanan', to='foods.makan')),
                ('namaminuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minuman', to='foods.makan')),
            ],
        ),
    ]