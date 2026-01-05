# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeTasksResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The objects that are returned.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        failed_child_count: int = None,
        finish_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        invoke_id: str = None,
        level: int = None,
        operator: str = None,
        param: str = None,
        parent_task_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        result: str = None,
        running_child_count: int = None,
        start_time: str = None,
        success_child_count: int = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
        total_child_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The total number of failed subtasks.
        self.failed_child_count = failed_child_count
        # The end time of the task.
        self.finish_time = finish_time
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        # The name of the cloud phone instance.
        self.instance_name = instance_name
        # The state of the cloud phone instance.
        self.instance_status = instance_status
        # The ID of the command execution.
        self.invoke_id = invoke_id
        # The level of the task.
        self.level = level
        # The operator.
        self.operator = operator
        # The parameters of the task.
        self.param = param
        # The ID of the parent task.
        self.parent_task_id = parent_task_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The execution result of the task.
        self.result = result
        # The total number of the subtasks that are running.
        self.running_child_count = running_child_count
        # The start time of the task.
        self.start_time = start_time
        # The total number of successfully executed subtasks.
        self.success_child_count = success_child_count
        # The ID of the task.
        self.task_id = task_id
        # The state of the task.
        self.task_status = task_status
        # The type of the task.
        self.task_type = task_type
        # The total number of subtasks of the current batch task.
        self.total_child_count = total_child_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.failed_child_count is not None:
            result['FailedChildCount'] = self.failed_child_count

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.level is not None:
            result['Level'] = self.level

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.param is not None:
            result['Param'] = self.param

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.result is not None:
            result['Result'] = self.result

        if self.running_child_count is not None:
            result['RunningChildCount'] = self.running_child_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.success_child_count is not None:
            result['SuccessChildCount'] = self.success_child_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_child_count is not None:
            result['TotalChildCount'] = self.total_child_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('FailedChildCount') is not None:
            self.failed_child_count = m.get('FailedChildCount')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RunningChildCount') is not None:
            self.running_child_count = m.get('RunningChildCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SuccessChildCount') is not None:
            self.success_child_count = m.get('SuccessChildCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalChildCount') is not None:
            self.total_child_count = m.get('TotalChildCount')

        return self

