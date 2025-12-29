# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotTaskCallDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The call details of a robocall task, in the JSON format.
        # 
        # *   **taskId**: the unique ID of the robocall task.
        # *   **caller**: the calling number.
        # *   **called**: the called number.
        # *   **duration**: the call duration. Unit: seconds.
        # *   **label**: the label of the called party.
        # *   **dialogCount**: the number of conversation rounds in the call.
        # *   **callResult**: the call result.
        # *   **hangupDirection**: the party who hung up. Valid values: **0**: the robot. **1**: the called party.
        # *   **transferResult**: the result of transferring the call to an agent. Valid values: **1**, **0**, and **3**. The value 1 indicates that the call was transferred to the agent. The value 0 indicates that the call failed to be transferred to the agent. The value 3 indicates that the call was not transferred to the agent.
        # *   **transferNumber**: the phone number of the agent to whom the call was transferred.
        # *   **transferFailReason**: the reason why the call failed to be transferred to the agent.
        # *   **callId**: the unique receipt ID of the call, in the `taskId^bizId` format.
        # *   **recallCurTimes**: the number of recalls.
        # *   **callStartTime**: the start time of the call.
        # *   **callEndTime**: the end time of the call.
        # *   **sureCount**: the number of times that the robocall task was affirmed.
        # *   **denyCount**: the number of times that the robocall task was denied.
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # *   **customCount**: the number of times that the robocall task was customized.
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # *   **defaultCount**: the default number of calls.
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # *   **recordStatus**: Indicates whether the call has a recording file. Valid values: **1**: The call has a recording file. **2**: The call does not have a recording file.
        # *   **recordFile**: the download URL of the recording file.
        # *   **dialogDetail**: the dialog details, in a JSON-formatted array. **role**: the object of the speech. **content**: the content of the speech. **speakTime**: the time of the speech.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

