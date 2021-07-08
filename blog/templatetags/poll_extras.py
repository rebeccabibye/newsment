from django import template
import requests
from lxml.html import fromstring

register = template.Library()

@register.filter(name='TitleOfArticle')
def TitleOfArticle(value,arg): #value
    tempvar = str(arg)  #url
    r = requests.get(tempvar)
    tree = fromstring(r.content)
    title = tree.findtext('.//title')
    return title

@register.filter(name='ConvertToInteger')
def ConvertToInteger(value,arg):
    integer = int(arg)
    return integer