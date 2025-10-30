# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class RerankResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        results: main_models.RerankResponseBodyResults = None,
        status: str = None,
        tokens: int = None,
    ):
        # Detailed information returned by the interface.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Rerank results.
        self.results = results
        # API execution status, value description:
        # - **success**: Execution succeeded.
        # - **fail**: Execution failed.
        self.status = status
        # Number of consumed tokens.
        self.tokens = tokens

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

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.RerankResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        return self

class RerankResponseBodyResults(DaraModel):
    def __init__(
        self,
        results: List[main_models.RerankResponseBodyResultsResults] = None,
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
                temp_model = main_models.RerankResponseBodyResultsResults()
                self.results.append(temp_model.from_map(k1))

        return self

class RerankResponseBodyResultsResults(DaraModel):
    def __init__(
        self,
        document: str = None,
        index: int = None,
        relevance_score: float = None,
    ):
        # Re-ordered document information.
        self.document = document
        # Index of this document in the request parameter Documents, starting from 0.
        self.index = index
        # Rerank similarity score.
        self.relevance_score = relevance_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['Document'] = self.document

        if self.index is not None:
            result['Index'] = self.index

        if self.relevance_score is not None:
            result['RelevanceScore'] = self.relevance_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Document') is not None:
            self.document = m.get('Document')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('RelevanceScore') is not None:
            self.relevance_score = m.get('RelevanceScore')

        return self

