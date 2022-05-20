from django.db import models

# 引数のmodels.Modelは固定で
class Todo(models.Model):
    title = models.CharField(max_length=140, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # この記載があることで管理画面に表示されるモデル内のデータを判別している
    # この記載がないと管理画面側ではtodo objectと表示される
    def __str__(self):
        return self.title
