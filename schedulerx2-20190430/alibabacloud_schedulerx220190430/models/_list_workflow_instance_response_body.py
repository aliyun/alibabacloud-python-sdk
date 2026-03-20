# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListWorkflowInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about workflow instances.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.ListWorkflowInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWorkflowInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        wf_instance_infos: List[main_models.ListWorkflowInstanceResponseBodyDataWfInstanceInfos] = None,
    ):
        # The workflow instances.
        self.wf_instance_infos = wf_instance_infos

    def validate(self):
        if self.wf_instance_infos:
            for v1 in self.wf_instance_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WfInstanceInfos'] = []
        if self.wf_instance_infos is not None:
            for k1 in self.wf_instance_infos:
                result['WfInstanceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.wf_instance_infos = []
        if m.get('WfInstanceInfos') is not None:
            for k1 in m.get('WfInstanceInfos'):
                temp_model = main_models.ListWorkflowInstanceResponseBodyDataWfInstanceInfos()
                self.wf_instance_infos.append(temp_model.from_map(k1))

        return self

class ListWorkflowInstanceResponseBodyDataWfInstanceInfos(DaraModel):
    def __init__(
        self,
        data_time: str = None,
        end_time: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        wf_instance_id: int = None,
        workflow_id: int = None,
    ):
        # The data timestamp of the workflow instance.
        self.data_time = data_time
        # The time when the workflow instance stopped running.
        self.end_time = end_time
        # The time when the workflow instance was scheduled to run.
        self.schedule_time = schedule_time
        # The time when the workflow instance started to run.
        self.start_time = start_time
        # The state of the workflow instance. Valid values:
        # 
        # *   1: pending
        # *   2: preparing
        # *   3: running
        # *   4: successful
        # *   5: failed
        self.status = status
        # The workflow instance ID.
        self.wf_instance_id = wf_instance_id
        # The workflow ID.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

