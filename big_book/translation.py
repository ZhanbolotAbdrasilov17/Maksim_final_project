from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'desc')


@register(Reviews)
class ReviewsTranslation(TranslationOptions):
    fields = ('title', 'desc')
