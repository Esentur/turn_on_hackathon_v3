from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Team(models.Model):
    captain = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='my_teams',
                                verbose_name='Капитан команды')
    name = models.CharField(verbose_name="Название команды", max_length=50)
    slogan = models.CharField(verbose_name="Девиз", max_length=500, blank=True, null=True)
    player1 = models.CharField(verbose_name="Игрок 1", max_length=50)
    player2 = models.CharField(verbose_name="Игрок 2", max_length=50)
    player3 = models.CharField(verbose_name="Игрок 3", max_length=50)
    player4 = models.CharField(verbose_name="Игрок 4", max_length=50)
    player5 = models.CharField(verbose_name="Игрок 5", max_length=50)

    def __str__(self):
        print(self.captain.username)
        return f'{self.name} - Капитан {self.captain.username}'

    class Meta:
        db_table = "team"
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Команда')
    text = models.TextField(verbose_name='Текст комментария', max_length=500)

    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)

    def __str__(self):
        return f'Автор коммента: {self.author} ----- Команда: {self.team} ----- Текст: {self.text}'

    class Meta:
        db_table = "comment"
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='likes',
                               verbose_name='Лайкнувший')
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='likes',
                             verbose_name='Команда')
    like = models.BooleanField(verbose_name='Лайк', default=False)

    def __str__(self):
        return f'Автор лайка: {self.author} ----- Команда: {self.team}'

    class Meta:
        db_table = "like"
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Favourite(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='favourites',
                               verbose_name='Избранные')
    vehicle = models.ForeignKey(Team,
                                on_delete=models.CASCADE,
                                related_name='favourites',
                                verbose_name='Избранные')
    favourite = models.BooleanField(verbose_name='favourite', default=False)

    def __str__(self):
        return f'Пользователь: {self.author} ----- Его(ее) избранное: {self.team}'

    class Meta:
        db_table = "favourite"
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class Rating(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='ratings',
                               verbose_name='Владелец рейтинга')
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='ratings',
                             verbose_name='Команда')

    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], default=1
    )

    def __str__(self):
        return f'Автор рейтинга: {self.author} ----- Команда: {self.team} ------ Рейтинг: {self.rating}'
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
