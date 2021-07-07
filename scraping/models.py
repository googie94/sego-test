# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import re



class HashPost(models.Model):
    post_id = models.CharField(verbose_name="포스트아이디", max_length=45, unique=True)
    domain = models.CharField(verbose_name="도메인", max_length=45, null=True, blank=True)
    bc_id = models.CharField(verbose_name="블로그/카페아이디", max_length=45, null=True, blank=True)
    author = models.CharField(verbose_name="작성자", max_length=100, null=True, blank=True)
    title = models.CharField(verbose_name="제목", max_length=100, null=True, blank=True)
    content = models.TextField(verbose_name="내용", null=True, blank=True)
    created_date = models.DateTimeField(verbose_name="작성일", null=True, blank=True)
    url = models.CharField(verbose_name="본문주소", max_length=200, null=True, blank=True)
    is_hidden = models.BooleanField(verbose_name="숨김여부", default=False)

    class Meta:
        db_table = 'hash_post'
        verbose_name = '포스트'
        verbose_name_plural = '포스트'

class HashPostTag(models.Model):
    post_id = models.CharField(verbose_name="포스트아이디", max_length=45)
    tag = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'hash_post_tag'
        verbose_name = '태그'
        verbose_name_plural = '태그'

class HashPostImage(models.Model):
    post_id = models.CharField(verbose_name="포스트아이디", max_length=45)
    url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'hash_post_image'
        verbose_name = '이미지'
        verbose_name_plural = '이미지'

# ---------------------------------------

class PostNaver(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    bc_id = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    is_hidden = models.BooleanField(default=False)
    is_good_count = models.IntegerField(default=0)
    is_bad_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'post_naver'
        verbose_name = '네이버 포스트'
        verbose_name_plural = '네이버 포스트'

class PostNaverImage(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'post_naver_image'
        verbose_name = '네이버 포스트 이미지'
        verbose_name_plural = '네이버 포스트 이미지'

class PostNaverTag(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'post_naver_tag'
        verbose_name = '네이버 포스트 태그'
        verbose_name_plural = '네이버 포스트 태그'

    def hangul(self):
        hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')
        result = hangul.sub('', self.tag)
        return result

class PostInstagram(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    is_hidden = models.BooleanField(default=False)
    is_good_count = models.IntegerField(default=0)
    is_bad_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'post_instagram'
        verbose_name = '인스타그램 포스트'
        verbose_name_plural = '인스타그램 포스트'

class PostInstagramTag(models.Model):
    post_id = models.CharField(max_length=45, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'post_instagram_tag'
        verbose_name = '인스타그램 포스트 태그'
        verbose_name_plural = '인스타그램 포스트 태그'

    def hangul(self):
        hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')
        result = hangul.sub('', self.tag)
        return result


##################################################################### 

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