# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetBaselineStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBaselineStatusResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the baseline instance.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The unique ID of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetBaselineStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBaselineStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
        bizdate: int = None,
        block_instance: main_models.GetBaselineStatusResponseBodyDataBlockInstance = None,
        buffer: float = None,
        end_cast: int = None,
        exp_time: int = None,
        finish_status: str = None,
        finish_time: int = None,
        in_group_id: int = None,
        last_instance: main_models.GetBaselineStatusResponseBodyDataLastInstance = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        sla_time: int = None,
        status: str = None,
    ):
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The business date timestamp.
        self.bizdate = bizdate
        # The information about the critical instance.
        self.block_instance = block_instance
        # The buffer time of the baseline instance, in seconds.
        self.buffer = buffer
        # The estimated completion timestamp of the baseline instance.
        self.end_cast = end_cast
        # The warning timestamp of the baseline instance.
        self.exp_time = exp_time
        # Indicates whether the baseline instance is completed. Valid values: UNFINISH and FINISH.
        self.finish_status = finish_status
        # The completion timestamp of the baseline instance. This parameter is returned only when FinishStatus is FINISH.
        self.finish_time = finish_time
        # The cycle number of the baseline instance. The value is 1 for daily baselines. The value ranges from [1,24\\] for hourly baselines.
        self.in_group_id = in_group_id
        # The information about the latest instance.
        self.last_instance = last_instance
        # The Alibaba Cloud UID of the baseline owner. Multiple owners are separated by commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 2, 5, 7, and 8.
        self.priority = priority
        # The ID of the workspace to which the baseline belongs.
        self.project_id = project_id
        # The committed completion timestamp of the baseline instance.
        self.sla_time = sla_time
        # The status of the baseline. Valid values: ERROR, SAFE, DANGROUS (warning), and OVER (exceeded).
        self.status = status

    def validate(self):
        if self.block_instance:
            self.block_instance.validate()
        if self.last_instance:
            self.last_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.block_instance is not None:
            result['BlockInstance'] = self.block_instance.to_map()

        if self.buffer is not None:
            result['Buffer'] = self.buffer

        if self.end_cast is not None:
            result['EndCast'] = self.end_cast

        if self.exp_time is not None:
            result['ExpTime'] = self.exp_time

        if self.finish_status is not None:
            result['FinishStatus'] = self.finish_status

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        if self.last_instance is not None:
            result['LastInstance'] = self.last_instance.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sla_time is not None:
            result['SlaTime'] = self.sla_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('BlockInstance') is not None:
            temp_model = main_models.GetBaselineStatusResponseBodyDataBlockInstance()
            self.block_instance = temp_model.from_map(m.get('BlockInstance'))

        if m.get('Buffer') is not None:
            self.buffer = m.get('Buffer')

        if m.get('EndCast') is not None:
            self.end_cast = m.get('EndCast')

        if m.get('ExpTime') is not None:
            self.exp_time = m.get('ExpTime')

        if m.get('FinishStatus') is not None:
            self.finish_status = m.get('FinishStatus')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        if m.get('LastInstance') is not None:
            temp_model = main_models.GetBaselineStatusResponseBodyDataLastInstance()
            self.last_instance = temp_model.from_map(m.get('LastInstance'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SlaTime') is not None:
            self.sla_time = m.get('SlaTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetBaselineStatusResponseBodyDataLastInstance(DaraModel):
    def __init__(
        self,
        end_cast: int = None,
        finish_time: int = None,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The estimated completion timestamp of the instance.
        self.end_cast = end_cast
        # The actual completion timestamp of the instance.
        self.finish_time = finish_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The Alibaba Cloud UID of the node owner.
        self.owner = owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The status of the instance. Valid values: NOT_RUN, WAIT_TIME, WAIT_RESOURCE, RUNNING, CHECKING, CHECKING_CONDITION, FAILURE, and SUCCESS.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_cast is not None:
            result['EndCast'] = self.end_cast

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndCast') is not None:
            self.end_cast = m.get('EndCast')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetBaselineStatusResponseBodyDataBlockInstance(DaraModel):
    def __init__(
        self,
        end_cast: int = None,
        finish_time: int = None,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The estimated completion timestamp of the instance.
        self.end_cast = end_cast
        # The actual completion timestamp of the instance.
        self.finish_time = finish_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The Alibaba Cloud UID of the node owner.
        self.owner = owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The status of the instance. Valid values: NOT_RUN, WAIT_TIME, WAIT_RESOURCE, RUNNING, CHECKING, CHECKING_CONDITION, FAILURE, and SUCCESS.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_cast is not None:
            result['EndCast'] = self.end_cast

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndCast') is not None:
            self.end_cast = m.get('EndCast')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

