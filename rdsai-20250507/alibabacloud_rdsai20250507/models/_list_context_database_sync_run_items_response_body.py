# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseSyncRunItemsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListContextDatabaseSyncRunItemsResponseBodyData = None,
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
        # Indicates whether the request succeeded.
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
            temp_model = main_models.ListContextDatabaseSyncRunItemsResponseBodyData()
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

class ListContextDatabaseSyncRunItemsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListContextDatabaseSyncRunItemsResponseBodyDataItems] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The data list.
        self.items = items
        # The page number. Pages start from 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListContextDatabaseSyncRunItemsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListContextDatabaseSyncRunItemsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        artifact_index: int = None,
        ctxdb_document_id: str = None,
        decision: str = None,
        decision_category: str = None,
        provider_document_id: str = None,
        reason: str = None,
        size_bytes: int = None,
        source_path: str = None,
        source_record_id: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        # The document shard index.
        self.artifact_index = artifact_index
        # The ContextDB document ID.
        self.ctxdb_document_id = ctxdb_document_id
        # The fine-grained execution status of the current synchronization item, which indicates the processing result of a single document in the current run. Common valid values include uploaded, uploaded-pending-review, upload-accepted, upload-busy, metadata-updating, metadata-updated, migrated, failed, source-failed, replace, warning, deferred, resume, skip, skipped, unsupported, and cancelled.
        self.decision = decision
        # The aggregated display status of the current synchronization item. Known mappings include success, failure, processing, and skipped. Unknown Decision values are passed through as-is.
        self.decision_category = decision_category
        # The source document ID.
        self.provider_document_id = provider_document_id
        # The processing reason or failure reason.
        self.reason = reason
        # The size in bytes.
        self.size_bytes = size_bytes
        # The source path.
        self.source_path = source_path
        # The source record ID.
        self.source_record_id = source_record_id
        # The title.
        self.title = title
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_index is not None:
            result['ArtifactIndex'] = self.artifact_index

        if self.ctxdb_document_id is not None:
            result['CtxdbDocumentId'] = self.ctxdb_document_id

        if self.decision is not None:
            result['Decision'] = self.decision

        if self.decision_category is not None:
            result['DecisionCategory'] = self.decision_category

        if self.provider_document_id is not None:
            result['ProviderDocumentId'] = self.provider_document_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        if self.source_record_id is not None:
            result['SourceRecordId'] = self.source_record_id

        if self.title is not None:
            result['Title'] = self.title

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactIndex') is not None:
            self.artifact_index = m.get('ArtifactIndex')

        if m.get('CtxdbDocumentId') is not None:
            self.ctxdb_document_id = m.get('CtxdbDocumentId')

        if m.get('Decision') is not None:
            self.decision = m.get('Decision')

        if m.get('DecisionCategory') is not None:
            self.decision_category = m.get('DecisionCategory')

        if m.get('ProviderDocumentId') is not None:
            self.provider_document_id = m.get('ProviderDocumentId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('SourceRecordId') is not None:
            self.source_record_id = m.get('SourceRecordId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

