# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import re

class NaverPost(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'naver_post'


class NaverComment(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_comment'


class InstaPost(models.Model):
    short_code = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    like_count = models.IntegerField()

    class Meta:
        db_table = 'insta_post'


class InstaTag(models.Model):
    short_code = models.CharField(max_length=45, blank=True, null=True)
    tag = models.CharField(max_length=45, blank=True, null=True)
    count = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'insta_tag'

    def hangul(self):
        hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')
        result = hangul.sub('', self.tag)
        return result