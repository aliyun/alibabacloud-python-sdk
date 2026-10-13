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
        # The API status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The task information.
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
        # The actual execution time. The value is a UNIX timestamp in milliseconds.
        self.actual_time = actual_time
        # The call ID.
        self.call_id = call_id
        # The called number.
        self.called_number = called_number
        # The calling number.
        self.calling_number = calling_number
        # The list of conversation information.
        self.conversations = conversations
        # The end reason. Valid values:
        # - FINISHED: normal completion.
        # - CHATBOT_HANGUP_AFTER_NOANSWER: the robot hangs up after unrecognized input.
        # - CHATBOT_HANGUP_AFTER_SILENCE: the robot hangs up after a silence timeout.
        # - CLIENT_HANGUP_AFTER_NOANSWER: the user hangs up after unrecognized input.
        # - CLIENT_HANGUP: the user hangs up without a reason.
        # - TRANSFER_BY_INTENT: the call is transferred to a human agent due to intent matching.
        # - TRANSFER_AFTER_NOANSWER: the call is transferred to a human agent after unrecognized input.
        # - INO_INTERACTION: no interaction from the user.
        # - ERROR: the system is interrupted due to an exception.
        # - SPECIAL_INTERCEPT_VOICE_ASSISTANT: intercepted due to special circumstances - voice assistant.
        # - SPECIAL_INTERCEPT_EXTENSION_NUMBER_TRANSFER: intercepted due to special circumstances - extension number transfer.
        # 
        # >Notice: The data type of this parameter is String. The returned value is an enumerated value such as FINISHED.</notice>
        self.end_reason = end_reason
        # The end time. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The task ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The job group ID.
        self.job_group_id = job_group_id
        # The job ID.
        self.job_id = job_id
        # **[Deprecated]** The planned execution time of the task. The value is a UNIX timestamp in milliseconds.
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
        # The instruction. Valid values:
        # - BeginDialogue: starts the conversation.
        # - Dialogue: indicates a conversation.
        # - AbortDialogue: aborts the conversation.
        # - SilenceTimeout: indicates a silence timeout.
        # - CollectedNumber: indicates a collected number.
        # - EndDialogue: ends the conversation.
        # - Broadcast: indicates an opening remark.
        # - HangUp: hangs up the call.
        # - Authorize: grants authorization.
        # - TransferToAgent: transfers the call to an agent.
        # - TransferToIVR: transfers the call to an IVR.
        # - RedirectToPage: redirects to a page.
        # - CollectNumber: collects a number.
        # - WaitOnAsyncTask: waits for an asynchronous task.
        # - Error: indicates an error.
        self.action = action
        # The conversation text.
        self.script = script
        # The session ID.
        self.sequence_id = sequence_id
        # The speaker of the conversation. Valid values: Robot and Contact.
        self.speaker = speaker
        # The time when the summary was created. The value is a UNIX timestamp in milliseconds.
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

