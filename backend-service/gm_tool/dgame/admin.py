from django.contrib import admin
from dgame.models import gift
# Register your models here.

admin.site.site_header = 'GM后台'  # 设置header
admin.site.site_title = 'OSS'      # 设置title

admin.site.register(gift)
