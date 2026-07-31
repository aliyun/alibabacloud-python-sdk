# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetAutoOpsTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.GetAutoOpsTaskResponseBodyTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the O&M task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            temp_model = main_models.GetAutoOpsTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class GetAutoOpsTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        allowed_over_time: int = None,
        comment: str = None,
        name: str = None,
        schedule_time_info: str = None,
        schedule_type: str = None,
        script: str = None,
        script_id: int = None,
        script_name: str = None,
        script_type: str = None,
        task_id: str = None,
        task_state: str = None,
    ):
        # The time when the approval of the O&M task was completed. This value is a UNIX timestamp. Unit: seconds.
        self.allowed_over_time = allowed_over_time
        # The remarks of the O&M task.
        self.comment = comment
        # The name of the O&M task.
        self.name = name
        # The execution plan of the O&M task.
        # - **ExecAt**: If the value of ScheduleType is Manual, this parameter is not meaningful. If the value of ScheduleType is FixTime, this parameter indicates the scheduled execution time in seconds as a UNIX timestamp. If the value of ScheduleType is CycleInterval, this parameter indicates the first execution time in seconds as a UNIX timestamp.
        # 
        # - **PeriodNum**: If the value of ScheduleType is Manual or FixTime, this parameter is not meaningful. If the value of ScheduleType is CycleInterval, this parameter indicates the interval for periodic execution.
        # 
        # - **PeriodUnit**: If the value of ScheduleType is Manual or FixTime, this parameter is not meaningful. If the value of ScheduleType is CycleInterval, this parameter indicates the unit of the periodic execution interval. Valid values: hour and day.
        self.schedule_time_info = schedule_time_info
        # The scheduling type of the task.
        # - **FixTime**: scheduled execution.
        # - **CycleInterval**: periodic execution.
        # - **Manual**: manual execution triggered by the user.
        self.schedule_type = schedule_type
        # The content of the script to be executed by the O&M task. The value is Base64-encoded.
        self.script = script
        # The ID of the script associated with the O&M task. This parameter is returned only when ScriptType is set to SpecificScript.
        self.script_id = script_id
        # The name of the script associated with the O&M task.
        self.script_name = script_name
        # The script type of the O&M task.
        # 
        # - **HandInput**: manually entered script.
        # 
        # - **SpecificScript**: associated existing script.
        self.script_type = script_type
        # The ID of the O&M task.
        self.task_id = task_id
        # The status of the O&M task.
        # 
        # - **PendingApproval**: pending approval.
        # - **Rejected**: rejected.
        # - **Cancelled**: cancelled.
        # - **PendingExecution**: approved and waiting for execution.
        # - **PrepareRun**: preparing to execute.
        # - **Running**: executing.
        # - **Completed**: execution completed.
        # - **Failed**: execution failed.
        self.task_state = task_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_over_time is not None:
            result['AllowedOverTime'] = self.allowed_over_time

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule_time_info is not None:
            result['ScheduleTimeInfo'] = self.schedule_time_info

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.script is not None:
            result['Script'] = self.script

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedOverTime') is not None:
            self.allowed_over_time = m.get('AllowedOverTime')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduleTimeInfo') is not None:
            self.schedule_time_info = m.get('ScheduleTimeInfo')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        return self

