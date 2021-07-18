from django.db import models

from users.models import CustomUser

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
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
        null=True,
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
    id = models.AutoField(primary_key=True, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tags',
        verbose_name='Теги',
    )
    author = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        through='IngredientTemp',
        related_name='ingredients',
        verbose_name='Ингредиенты',
    )
    is_favorited = models.BooleanField(
        blank=False,
    )
    is_in_shopping_cart = models.BooleanField(
        blank=False,
    )
    name = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
        blank=False,
        help_text='Напишите название рецепта'
    )
    image = models.ImageField(
        upload_to='image/', 
        null=False
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

    class Meta:
        verbose_name_plural = 'Рецепты'
        ordering = ['id']


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
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        help_text='Напишите название рецепта'
    )
    image = models.ImageField(
        upload_to='image/', 
        null=False
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        blank=False,
        help_text='Укажите Время приготовления в минутах',
    )
    class Meta:
        verbose_name_plural = 'Корзина рецептов'
        ordering = ['id']


class Favorite(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        help_text='Напишите название рецепта'
    )
    image = models.ImageField(
        upload_to='image/', 
        null=False
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        blank=False,
        help_text='Укажите Время приготовления в минутах',
    )
    class Meta:
        verbose_name_plural = 'Избранные рецепты'
        ordering = ['id']


class Subscription(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        CustomUser, null=True,
        on_delete=models.CASCADE,
        related_name='following'
    )
    class Meta:
        verbose_name_plural = 'Подписки'
        ordering = ['id']