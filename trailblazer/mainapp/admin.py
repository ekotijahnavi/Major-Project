# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Abstracts,Contact,FeedBack,Eceabstract,Cseab,Cseproject,Eceproject,Civilproject,Mechproject
from .models import Civilabstract,Mechabstract
# Register your models here.
admin.site.register(Eceabstract)
admin.site.register(Contact)
admin.site.register(FeedBack)
admin.site.register(Cseab)
admin.site.register(Cseproject)
admin.site.register(Eceproject)
admin.site.register(Civilproject)
admin.site.register(Mechproject)
admin.site.register(Civilabstract)
admin.site.register(Mechabstract)