# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStackGroupOperationsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_group_operations: List[main_models.ListStackGroupOperationsResponseBodyStackGroupOperations] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stack group operations.
        self.stack_group_operations = stack_group_operations
        # The total number of stack group operations.
        self.total_count = total_count

    def validate(self):
        if self.stack_group_operations:
            for v1 in self.stack_group_operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StackGroupOperations'] = []
        if self.stack_group_operations is not None:
            for k1 in self.stack_group_operations:
                result['StackGroupOperations'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stack_group_operations = []
        if m.get('StackGroupOperations') is not None:
            for k1 in m.get('StackGroupOperations'):
                temp_model = main_models.ListStackGroupOperationsResponseBodyStackGroupOperations()
                self.stack_group_operations.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStackGroupOperationsResponseBodyStackGroupOperations(DaraModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        end_time: str = None,
        operation_description: str = None,
        operation_id: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
    ):
        # The operation type.
        # 
        # Valid values:
        # 
        # *   CREATE
        # *   UPDATE
        # *   DELETE
        # *   DETECT_DRIFT
        self.action = action
        # The time when the operation was initiated.
        self.create_time = create_time
        # The time when the operation ended.
        self.end_time = end_time
        # The description of the operation.
        self.operation_description = operation_description
        # The operation ID.
        self.operation_id = operation_id
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   SUCCEEDED
        # *   FAILED
        # *   STOPPING
        # *   STOPPED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

