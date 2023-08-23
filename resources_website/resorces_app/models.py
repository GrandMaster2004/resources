from django.db import models

# Create your models here.
class AddBranch(models.Model):
    branch_name = models.CharField(max_length=30)
    branch_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='branch_images')


class pyq(models.Model):
    branch_name = models.CharField(max_length=30)
    pyq_id = models.AutoField(primary_key=True)
    pyq_details = models.CharField(max_length=300)
    pyq_Image = models.ImageField(upload_to='pyq_images')
    pyq_title = models.CharField(max_length=30)
    year = models.CharField(max_length=20)
    student_year = models.CharField(max_length=1)

class pdf_formate(models.Model):
    branch_name = models.CharField(max_length=30)
    year = models.CharField(max_length=20)
    student_year = models.CharField(max_length=1)
    pyq_pdf = models.FileField(upload_to='pyq_pdfs')
