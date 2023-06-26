from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано'), ]


class ToDoList(models.Model):
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    time = models.DateTimeField(default=None, verbose_name="Дата выполнения")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.pk} {self.description}: {self.status}"

    class Meta:
        db_table = "todolist"
        verbose_name = "Дело"
        verbose_name_plural = "Список дел"
