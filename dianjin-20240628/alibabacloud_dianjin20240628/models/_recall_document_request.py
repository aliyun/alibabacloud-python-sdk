# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RecallDocumentRequest(DaraModel):
    def __init__(
        self,
        filters: List[main_models.RecallDocumentRequestFilters] = None,
        query: str = None,
        rearrangement: bool = None,
        top_k: int = None,
    ):
        # Metadata filter conditions.
        self.filters = filters
        # Text.
        # 
        # This parameter is required.
        self.query = query
        # Enable parent-child document chunk retrieval.
        # 
        # - Parent-child document chunks: During document parsing, a complete semantic block, such as a paragraph or a section, might split into multiple document chunks. This depends on your chunking strategy. When you enable parent-child document retrieval, the system attempts to complete the semantic block of the retrieved document chunk. This makes the corpus more semantically complete when constructing prompts, improving answer completeness and accuracy.
        self.rearrangement = rearrangement
        # The number of document chunks to retrieve.
        self.top_k = top_k

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['filters'].append(k1.to_map() if k1 else None)

        if self.query is not None:
            result['query'] = self.query

        if self.rearrangement is not None:
            result['rearrangement'] = self.rearrangement

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('filters') is not None:
            for k1 in m.get('filters'):
                temp_model = main_models.RecallDocumentRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rearrangement') is not None:
            self.rearrangement = m.get('rearrangement')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class RecallDocumentRequestFilters(DaraModel):
    def __init__(
        self,
        and_: List[main_models.RecallDocumentRequestFiltersAnd] = None,
        chunk_type: str = None,
        doc_id_list: List[str] = None,
        library_id: str = None,
        or_: List[main_models.RecallDocumentRequestFiltersOr] = None,
        status: List[str] = None,
    ):
        # AND expression, used to filter documents/document chunks.
        self.and_ = and_
        # Document chunk type, used to filter document chunks, such as: Text, Graph, Table, FAQ.
        self.chunk_type = chunk_type
        # Document ID list, used to filter documents/document chunks.
        self.doc_id_list = doc_id_list
        # Document library ID, used to filter documents/document chunks.
        # 
        # This parameter is required.
        self.library_id = library_id
        # OR expression, used to filter documents/document chunks.
        self.or_ = or_
        # Document status list, used to filter documents.
        self.status = status

    def validate(self):
        if self.and_:
            for v1 in self.and_:
                 if v1:
                    v1.validate()
        if self.or_:
            for v1 in self.or_:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['and'] = []
        if self.and_ is not None:
            for k1 in self.and_:
                result['and'].append(k1.to_map() if k1 else None)

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        result['or'] = []
        if self.or_ is not None:
            for k1 in self.or_:
                result['or'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k1 in m.get('and'):
                temp_model = main_models.RecallDocumentRequestFiltersAnd()
                self.and_.append(temp_model.from_map(k1))

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        self.or_ = []
        if m.get('or') is not None:
            for k1 in m.get('or'):
                temp_model = main_models.RecallDocumentRequestFiltersOr()
                self.or_.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class RecallDocumentRequestFiltersOr(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Keyword weight.
        self.boost = boost
        # The key of the metadata in the document library.
        self.key = key
        # The relationship between the value stored in the document library metadata key and the value you enter.
        # 
        # - eq: The value stored in the document library metadata key equals the value you enter.
        # 
        # - lte: The value stored in the document library metadata key is less than or equal to the value you enter.
        # 
        # - gte: The value stored in the document library metadata key is greater than or equal to the value you enter.
        # 
        # - lt: The value stored in the document library metadata key is less than the value you enter.
        # 
        # - gt: The value stored in the document library metadata key is greater than the value you enter.
        # 
        # - contains: The list of values stored in the document library metadata key contains the value you enter.
        self.operator = operator
        # The value of the metadata you enter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boost is not None:
            result['boost'] = self.boost

        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class RecallDocumentRequestFiltersAnd(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Keyword weight.
        self.boost = boost
        # The key of the metadata in the document library.
        self.key = key
        # The relationship between the value stored in the document library metadata key and the value you enter.
        # 
        # - eq: The value stored in the document library metadata key equals the value you enter.
        # 
        # - lte: The value stored in the document library metadata key is less than or equal to the value you enter.
        # 
        # - gte: The value stored in the document library metadata key is greater than or equal to the value you enter.
        # 
        # - lt: The value stored in the document library metadata key is less than the value you enter.
        # 
        # - gt: The value stored in the document library metadata key is greater than the value you enter.
        # 
        # - contains: The list of values stored in the document library metadata key contains the value you enter.
        self.operator = operator
        # The value of the metadata you enter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boost is not None:
            result['boost'] = self.boost

        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

