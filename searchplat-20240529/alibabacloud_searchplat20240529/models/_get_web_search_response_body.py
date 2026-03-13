# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetWebSearchResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetWebSearchResponseBodyResult = None,
        usage: main_models.GetWebSearchResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency is not None:
            result['latency'] = self.latency

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('result') is not None:
            temp_model = main_models.GetWebSearchResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetWebSearchResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetWebSearchResponseBodyUsage(DaraModel):
    def __init__(
        self,
        filter_model: main_models.GetWebSearchResponseBodyUsageFilterModel = None,
        rewrite_model: main_models.GetWebSearchResponseBodyUsageRewriteModel = None,
        search_count: int = None,
    ):
        self.filter_model = filter_model
        self.rewrite_model = rewrite_model
        self.search_count = search_count

    def validate(self):
        if self.filter_model:
            self.filter_model.validate()
        if self.rewrite_model:
            self.rewrite_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_model is not None:
            result['filter_model'] = self.filter_model.to_map()

        if self.rewrite_model is not None:
            result['rewrite_model'] = self.rewrite_model.to_map()

        if self.search_count is not None:
            result['search_count'] = self.search_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter_model') is not None:
            temp_model = main_models.GetWebSearchResponseBodyUsageFilterModel()
            self.filter_model = temp_model.from_map(m.get('filter_model'))

        if m.get('rewrite_model') is not None:
            temp_model = main_models.GetWebSearchResponseBodyUsageRewriteModel()
            self.rewrite_model = temp_model.from_map(m.get('rewrite_model'))

        if m.get('search_count') is not None:
            self.search_count = m.get('search_count')

        return self

class GetWebSearchResponseBodyUsageRewriteModel(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')

        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')

        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')

        return self

class GetWebSearchResponseBodyUsageFilterModel(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')

        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')

        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')

        return self

class GetWebSearchResponseBodyResult(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.GetWebSearchResponseBodyResultSearchResult] = None,
    ):
        self.search_result = search_result

    def validate(self):
        if self.search_result:
            for v1 in self.search_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['search_result'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['search_result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_result = []
        if m.get('search_result') is not None:
            for k1 in m.get('search_result'):
                temp_model = main_models.GetWebSearchResponseBodyResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class GetWebSearchResponseBodyResultSearchResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        link: str = None,
        meta_info: Dict[str, Any] = None,
        position: int = None,
        snippet: str = None,
        tilte: str = None,
    ):
        self.content = content
        self.link = link
        self.meta_info = meta_info
        self.position = position
        self.snippet = snippet
        self.tilte = tilte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.link is not None:
            result['link'] = self.link

        if self.meta_info is not None:
            result['meta_info'] = self.meta_info

        if self.position is not None:
            result['position'] = self.position

        if self.snippet is not None:
            result['snippet'] = self.snippet

        if self.tilte is not None:
            result['tilte'] = self.tilte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('meta_info') is not None:
            self.meta_info = m.get('meta_info')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('tilte') is not None:
            self.tilte = m.get('tilte')

        return self

