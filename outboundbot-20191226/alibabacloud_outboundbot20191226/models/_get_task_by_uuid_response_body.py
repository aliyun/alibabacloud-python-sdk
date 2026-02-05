# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetTaskByUuidResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task: main_models.GetTaskByUuidResponseBodyTask = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Task') is not None:
            temp_model = main_models.GetTaskByUuidResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class GetTaskByUuidResponseBodyTask(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        call_id: str = None,
        called_number: str = None,
        calling_number: str = None,
        conversations: List[main_models.GetTaskByUuidResponseBodyTaskConversations] = None,
        end_reason: str = None,
        end_time: int = None,
        id: str = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_id: str = None,
        planned_time: int = None,
    ):
        self.actual_time = actual_time
        self.call_id = call_id
        self.called_number = called_number
        self.calling_number = calling_number
        self.conversations = conversations
        self.end_reason = end_reason
        self.end_time = end_time
        self.id = id
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.planned_time = planned_time

    def validate(self):
        if self.conversations:
            for v1 in self.conversations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        result['Conversations'] = []
        if self.conversations is not None:
            for k1 in self.conversations:
                result['Conversations'].append(k1.to_map() if k1 else None)

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.planned_time is not None:
            result['PlannedTime'] = self.planned_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        self.conversations = []
        if m.get('Conversations') is not None:
            for k1 in m.get('Conversations'):
                temp_model = main_models.GetTaskByUuidResponseBodyTaskConversations()
                self.conversations.append(temp_model.from_map(k1))

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PlannedTime') is not None:
            self.planned_time = m.get('PlannedTime')

        return self

class GetTaskByUuidResponseBodyTaskConversations(DaraModel):
    def __init__(
        self,
        action: str = None,
        script: str = None,
        sequence_id: str = None,
        speaker: str = None,
        timestamp: int = None,
    ):
        self.action = action
        self.script = script
        self.sequence_id = sequence_id
        self.speaker = speaker
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.script is not None:
            result['Script'] = self.script

        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id

        if self.speaker is not None:
            result['Speaker'] = self.speaker

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')

        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

