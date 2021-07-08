from django import template
import requests
from lxml.html import fromstring

register = template.Library()

@register.filter(name='TitleOfArticle2')
def TitleOfArticle2(value,arg): #value
    tempvar = str(arg)  #url
    r = requests.get(tempvar)
    tree = fromstring(r.content)
    title = tree.findtext('.//title')
    return title