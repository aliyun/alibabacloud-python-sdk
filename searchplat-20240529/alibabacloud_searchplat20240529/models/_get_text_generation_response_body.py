# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetTextGenerationResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetTextGenerationResponseBodyResult = None,
        usage: main_models.GetTextGenerationResponseBodyUsage = None,
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
            temp_model = main_models.GetTextGenerationResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetTextGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetTextGenerationResponseBodyUsage(DaraModel):
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

class GetTextGenerationResponseBodyResult(DaraModel):
    def __init__(
        self,
        search_results: List[main_models.GetTextGenerationResponseBodyResultSearchResults] = None,
        text: str = None,
    ):
        self.search_results = search_results
        self.text = text

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['search_results'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['search_results'].append(k1.to_map() if k1 else None)

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_results = []
        if m.get('search_results') is not None:
            for k1 in m.get('search_results'):
                temp_model = main_models.GetTextGenerationResponseBodyResultSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class GetTextGenerationResponseBodyResultSearchResults(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

