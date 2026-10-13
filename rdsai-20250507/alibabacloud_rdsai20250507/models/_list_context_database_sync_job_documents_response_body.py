# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseSyncJobDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListContextDatabaseSyncJobDocumentsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListContextDatabaseSyncJobDocumentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListContextDatabaseSyncJobDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.ListContextDatabaseSyncJobDocumentsResponseBodyDataDocuments] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of documents.
        self.documents = documents
        # The page number, starting from 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

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

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.ListContextDatabaseSyncJobDocumentsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListContextDatabaseSyncJobDocumentsResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        content_hash: str = None,
        ctxdb_document_id: str = None,
        provider_document_id: str = None,
        retired_at: str = None,
        source_update_time: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The content hash.
        self.content_hash = content_hash
        # The ContextDB document ID.
        self.ctxdb_document_id = ctxdb_document_id
        # The source document ID.
        self.provider_document_id = provider_document_id
        # The retirement time.
        self.retired_at = retired_at
        # The source update time.
        self.source_update_time = source_update_time
        # The status.
        self.status = status
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_hash is not None:
            result['ContentHash'] = self.content_hash

        if self.ctxdb_document_id is not None:
            result['CtxdbDocumentId'] = self.ctxdb_document_id

        if self.provider_document_id is not None:
            result['ProviderDocumentId'] = self.provider_document_id

        if self.retired_at is not None:
            result['RetiredAt'] = self.retired_at

        if self.source_update_time is not None:
            result['SourceUpdateTime'] = self.source_update_time

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentHash') is not None:
            self.content_hash = m.get('ContentHash')

        if m.get('CtxdbDocumentId') is not None:
            self.ctxdb_document_id = m.get('CtxdbDocumentId')

        if m.get('ProviderDocumentId') is not None:
            self.provider_document_id = m.get('ProviderDocumentId')

        if m.get('RetiredAt') is not None:
            self.retired_at = m.get('RetiredAt')

        if m.get('SourceUpdateTime') is not None:
            self.source_update_time = m.get('SourceUpdateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

