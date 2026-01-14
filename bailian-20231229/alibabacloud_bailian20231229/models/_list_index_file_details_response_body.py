# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListIndexFileDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIndexFileDetailsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIndexFileDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIndexFileDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.ListIndexFileDetailsResponseBodyDataDocuments] = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.documents = documents
        self.index_id = index_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.ListIndexFileDetailsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIndexFileDetailsResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        chunk_mode: str = None,
        chunk_size: str = None,
        code: str = None,
        document_type: str = None,
        enable_headers: str = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        overlap_size: str = None,
        size: int = None,
        source_id: str = None,
        status: str = None,
        separator: str = None,
    ):
        self.chunk_mode = chunk_mode
        self.chunk_size = chunk_size
        self.code = code
        self.document_type = document_type
        self.enable_headers = enable_headers
        self.gmt_modified = gmt_modified
        self.id = id
        self.message = message
        self.name = name
        self.overlap_size = overlap_size
        self.size = size
        self.source_id = source_id
        self.status = status
        self.separator = separator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.code is not None:
            result['Code'] = self.code

        if self.document_type is not None:
            result['DocumentType'] = self.document_type

        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.size is not None:
            result['Size'] = self.size

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.status is not None:
            result['Status'] = self.status

        if self.separator is not None:
            result['separator'] = self.separator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')

        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('separator') is not None:
            self.separator = m.get('separator')

        return self

