# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class QueryDisplayKnowledgeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryDisplayKnowledgeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The query result of the display knowledge base content.
        self.data = data
        # The returned message or failure description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryDisplayKnowledgeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDisplayKnowledgeResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        knowledge_base_status: str = None,
        page_num: int = None,
        page_size: int = None,
        rag_id: str = None,
        records: List[main_models.QueryDisplayKnowledgeResponseBodyDataRecords] = None,
        success: bool = None,
        task_id: str = None,
        total: int = None,
        total_page: int = None,
        usage_map: Dict[str, int] = None,
    ):
        # The business error code.
        self.error_code = error_code
        # The business error message.
        self.error_message = error_message
        # The knowledge base status.
        self.knowledge_base_status = knowledge_base_status
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The knowledge base ID.
        self.rag_id = rag_id
        # The records on the current page.
        self.records = records
        # Indicates whether the business processing is successful.
        self.success = success
        # The asynchronous task ID. This parameter is empty for synchronous API operations.
        self.task_id = task_id
        # The total number of records.
        self.total = total
        # The total number of pages.
        self.total_page = total_page
        # The usage information. This parameter is empty for free API operations.
        self.usage_map = usage_map

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.knowledge_base_status is not None:
            result['KnowledgeBaseStatus'] = self.knowledge_base_status

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total is not None:
            result['Total'] = self.total

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('KnowledgeBaseStatus') is not None:
            self.knowledge_base_status = m.get('KnowledgeBaseStatus')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.QueryDisplayKnowledgeResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class QueryDisplayKnowledgeResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        failure_message: str = None,
        failure_reason: str = None,
        gmt_modified: str = None,
        image_url: str = None,
        image_url_expire_time: str = None,
        record_id: int = None,
        sku_id: str = None,
        sku_name: str = None,
        status: str = None,
    ):
        # The description of the failure cause. This parameter is returned only when the status is FAILED.
        self.failure_message = failure_message
        # The code of the failure cause. This parameter is returned only when the status is FAILED.
        self.failure_reason = failure_reason
        # The last modified time.
        self.gmt_modified = gmt_modified
        # The 24-hour signed URL of the transferred image.
        self.image_url = image_url
        # The expiration time of the signed URL.
        self.image_url_expire_time = image_url_expire_time
        # The record ID.
        self.record_id = record_id
        # SKU ID
        self.sku_id = sku_id
        # The SKU name.
        self.sku_name = sku_name
        # The record status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_message is not None:
            result['FailureMessage'] = self.failure_message

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.image_url_expire_time is not None:
            result['ImageUrlExpireTime'] = self.image_url_expire_time

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureMessage') is not None:
            self.failure_message = m.get('FailureMessage')

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageUrlExpireTime') is not None:
            self.image_url_expire_time = m.get('ImageUrlExpireTime')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

