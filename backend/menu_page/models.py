from django.db import models


class Menu(models.Model):
    """Класс для родителя"""

    name = models.CharField('Меню',
                            max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    """Класс для дочерних элементов меню"""

    name = models.CharField('Подменю',
                            max_length=50)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='children')
    menu = models.ForeignKey(Menu,
                             related_name='submenus',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'

    def __str__(self):
        return self.name
