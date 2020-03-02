# Generated by Django 2.2.3 on 2019-07-18 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('is_main', models.BooleanField()),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('cathegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('start', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(through='shop.ItemInOrder', to='shop.Item')),
            ],
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order'),
        ),
        migrations.CreateModel(
            name='ItemInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Basket')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(through='shop.ItemInBasket', to='shop.Item'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('items', models.ManyToManyField(related_name='articles', to='shop.Item')),
            ],
        ),
    ]
