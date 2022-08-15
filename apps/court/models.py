from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
CORT_NUM = (
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third')
)


class Court(models.Model):
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='booked_corts',
                                 verbose_name='Заказчик')
    court_num = models.CharField(verbose_name='Поле', max_length=10, choices=CORT_NUM)
    schedule = models.DateTimeField(verbose_name='Дата и время')
    is_booked = models.BooleanField(verbose_name='Забронирован', default=False)

    def __str__(self):
        return self.court_num

    class Meta:
        db_table = 'court'
        verbose_name = 'Бронь площадки'
        verbose_name_plural = 'Забронированные площадки'
