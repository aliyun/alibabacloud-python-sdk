# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GenerateTraceability(DaraModel):
    def __init__(
        self,
        news: List[main_models.GenerateTraceabilityNews] = None,
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
        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.GenerateTraceabilityNews()
                self.news.append(temp_model.from_map(k1))

        return self



class GenerateTraceabilityNews(DaraModel):
    def __init__(
        self,
        index: int = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        title: str = None,
        url: str = None,
    ):
        self.index = index
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

