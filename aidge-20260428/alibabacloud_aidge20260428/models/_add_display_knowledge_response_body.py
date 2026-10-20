# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class AddDisplayKnowledgeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddDisplayKnowledgeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The result of adding content to the display knowledge base.
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
            temp_model = main_models.AddDisplayKnowledgeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddDisplayKnowledgeResponseBodyData(DaraModel):
    def __init__(
        self,
        accepted_count: int = None,
        error_code: str = None,
        error_message: str = None,
        failed_count: int = None,
        knowledge_base_status: str = None,
        rag_id: str = None,
        results: List[main_models.AddDisplayKnowledgeResponseBodyDataResults] = None,
        success: bool = None,
        task_id: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The number of accepted records.
        self.accepted_count = accepted_count
        # The business error code.
        self.error_code = error_code
        # The business error message.
        self.error_message = error_message
        # The number of failed records.
        self.failed_count = failed_count
        # The knowledge base status.
        self.knowledge_base_status = knowledge_base_status
        # The knowledge base ID.
        self.rag_id = rag_id
        # The processing results for each record.
        self.results = results
        # Indicates whether the business processing is successful.
        self.success = success
        # The asynchronous task ID. This parameter is empty for synchronous API operations.
        self.task_id = task_id
        # The usage information. This parameter is empty for free API operations.
        self.usage_map = usage_map

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
        if self.accepted_count is not None:
            result['AcceptedCount'] = self.accepted_count

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.knowledge_base_status is not None:
            result['KnowledgeBaseStatus'] = self.knowledge_base_status

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptedCount') is not None:
            self.accepted_count = m.get('AcceptedCount')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('KnowledgeBaseStatus') is not None:
            self.knowledge_base_status = m.get('KnowledgeBaseStatus')

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.AddDisplayKnowledgeResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class AddDisplayKnowledgeResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        index: int = None,
        record_id: int = None,
        sku_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The failure error code.
        self.error_code = error_code
        # The failure reason.
        self.error_message = error_message
        # The index in the original request array.
        self.index = index
        # The record ID.
        self.record_id = record_id
        # The effective SKU ID.
        self.sku_id = sku_id
        # The record status.
        self.status = status
        # Indicates whether the record is accepted.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.index is not None:
            result['Index'] = self.index

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

