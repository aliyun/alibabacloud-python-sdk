# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class RetryKnowledgeBaseFilesResponseBody(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        items: List[main_models.RetryKnowledgeBaseFilesResponseBodyItems] = None,
        request_id: str = None,
        succeeded_count: int = None,
        total_count: int = None,
    ):
        self.failed_count = failed_count
        self.items = items
        self.request_id = request_id
        self.succeeded_count = succeeded_count
        self.total_count = total_count

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
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.succeeded_count is not None:
            result['SucceededCount'] = self.succeeded_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.RetryKnowledgeBaseFilesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SucceededCount') is not None:
            self.succeeded_count = m.get('SucceededCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class RetryKnowledgeBaseFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.file_id = file_id
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

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

