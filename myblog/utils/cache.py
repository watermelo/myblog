#coding=utf8
import logging
import md5
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from time import time
from django.core.cache import get_cache

logger = logging.getLogger(__name__)

try:
    cache = get_cache('memcache')
except ImportError as e:
    logger.warn(u'加载memcache时出错:[%s], 改为内存缓存', e)
    cache = get_cache('default')


def cache_decorator(expiration=3*60):

    def wrapper(func):
        def news(*args, **kwargs):
            unique_str = repr((func, args, kwargs))
            m = md5.new(unique_str)
            key = m.hexdigest()
            value = cache.get(key)
            if value:
                return value
            else:
                value = func(*args, **kwargs)
                cache.set(key, value, expiration)
                return value
        return news
    return wrapper
