# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeTaskAttributeResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        failed_count: int = None,
        finished_time: str = None,
        operation_progress_set: main_models.DescribeTaskAttributeResponseBodyOperationProgressSet = None,
        region_id: str = None,
        request_id: str = None,
        success_count: int = None,
        support_cancel: str = None,
        task_action: str = None,
        task_id: str = None,
        task_process: str = None,
        task_status: str = None,
        total_count: int = None,
    ):
        # The time when the task was created.
        self.creation_time = creation_time
        # The number of failed tasks.
        self.failed_count = failed_count
        # The time when the task was completed.
        self.finished_time = finished_time
        # The return data of the task.
        self.operation_progress_set = operation_progress_set
        # The region ID of the task.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The number of completed tasks.
        self.success_count = success_count
        # Indicates whether the task can be canceled by calling the [CancelTask](https://help.aliyun.com/document_detail/25624.html) operation. Valid values:
        # 
        # *   true
        # *   false
        self.support_cancel = support_cancel
        # The name of the operation that generated the task.
        self.task_action = task_action
        # The ID of the task.
        self.task_id = task_id
        # The progress of the task.
        self.task_process = task_process
        # The status of the task.
        self.task_status = task_status
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.operation_progress_set:
            self.operation_progress_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.operation_progress_set is not None:
            result['OperationProgressSet'] = self.operation_progress_set.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.support_cancel is not None:
            result['SupportCancel'] = self.support_cancel

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_process is not None:
            result['TaskProcess'] = self.task_process

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('OperationProgressSet') is not None:
            temp_model = main_models.DescribeTaskAttributeResponseBodyOperationProgressSet()
            self.operation_progress_set = temp_model.from_map(m.get('OperationProgressSet'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('SupportCancel') is not None:
            self.support_cancel = m.get('SupportCancel')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTaskAttributeResponseBodyOperationProgressSet(DaraModel):
    def __init__(
        self,
        operation_progress: List[main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress] = None,
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
                temp_model = main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress()
                self.operation_progress.append(temp_model.from_map(k1))

        return self

class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgress(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        operation_status: str = None,
        related_item_set: main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The status of the operation.
        self.operation_status = operation_status
        # The type of resource information.
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
            temp_model = main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet()
            self.related_item_set = temp_model.from_map(m.get('RelatedItemSet'))

        return self

class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSet(DaraModel):
    def __init__(
        self,
        related_item: List[main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem] = None,
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
                temp_model = main_models.DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem()
                self.related_item.append(temp_model.from_map(k1))

        return self

class DescribeTaskAttributeResponseBodyOperationProgressSetOperationProgressRelatedItemSetRelatedItem(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the related item.
        self.name = name
        # The value of the related item.
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

