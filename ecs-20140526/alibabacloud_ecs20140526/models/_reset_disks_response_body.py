# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ResetDisksResponseBody(DaraModel):
    def __init__(
        self,
        operation_progress_set: main_models.ResetDisksResponseBodyOperationProgressSet = None,
        request_id: str = None,
    ):
        # Details about the rollback operation.
        self.operation_progress_set = operation_progress_set
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.operation_progress_set:
            self.operation_progress_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_progress_set is not None:
            result['OperationProgressSet'] = self.operation_progress_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationProgressSet') is not None:
            temp_model = main_models.ResetDisksResponseBodyOperationProgressSet()
            self.operation_progress_set = temp_model.from_map(m.get('OperationProgressSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ResetDisksResponseBodyOperationProgressSet(DaraModel):
    def __init__(
        self,
        operation_progress: List[main_models.ResetDisksResponseBodyOperationProgressSetOperationProgress] = None,
    ):
        self.operation_progress = operation_progress

    def validate(self):
        if self.operation_progress:
            for v1 in self.operation_progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationProgress'] = []
        if self.operation_progress is not None:
            for k1 in self.operation_progress:
                result['OperationProgress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_progress = []
        if m.get('OperationProgress') is not None:
            for k1 in m.get('OperationProgress'):
                temp_model = main_models.ResetDisksResponseBodyOperationProgressSetOperationProgress()
                self.operation_progress.append(temp_model.from_map(k1))

        return self

class ResetDisksResponseBodyOperationProgressSetOperationProgress(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        operation_status: str = None,
        related_item_set: main_models.ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet = None,
    ):
        # The error code that is returned if the request failed. This parameter is empty if the request is successful.
        # 
        # For information about error codes and error messages, see [Service error codes](https://error-center.alibabacloud.com/status/product/Ecs).
        self.error_code = error_code
        # The error message that is returned if the request failed. This parameter is empty if the request is successful.
        # 
        # For information about error codes and error messages, see [Service error codes](https://error-center.alibabacloud.com/status/product/Ecs).
        self.error_msg = error_msg
        # Indicates whether the request is successful. If the request is successful, Success is returned. If the request failed, an error code and an error message are returned.
        self.operation_status = operation_status
        # Details about the resources.
        self.related_item_set = related_item_set

    def validate(self):
        if self.related_item_set:
            self.related_item_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.related_item_set is not None:
            result['RelatedItemSet'] = self.related_item_set.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('RelatedItemSet') is not None:
            temp_model = main_models.ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet()
            self.related_item_set = temp_model.from_map(m.get('RelatedItemSet'))

        return self

class ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSet(DaraModel):
    def __init__(
        self,
        related_item: List[main_models.ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem] = None,
    ):
        self.related_item = related_item

    def validate(self):
        if self.related_item:
            for v1 in self.related_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RelatedItem'] = []
        if self.related_item is not None:
            for k1 in self.related_item:
                result['RelatedItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_item = []
        if m.get('RelatedItem') is not None:
            for k1 in m.get('RelatedItem'):
                temp_model = main_models.ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem()
                self.related_item.append(temp_model.from_map(k1))

        return self

class ResetDisksResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The resource name.
        self.name = name
        # The resource ID.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

