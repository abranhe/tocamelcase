import re

def toCamelCase(non_camel_case):
    return ''.join(camelCase.capitalize() or '_' for camelCase in non_camel_case.split('_'))
