from modeltranslation.translator import translator, TranslationOptions
from .models import *


class LatestResultsTranslationOptions(TranslationOptions):
    fields = ('name',)


class ServicesTranslationOptions(TranslationOptions):
    fields = ('name','title')



class ComunityTranslationOptions(TranslationOptions):
    fields = ('job','title')



class Detail_PortfolioTranslationOptions(TranslationOptions):
    fields = ('detail_name','title','text')



class Benefits_portfolioTranslationOptions(TranslationOptions):
    fields = ('title',)





translator.register(LatestResults, LatestResultsTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(Comunity, ComunityTranslationOptions)
translator.register(Detail_Portfolio, Detail_PortfolioTranslationOptions)
translator.register(Benefits_portfolio, Benefits_portfolioTranslationOptions)
