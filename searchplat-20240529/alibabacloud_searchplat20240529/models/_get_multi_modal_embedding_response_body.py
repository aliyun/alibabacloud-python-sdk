# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMultiModalEmbeddingResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetMultiModalEmbeddingResponseBodyResult = None,
        usage: main_models.GetMultiModalEmbeddingResponseBodyUsage = None,
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
            temp_model = main_models.GetMultiModalEmbeddingResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetMultiModalEmbeddingResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetMultiModalEmbeddingResponseBodyUsage(DaraModel):
    def __init__(
        self,
        image: int = None,
        image_token: int = None,
        text_token: int = None,
        token_count: int = None,
    ):
        self.image = image
        self.image_token = image_token
        self.text_token = text_token
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.image_token is not None:
            result['image_token'] = self.image_token

        if self.text_token is not None:
            result['text_token'] = self.text_token

        if self.token_count is not None:
            result['token_count'] = self.token_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('image_token') is not None:
            self.image_token = m.get('image_token')

        if m.get('text_token') is not None:
            self.text_token = m.get('text_token')

        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')

        return self

class GetMultiModalEmbeddingResponseBodyResult(DaraModel):
    def __init__(
        self,
        embeddings: List[main_models.GetMultiModalEmbeddingResponseBodyResultEmbeddings] = None,
    ):
        self.embeddings = embeddings

    def validate(self):
        if self.embeddings:
            for v1 in self.embeddings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['embeddings'] = []
        if self.embeddings is not None:
            for k1 in self.embeddings:
                result['embeddings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embeddings = []
        if m.get('embeddings') is not None:
            for k1 in m.get('embeddings'):
                temp_model = main_models.GetMultiModalEmbeddingResponseBodyResultEmbeddings()
                self.embeddings.append(temp_model.from_map(k1))

        return self

class GetMultiModalEmbeddingResponseBodyResultEmbeddings(DaraModel):
    def __init__(
        self,
        embedding: List[float] = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding is not None:
            result['embedding'] = self.embedding

        if self.index is not None:
            result['index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('embedding') is not None:
            self.embedding = m.get('embedding')

        if m.get('index') is not None:
            self.index = m.get('index')

        return self

