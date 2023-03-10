from flished import settings, utils
from django.shortcuts import reverse
from blog import blog_service
from core.resources import ui_strings as UI_STRINGS


def core_context(request):
    recent_posts = []
    if request.user.is_authenticated:
        recent_posts = blog_service.get_user_recent_posts(request.user)

    context = {
        'header':{
            'head': UI_STRINGS.UI_HOME_BANNER_TITLE,
            'lead': UI_STRINGS.UI_HOME_BANNER_SUB,
            'actions': [{'link': reverse('blog:create-post'), "label": UI_STRINGS.UI_HOME_BANNER_CTA}]
        },
        "UI_STRINGS": UI_STRINGS,
        'recent_posts': recent_posts,
        'UI_STRINGS_CONTEXT': UI_STRINGS.UI_STRINGS_CONTEXT,
        'site_name' : settings.SITE_NAME,
        'SITE_NAME' : settings.SITE_NAME,
        'SITE_HEADER_BG': settings.SITE_HEADER_BG,
        'META_KEYWORDS': UI_STRINGS.HOME_META_KEYWORDS,
        'META_DESCRIPTION': UI_STRINGS.HOME_META_DESCRIPTION,
        'UI_WHATSAPP_SHARE_BODY': UI_STRINGS.UI_WHATSAPP_SHARE_BODY,
        'DEFAULT_FROM_EMAIL': settings.DEFAULT_FROM_EMAIL,
        'TEMPLATE_CACHE_TIMEOUT': settings.TEMPLATE_CACHE_TIMEOUT,
        'SEARCH_AVAILABLE': True
    }
    return context