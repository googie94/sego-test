from django.db import models

# Create your models here.


class Segouser(models.Model):
	username = models.CharField(max_length=32, verbose_name='사용자명')
	email = models.CharField(max_length=128, verbose_name='이메일')
	password = models.CharField(max_length=64, verbose_name='비밀번호')
	registered_time = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

	def __str__(self):
		return self.username #위 클래스에서 문자열로 변환하며 어떤값이 반환될 지 지정

	class Meta:
		db_table='sego_user' #데이터 내 테이블 명 지정
		verbose_name='세고사용자' # 관리자에서 테이블명 지정
		verbose_name_plural='세고사용자' #복수형으로 나타나는 이름을 지정



