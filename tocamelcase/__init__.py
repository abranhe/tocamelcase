import re

def convert(non_camel_case):
    return ''.join(x.capitalize() or '_' for x in non_camel_case.split('_'))
