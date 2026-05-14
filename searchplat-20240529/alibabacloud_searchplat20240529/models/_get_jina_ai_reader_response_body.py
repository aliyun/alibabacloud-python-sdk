# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetJinaAiReaderResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetJinaAiReaderResponseBodyResult = None,
        usage: main_models.GetJinaAiReaderResponseBodyUsage = None,
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
            temp_model = main_models.GetJinaAiReaderResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetJinaAiReaderResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetJinaAiReaderResponseBodyUsage(DaraModel):
    def __init__(
        self,
        token_count: int = None,
    ):
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.token_count is not None:
            result['token_count'] = self.token_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')

        return self

class GetJinaAiReaderResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        meta: Dict[str, str] = None,
    ):
        self.content = content
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.meta is not None:
            result['meta'] = self.meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        return self

