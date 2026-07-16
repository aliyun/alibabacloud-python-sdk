# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maasaisearchproxy20260424 import models as main_models
from darabonba.model import DaraModel

class WebSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.WebSearchResponseBodyData = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.WebSearchResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class WebSearchResponseBodyData(DaraModel):
    def __init__(
        self,
        result: List[main_models.WebSearchResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.result = result
        self.total = total

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.WebSearchResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class WebSearchResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        date: str = None,
        snippet: str = None,
        source: main_models.WebSearchResponseBodyDataResultSource = None,
        title: str = None,
        url: str = None,
    ):
        self.date = date
        self.snippet = snippet
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.snippet is not None:
            result['snippet'] = self.snippet

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('source') is not None:
            temp_model = main_models.WebSearchResponseBodyDataResultSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class WebSearchResponseBodyDataResultSource(DaraModel):
    def __init__(
        self,
        domain: str = None,
        favicon: str = None,
        name: str = None,
    ):
        self.domain = domain
        self.favicon = favicon
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.favicon is not None:
            result['favicon'] = self.favicon

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('favicon') is not None:
            self.favicon = m.get('favicon')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

