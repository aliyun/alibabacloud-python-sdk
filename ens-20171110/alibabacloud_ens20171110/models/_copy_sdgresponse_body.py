# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CopySDGResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CopySDGResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data object.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CopySDGResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CopySDGResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        result: main_models.CopySDGResponseBodyDataResult = None,
        success: bool = None,
    ):
        # The response message. Success is returned for a successful request.
        self.message = message
        # The execution result of the synchronization request.
        self.result = result
        # Indicates whether all tasks are successful. Valid values:
        # 
        # *   **true**: All tasks are successful.
        # *   **false**: Failed tasks exist.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            temp_model = main_models.CopySDGResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CopySDGResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        failed_items: List[main_models.CopySDGResponseBodyDataResultFailedItems] = None,
        success_count: int = None,
    ):
        # The number of failed nodes.
        self.failed_count = failed_count
        # Details of failed nodes.
        self.failed_items = failed_items
        # The number of successful nodes.
        self.success_count = success_count

    def validate(self):
        if self.failed_items:
            for v1 in self.failed_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['FailedItems'] = []
        if self.failed_items is not None:
            for k1 in self.failed_items:
                result['FailedItems'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.failed_items = []
        if m.get('FailedItems') is not None:
            for k1 in m.get('FailedItems'):
                temp_model = main_models.CopySDGResponseBodyDataResultFailedItems()
                self.failed_items.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class CopySDGResponseBodyDataResultFailedItems(DaraModel):
    def __init__(
        self,
        destination_region_id: str = None,
        error_message: str = None,
    ):
        # The ID of the destination node.
        self.destination_region_id = destination_region_id
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

