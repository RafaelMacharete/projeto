# Generated by Django 5.1 on 2024-11-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_categoriaproduto_produto_catproduto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='classProduto',
            field=models.CharField(max_length=255),
        ),
    ]
