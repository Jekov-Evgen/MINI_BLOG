from django.db import models

class Blog_user(models.Model):
    post_title = models.CharField('Нзвание поста',max_length=50)
    publication_text = models.TextField('Текст публикации')
    author_name = models.CharField('Имя автора', max_length=50)
    publication_date = models.DateField('Дата публикации')
    image_post = models.ImageField("Фото публикации", default=1, upload_to='image%Y')
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        
    def __str__(self) -> str:
        return f'{self.post_title}, {self.author_name}'
    
    
class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text_comment = models.TextField(max_length=600)
    to_which_post = models.ForeignKey(Blog_user, on_delete=models.CASCADE, verbose_name='Публикация')
    
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        
    def __str__(self) -> str:
        return f'{self.name}, {self.to_which_post}'
    
class Like(models.Model):
    ip = models.CharField('IP-adress', max_length=100)
    pos = models.ForeignKey(Blog_user, verbose_name='Публикация', on_delete=models.CASCADE)
