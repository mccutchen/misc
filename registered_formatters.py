#import wrm.formatter

import re

FORMATTERS = dict()
PATTERN_TEMPLATE = '^%s$'
DEFAULT_FORMATTER = None

class register_formatter:
    def __init__(self, pattern, default=False):
        self.pattern = pattern
        self.compiledpattern = re.compile(PATTERN_TEMPLATE % pattern)
        self.default = default

    def __call__(self, func):
        global DEFAULT_FORMATTER
        if self.default:
            DEFAULT_FORMATTER = func
        else:
            FORMATTERS[self.compiledpattern] = func
        return func

def find_formatter(name):
    for pattern in FORMATTERS:
        if pattern.match(name):
            return FORMATTERS[pattern]
    return DEFAULT_FORMATTER

@register_formatter('', True)
def default_formatter(value, allvalues=None):
    return value.strip()

@register_formatter('credit_hours')
def credit_hours(value, allvalues=None):
    # remove trailing zeros and decimals
    return value.strip().rstrip('0').rstrip('.')

@register_formatter('meets.*')
def preserve_spaces(value, allvalues=None):
    print 'Preserving space...'
    return value