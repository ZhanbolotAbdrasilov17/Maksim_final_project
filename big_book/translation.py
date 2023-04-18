from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'desc')
