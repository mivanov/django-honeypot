from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('honeypot/honeypot_field.html')
def render_honeypot_field(field_name=None):
    """
        Renders honeypot field named field_name (defaults to HONEYPOT_FIELD_NAME).
    """
    if not field_name:
        field_name = settings.HONEYPOT_FIELD_NAME
    value = getattr(settings, 'HONEYPOT_VALUE', '')
    if callable(value):
        value = value()
    
    use_js_field = getattr(settings, 'HONEYPOT_USE_JS_FIELD', False)
    display_script_tags = True
    
    return {'fieldname': field_name, 'value': value,
            'display_script_tags': display_script_tags,
            'use_js_field': use_js_field}


@register.inclusion_tag('honeypot/honeypot_field.html')
def render_honeypot_field_js(field_name=None):
    """
        Renders honeypot field named field_name (defaults to HONEYPOT_FIELD_NAME).
    """
    if not field_name:
        field_name = settings.HONEYPOT_FIELD_NAME
    value = getattr(settings, 'HONEYPOT_VALUE', '')
    if callable(value):
        value = value()
    
    use_js_field = getattr(settings, 'HONEYPOT_USE_JS_FIELD', False)
    display_script_tags = False
    
    return {'fieldname': field_name, 'value': value, 'display_script_tags': display_script_tags,
        'use_js_field': use_js_field}
