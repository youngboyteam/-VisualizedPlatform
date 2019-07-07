from django.db import models

# Create your models here.
class TestData(models.Model):
    id = models.CharField(primary_key=True,verbose_name=u"主键",max_length=20,default="")
    x_data = models.CharField(max_length=1000,verbose_name="月份")
    y_data = models.CharField(max_length=1000,verbose_name="数值")

    class Meta:
        verbose_name = u"测试数据"
        verbose_name_plural = verbose_name