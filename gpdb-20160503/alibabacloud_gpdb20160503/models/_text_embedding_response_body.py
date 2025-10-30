# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class TextEmbeddingResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        results: main_models.TextEmbeddingResponseBodyResults = None,
        status: str = None,
        text_tokens: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.results = results
        self.status = status
        self.text_tokens = text_tokens

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.text_tokens is not None:
            result['TextTokens'] = self.text_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.TextEmbeddingResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TextTokens') is not None:
            self.text_tokens = m.get('TextTokens')

        return self

class TextEmbeddingResponseBodyResults(DaraModel):
    def __init__(
        self,
        results: List[main_models.TextEmbeddingResponseBodyResultsResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.TextEmbeddingResponseBodyResultsResults()
                self.results.append(temp_model.from_map(k1))

        return self

class TextEmbeddingResponseBodyResultsResults(DaraModel):
    def __init__(
        self,
        embedding: main_models.TextEmbeddingResponseBodyResultsResultsEmbedding = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        if self.embedding:
            self.embedding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding is not None:
            result['Embedding'] = self.embedding.to_map()

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Embedding') is not None:
            temp_model = main_models.TextEmbeddingResponseBodyResultsResultsEmbedding()
            self.embedding = temp_model.from_map(m.get('Embedding'))

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

class TextEmbeddingResponseBodyResultsResultsEmbedding(DaraModel):
    def __init__(
        self,
        embedding: List[float] = None,
    ):
        self.embedding = embedding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding is not None:
            result['Embedding'] = self.embedding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Embedding') is not None:
            self.embedding = m.get('Embedding')

        return self

