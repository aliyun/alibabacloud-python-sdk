# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetDocumentSplitResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetDocumentSplitResponseBodyResult = None,
        usage: main_models.GetDocumentSplitResponseBodyUsage = None,
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
            temp_model = main_models.GetDocumentSplitResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetDocumentSplitResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetDocumentSplitResponseBodyUsage(DaraModel):
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

class GetDocumentSplitResponseBodyResult(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.GetDocumentSplitResponseBodyResultChunks] = None,
        nodes: List[Dict[str, str]] = None,
        rich_texts: List[main_models.GetDocumentSplitResponseBodyResultRichTexts] = None,
        sentences: List[main_models.GetDocumentSplitResponseBodyResultSentences] = None,
    ):
        self.chunks = chunks
        self.nodes = nodes
        self.rich_texts = rich_texts
        self.sentences = sentences

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()
        if self.rich_texts:
            for v1 in self.rich_texts:
                 if v1:
                    v1.validate()
        if self.sentences:
            for v1 in self.sentences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['chunks'].append(k1.to_map() if k1 else None)

        if self.nodes is not None:
            result['nodes'] = self.nodes

        result['rich_texts'] = []
        if self.rich_texts is not None:
            for k1 in self.rich_texts:
                result['rich_texts'].append(k1.to_map() if k1 else None)

        result['sentences'] = []
        if self.sentences is not None:
            for k1 in self.sentences:
                result['sentences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.GetDocumentSplitResponseBodyResultChunks()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        self.rich_texts = []
        if m.get('rich_texts') is not None:
            for k1 in m.get('rich_texts'):
                temp_model = main_models.GetDocumentSplitResponseBodyResultRichTexts()
                self.rich_texts.append(temp_model.from_map(k1))

        self.sentences = []
        if m.get('sentences') is not None:
            for k1 in m.get('sentences'):
                temp_model = main_models.GetDocumentSplitResponseBodyResultSentences()
                self.sentences.append(temp_model.from_map(k1))

        return self

class GetDocumentSplitResponseBodyResultSentences(DaraModel):
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

class GetDocumentSplitResponseBodyResultRichTexts(DaraModel):
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

class GetDocumentSplitResponseBodyResultChunks(DaraModel):
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

