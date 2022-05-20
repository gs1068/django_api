from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # Metaクラスはモデルクラス内に配置される
    # MetaクラスはDjangoのどのモデルへの取り扱いを変更することが可能
    class Meta:
        model = Todo
        # fieldsで指定したカラムを表示できる
        fields = ('id', 'title', 'created_at')
        read_only_fields = ('id',)
