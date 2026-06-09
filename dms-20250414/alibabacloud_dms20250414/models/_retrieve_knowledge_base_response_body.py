# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class RetrieveKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.RetrieveKnowledgeBaseResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.RetrieveKnowledgeBaseResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RetrieveKnowledgeBaseResponseBodyData(DaraModel):
    def __init__(
        self,
        matches: List[main_models.RetrieveKnowledgeBaseResponseBodyDataMatches] = None,
        results: List[main_models.RetrieveKnowledgeBaseResponseBodyDataResults] = None,
    ):
        self.matches = matches
        self.results = results

    def validate(self):
        if self.matches:
            for v1 in self.matches:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Matches'] = []
        if self.matches is not None:
            for k1 in self.matches:
                result['Matches'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matches = []
        if m.get('Matches') is not None:
            for k1 in m.get('Matches'):
                temp_model = main_models.RetrieveKnowledgeBaseResponseBodyDataMatches()
                self.matches.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.RetrieveKnowledgeBaseResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class RetrieveKnowledgeBaseResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        id: str = None,
        loader_metadata: str = None,
        metadata: Dict[str, Any] = None,
        rerank_score: float = None,
        retrieval_source: int = None,
        score: float = None,
        vector: List[float] = None,
    ):
        self.content = content
        self.file_name = file_name
        self.id = id
        self.loader_metadata = loader_metadata
        self.metadata = metadata
        self.rerank_score = rerank_score
        self.retrieval_source = retrieval_source
        self.score = score
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.rerank_score is not None:
            result['RerankScore'] = self.rerank_score

        if self.retrieval_source is not None:
            result['RetrievalSource'] = self.retrieval_source

        if self.score is not None:
            result['Score'] = self.score

        if self.vector is not None:
            result['Vector'] = self.vector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RerankScore') is not None:
            self.rerank_score = m.get('RerankScore')

        if m.get('RetrievalSource') is not None:
            self.retrieval_source = m.get('RetrievalSource')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Vector') is not None:
            self.vector = m.get('Vector')

        return self

class RetrieveKnowledgeBaseResponseBodyDataMatches(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        id: str = None,
        loader_metadata: str = None,
        metadata: Dict[str, Any] = None,
    ):
        self.content = content
        self.file_name = file_name
        self.id = id
        self.loader_metadata = loader_metadata
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        return self

