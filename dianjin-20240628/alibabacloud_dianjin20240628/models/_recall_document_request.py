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
        self.filters = filters
        # This parameter is required.
        self.query = query
        self.rearrangement = rearrangement
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
        self.and_ = and_
        self.chunk_type = chunk_type
        self.doc_id_list = doc_id_list
        # This parameter is required.
        self.library_id = library_id
        self.or_ = or_
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
        self.boost = boost
        self.key = key
        self.operator = operator
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
        self.boost = boost
        self.key = key
        self.operator = operator
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

