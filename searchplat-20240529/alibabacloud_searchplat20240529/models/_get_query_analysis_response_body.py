# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetQueryAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetQueryAnalysisResponseBodyResult = None,
        usage: main_models.GetQueryAnalysisResponseBodyUsage = None,
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
            temp_model = main_models.GetQueryAnalysisResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetQueryAnalysisResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetQueryAnalysisResponseBodyUsage(DaraModel):
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

class GetQueryAnalysisResponseBodyResult(DaraModel):
    def __init__(
        self,
        intent: str = None,
        queries: List[str] = None,
        query: str = None,
        sql: Dict[str, Any] = None,
    ):
        self.intent = intent
        self.queries = queries
        self.query = query
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent is not None:
            result['intent'] = self.intent

        if self.queries is not None:
            result['queries'] = self.queries

        if self.query is not None:
            result['query'] = self.query

        if self.sql is not None:
            result['sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intent') is not None:
            self.intent = m.get('intent')

        if m.get('queries') is not None:
            self.queries = m.get('queries')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        return self

