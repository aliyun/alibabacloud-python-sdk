# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class HotNewsRecommendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.HotNewsRecommendResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.HotNewsRecommendResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class HotNewsRecommendResponseBodyData(DaraModel):
    def __init__(
        self,
        news: List[main_models.HotNewsRecommendResponseBodyDataNews] = None,
    ):
        self.news = news

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['news'] = []
        if self.news is not None:
            for k1 in self.news:
                result['news'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.news = []
        if m.get('news') is not None:
            for k1 in m.get('news'):
                temp_model = main_models.HotNewsRecommendResponseBodyDataNews()
                self.news.append(temp_model.from_map(k1))

        return self

class HotNewsRecommendResponseBodyDataNews(DaraModel):
    def __init__(
        self,
        content: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        search_source: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.search_source = search_source
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls

        if self.pub_time is not None:
            result['pubTime'] = self.pub_time

        if self.search_source is not None:
            result['searchSource'] = self.search_source

        if self.source is not None:
            result['source'] = self.source

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')

        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')

        if m.get('searchSource') is not None:
            self.search_source = m.get('searchSource')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

