import sys, struct, os.path

from django.utils import text
from django.utils.http import (
    base36_to_int, escape_leading_slashes, http_date, int_to_base36,
    url_has_allowed_host_and_scheme, is_same_domain, parse_etags, parse_http_date, quote_etag,
    urlencode, urlsafe_base64_decode, urlsafe_base64_encode
)
from django.utils.html import (
    conditional_escape, escape, escapejs, format_html, html_safe, json_script,
    linebreaks, smart_urlquote, strip_spaces_between_tags, strip_tags, urlize,
)
from django.utils.ipv6 import clean_ipv6_address, is_valid_ipv6_address
import datetime
from django.utils import feedgenerator
from django.utils.encoding import (
    escape_uri_path, filepath_to_uri,
    iri_to_uri, smart_str,
    uri_to_iri,
)
from django import forms
from django.conf import settings
settings.configure()

def test_base36_to_int(inp):
    try:
        base36_to_int(inp)
    except:
        pass

def test_escape_leading_slashes(inp):
    escape_leading_slashes(inp)

def test_url_has_allowed_host_and_scheme(inp):
    url_has_allowed_host_and_scheme(inp, allowed_hosts={'a', 'b'})

def test_parse_etags(inp):
    parse_etags(inp)

def test_parse_http_date(inp):
    try:
        parse_http_date(inp)
    except:
        pass
def test_quote_etag(inp):
    quote_etag(inp)

def test_urlencode(inp):
    try:
        urlencode(inp)
    except:
        pass

def test_urlsafe_base64_decode(inp):
    try:
        urlsafe_base64_decode(inp)
    except:
        pass

def test_urlsafe_base64_encode(inp):
    urlsafe_base64_encode(inp)

def test_conditional_escape(inp):
    conditional_escape(inp)

def test_escape(inp):
    escape(inp)

def test_escapejs(inp):
    escapejs(inp)

def test_json_script(inp):
    json_script(inp, 'id')

def test_linebreaks(inp):
    linebreaks(inp)

def test_smart_urlquote(inp):
    smart_urlquote(inp)

def test_strip_spaces_between_tags(inp):
    strip_spaces_between_tags(inp)

def test_strip_tags(inp):
    try:
        strip_tags(inp)
    except:
        pass

def test_urlize(inp):
    urlize(inp)

def test_smart_split(inp):
    text.smart_split(inp)

def test_Truncator(inp):
    text.Truncator(inp).words(8, '...', html=True)

def test_wrap(inp):
    text.wrap(inp, 8)

def test_normalize_newlines(inp):
    text.normalize_newlines(inp)

def test_phone(inp):
    text.phone2numeric(inp)

def test_unescape_string_literal(inp):
    try:
        text.unescape_string_literal(inp)
    except:
        pass

def test_get_valid_filename(inp):
    text.get_valid_filename(inp)

def test_is_valid_ipv6_address(inp):
    try:
        is_valid_ipv6_address(inp)
    except:
        pass

def test_clean_ipv6_address(inp):
    try:
        clean_ipv6_address(inp)
    except:
        pass

def test_slugify(inp):
    text.slugify(inp)

def test_camel_case_to_spaces(inp):
    text.camel_case_to_spaces(inp)

def test_get_tag_uri(inp):
    try:
        feedgenerator.get_tag_uri(inp, datetime.date(2004, 10, 25))
    except:
        pass

def test_Atom1Feed(inp):
    feedgenerator.Atom1Feed(inp, "link", "description")

def test_Rss201rev2Feed(inp):
    feedgenerator.Rss201rev2Feed(inp, "link", "description")

def test_escape_uri_path(inp):
    escape_uri_path(inp)

def test_filepath_to_uri(inp):
    filepath_to_uri(inp)

def test_iri_to_uri(inp):
    iri_to_uri(inp)

def test_uri_to_iri(inp):
    try:
        uri_to_iri(inp)
    except:
        pass

def test_smart_str(inp):
    try:
        smart_str(inp)
    except:
        pass

def test_forms_BooleanField(inp):
    try:
        forms.BooleanField().clean(inp)
    except:
        pass
def test_forms_NullBooleanField(inp):
    try:
        forms.NullBooleanField().clean(inp)
    except:
        pass
def test_forms_CharField(inp):
    try:
        forms.CharField().clean(inp)
    except:
        pass
def test_forms_DateField(inp):
    try:
        forms.DateField().clean(inp)
    except:
        pass
def test_forms_DateTimeField(inp):
    try:
        forms.DateTimeField().clean(inp)
    except:
        pass
def test_forms_DecimalField(inp):
    try:
        forms.DecimalField().clean(inp)
    except:
        pass
def test_forms_DurationField(inp):
    try:
        forms.DurationField().clean(inp)
    except:
        pass
def test_forms_EmailField(inp):
    try:
        forms.EmailField().clean(inp)
    except:
        pass
def test_forms_Field(inp):
    try:
        forms.Field().clean(inp)
    except:
        pass
def test_forms_FloatField(inp):
    try:
        forms.FloatField().clean(inp)
    except:
        pass
def test_forms_GenericIPAddressField(inp):
    try:
        forms.GenericIPAddressField().clean(inp)
    except:
        pass
def test_forms_IntegerField(inp):
    try:
        forms.IntegerField().clean(inp)
    except:
        pass
def test_forms_NullBooleanField(inp):
    try:
        forms.NullBooleanField().clean(inp)
    except:
        pass
def test_forms_SlugField(inp):
    try:
        forms.SlugField().clean(inp)
    except:
        pass
def test_forms_TimeField(inp):
    try:
        forms.TimeField().clean(inp)
    except:
        pass
def test_forms_URLField(inp):
    try:
        forms.URLField().clean(inp)
    except:
        pass
def test_forms_UUIDField(inp):
    try:
        forms.UUIDField().clean(inp)
    except:
        pass

def test_limited_parse_qsl(inp):
    try:
        limited_parse_qsl(inp)
    except:
        pass

tests = [
    (test_base36_to_int, str),
    (test_escape_leading_slashes, str),
    (test_url_has_allowed_host_and_scheme, str),
    (test_parse_etags, str),
    (test_parse_http_date, str),
    (test_quote_etag, str),
    (test_urlencode, str),
    (test_urlsafe_base64_decode, str),
    (test_urlsafe_base64_encode, bytes),
    (test_conditional_escape, str),
    (test_escape, str),
    (test_escapejs, str),
    (test_json_script, str),
    (test_linebreaks, str),
    (test_smart_urlquote, str),
    (test_strip_spaces_between_tags, str),
    (test_strip_tags, str),
    (test_urlize, str),
    (test_smart_split, str),
    (test_Truncator, str),
    (test_wrap, str),
    (test_normalize_newlines, str),
    (test_phone, str),
    (test_unescape_string_literal, str),
    (test_get_valid_filename, str),
    (test_is_valid_ipv6_address, str),
    (test_clean_ipv6_address, str),
    (test_slugify, str),
    (test_camel_case_to_spaces, str),
    (test_get_tag_uri, str),
    (test_Atom1Feed, str),
    (test_Rss201rev2Feed, str),
    (test_escape_uri_path, str),
    (test_filepath_to_uri, str),
    (test_iri_to_uri, str),
    (test_uri_to_iri, str),
    (test_smart_str, bytes),
    (test_forms_BooleanField, str),
    (test_forms_NullBooleanField, str),
    (test_forms_CharField, str),
    (test_forms_DateField, str),
    (test_forms_DateTimeField, str),
    (test_forms_DecimalField, str),
    (test_forms_DurationField, str),
    (test_forms_EmailField, str),
    (test_forms_Field, str),
    (test_forms_FloatField, str),
    (test_forms_GenericIPAddressField, str),
    (test_forms_IntegerField, str),
    (test_forms_NullBooleanField, str),
    (test_forms_SlugField, str),
    (test_forms_TimeField, str),
    (test_forms_URLField, str),
    (test_forms_UUIDField, str),
    (test_limited_parse_qsl, str),

]

#def FuzzerRunOne(FuzzerInput):
#    if len(FuzzerInput) < 2:
#        return
#    choice = struct.unpack('>H', FuzzerInput[:2])[0]
#    if choice >= len(tests):
#        return
#    FuzzerInput = FuzzerInput[2:]
#
#    if tests[choice][1] == str:
#        FuzzerInput = FuzzerInput.decode("utf8", "replace")
#    
#    tests[choice][0](FuzzerInput)
