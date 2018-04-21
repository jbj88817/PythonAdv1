# coding=utf-8
# 可迭代对象和迭代器
import requests

from collections import Iterable, Iterator


class WeatherIterator(Iterator):

    def __iter__(self):
        pass

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    @staticmethod
    def get_weather(city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s ' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'北京', u'上海', u'长春', u'广州']):
    print x
