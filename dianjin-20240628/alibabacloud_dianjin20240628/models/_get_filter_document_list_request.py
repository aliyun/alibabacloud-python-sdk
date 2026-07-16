# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetFilterDocumentListRequest(DaraModel):
    def __init__(
        self,
        and_: List[main_models.GetFilterDocumentListRequestAnd] = None,
        doc_id_list: List[str] = None,
        library_id: str = None,
        or_: List[main_models.GetFilterDocumentListRequestOr] = None,
        page: int = None,
        page_size: int = None,
        status: List[str] = None,
    ):
        # AND expression to filter documents or document chunks.
        self.and_ = and_
        # List of document IDs to filter documents or document chunks.
        self.doc_id_list = doc_id_list
        # Document library ID to filter documents or document chunks.
        # 
        # This parameter is required.
        self.library_id = library_id
        # OR expression to filter documents or document chunks.
        self.or_ = or_
        # Page number for pagination.
        self.page = page
        # Number of records per page for pagination.
        self.page_size = page_size
        # List of document statuses to filter documents.
        # 
        # ### Document parsing status codes
        # 
        # *Status codes: WaitRefresh, InQueue, FetchingData, Embedding, Completed, FormatError, Error*
        # 
        # - Completed: Active. Document parsing completed.
        # 
        # - Error: Inactive. Document parsing failed.
        # 
        # - FormatError: File format error. Re-upload the file in the correct format if it is encrypted or incomplete.
        # 
        # - InQueue: Pending. Document is waiting for parsing.
        # 
        # - Parsed: Parsing completed.
        # 
        # - Other statuses are internal system states. For example, WaitRefresh means the task is scheduled. FetchingData means parsing is in progress. Embedding means index building is in progress.
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

        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        result['or'] = []
        if self.or_ is not None:
            for k1 in self.or_:
                result['or'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k1 in m.get('and'):
                temp_model = main_models.GetFilterDocumentListRequestAnd()
                self.and_.append(temp_model.from_map(k1))

        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        self.or_ = []
        if m.get('or') is not None:
            for k1 in m.get('or'):
                temp_model = main_models.GetFilterDocumentListRequestOr()
                self.or_.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetFilterDocumentListRequestOr(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Weight of the value in the text retrieval engine. Default is 1.
        self.boost = boost
        # Metadata key in the document library.
        self.key = key
        # ### Relationship between the stored metadata value and your input value
        # 
        # - eq: The stored metadata value equals your input value.
        # 
        # - contains: The stored metadata value list contains your input value.
        self.operator = operator
        # Input metadata value.
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

class GetFilterDocumentListRequestAnd(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Weight of the value in the text retrieval engine. Default is 1.
        self.boost = boost
        # Metadata key in the document library.
        self.key = key
        # ### Relationship between the stored metadata value and your input value
        # 
        # - eq: The stored metadata value equals your input value.
        # 
        # - contains: The stored metadata value list contains your input value.
        self.operator = operator
        # Input metadata value.
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

