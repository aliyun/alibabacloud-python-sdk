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
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # requestId
        self.trace_id = trace_id

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

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

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

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

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
        snippet: str = None,
        title: str = None,
        url: str = None,
    ):
        self.snippet = snippet
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snippet is not None:
            result['snippet'] = self.snippet

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

