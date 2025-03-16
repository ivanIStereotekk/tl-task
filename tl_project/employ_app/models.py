from django.db.models import CharField, DateField, DecimalField, CASCADE, ForeignKey, Model

from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    name = CharField(max_length=255)
    city = CharField(max_length=100, null=True, blank=True)  # Добавляем город
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name} ({self.city})" if self.city else self.name
    
class Employee(Model):
    full_name = CharField(max_length=255)
    position = CharField(max_length=255)
    hire_date = DateField()
    salary = DecimalField(max_digits=10, decimal_places=2)
    department = ForeignKey(Department, on_delete=CASCADE, related_name='employees')

    def __str__(self):
        return self.full_name