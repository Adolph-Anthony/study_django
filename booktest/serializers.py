from rest_framework import serializers
from .models import BookInfo

# class BookInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookInfo
#         fields = '__all__'

class BookInfoSerializer(serializers.ModelSerializer):
    """模型图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = '__all__'


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    logo = serializers.ImageField(label='图片', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    def validate_btitle(self, value):
        '''自定义验证'''
        if 'django' not in value.lower():
            #如果输入的词小写不是django则抛出错误
            raise serializers.ValidationError("验证错误描述")
        return value

    def validate(self, attrs):
        bcomment = attrs['bcomment']
        bread = attrs['bread']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    def create(self, validated_data):
        """新建"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        #如果没传这个属性,直接使用对象原来的属性代替,instance.bpub_date
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
    #外键嵌套序列化
    hbook = BookInfoSerializer()