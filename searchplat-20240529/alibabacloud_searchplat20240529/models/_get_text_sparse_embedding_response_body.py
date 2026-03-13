# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetTextSparseEmbeddingResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetTextSparseEmbeddingResponseBodyResult = None,
        usage: main_models.GetTextSparseEmbeddingResponseBodyUsage = None,
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
            temp_model = main_models.GetTextSparseEmbeddingResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetTextSparseEmbeddingResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetTextSparseEmbeddingResponseBodyUsage(DaraModel):
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

class GetTextSparseEmbeddingResponseBodyResult(DaraModel):
    def __init__(
        self,
        sparse_embeddings: List[main_models.GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings] = None,
    ):
        self.sparse_embeddings = sparse_embeddings

    def validate(self):
        if self.sparse_embeddings:
            for v1 in self.sparse_embeddings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['sparse_embeddings'] = []
        if self.sparse_embeddings is not None:
            for k1 in self.sparse_embeddings:
                result['sparse_embeddings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sparse_embeddings = []
        if m.get('sparse_embeddings') is not None:
            for k1 in m.get('sparse_embeddings'):
                temp_model = main_models.GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings()
                self.sparse_embeddings.append(temp_model.from_map(k1))

        return self

class GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings(DaraModel):
    def __init__(
        self,
        embedding: List[main_models.GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding] = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        if self.embedding:
            for v1 in self.embedding:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['embedding'] = []
        if self.embedding is not None:
            for k1 in self.embedding:
                result['embedding'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embedding = []
        if m.get('embedding') is not None:
            for k1 in m.get('embedding'):
                temp_model = main_models.GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding()
                self.embedding.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        return self

class GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding(DaraModel):
    def __init__(
        self,
        token: str = None,
        token_id: int = None,
        weight: float = None,
    ):
        self.token = token
        self.token_id = token_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.token is not None:
            result['token'] = self.token

        if self.token_id is not None:
            result['token_id'] = self.token_id

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('token_id') is not None:
            self.token_id = m.get('token_id')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

