from django.db import models
from django.db.models import fields

from users.models import CustomUser


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента',
        blank=False,
        max_length=200,
        help_text='Укажите название ингредиента'
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        blank=False,
        max_length=200,
        help_text='Укажите единицу измерения'
    )

    class Meta:
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название тега',
        blank=False,
        max_length=200,
        help_text='Укажите тег'
    )
    color = models.CharField(
        verbose_name='Цвет тега', 
        null=True,
        max_length=200,
        help_text='Укажите цвет тег'
    )
    slug = models.SlugField(
        verbose_name='Слаг тега',
        max_length=200,
        unique=True,
        help_text=('Укажите слаг тега. Используйте только латиницу, цифры, '
                   'дефисы и знаки подчёркивания')
    )

    class Meta:
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='recipes',
        verbose_name='Теги',
    )
    author = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        through='IngredientTemp',
        related_name='recipes',
        verbose_name='Ингредиенты',
    )
    name = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
        blank=False,
        help_text='Напишите название рецепта'
    )
    image = models.ImageField(
        upload_to='image/', 
        blank=True
    )
    text = models.TextField(
        verbose_name='Описание рецепта',
        blank=False,
        help_text='Добавьте сюда описание рецепта'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        blank=False,
        help_text='Укажите Время приготовления в минутах',
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class IngredientTemp(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        blank=False
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        blank=False
    )
    amount = models.PositiveSmallIntegerField(
        blank=False
    )
    class Meta:
        verbose_name_plural = ('Промежуточная таблица для добавления '
                               'новой колонки - количество')
        ordering = ['id']


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='purchases', verbose_name='Пользователь')
    purchase = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='customers', verbose_name='Покупка')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='favorite'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='favorite'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='followers')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], 
                                    name='subscription_unique'),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} => {self.author}'
