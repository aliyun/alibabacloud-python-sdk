# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotTaskCallListResponseBody(DaraModel):
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
        # The information about the robocall task, which is a JSON-formatted array.
        # 
        # *   **taskId**: the unique ID of the robocall task.
        # *   **caller**: the calling number.
        # *   **called**: the called number.
        # *   **duration**: the call duration. Unit: seconds.
        # *   **label**: the label of the called party.
        # *   **dialogCount**: the number of conversation rounds in the call.
        # *   **callResult**: the call result.
        # *   **hangupDirection**: the party who hung up. Valid values: **1** and **0**. The value 1 indicates the called party, and the value 0 indicates the robot.
        # *   **transferResult**: the result of transferring the call to an agent. Valid values: **1**, **0**, and **3**. The value 1 indicates that the call was transferred to an agent. The value 0 indicates that the call failed to be transferred to an agent. The value 3 indicates that the call was not transferred to an agent.
        # *   **transferNumber**: the phone number of the agent to whom the call was transferred.
        # *   **transferFailReason**: the reason why the call failed to be transferred to an agent.
        # *   **callId**: the unique receipt ID of the call.
        # *   **recallCurTimes**: the number of recalls.
        # *   **callStartTime**: the start time of the call.
        # *   **callEndTime**: the end time of the call.
        # *   **sureCount**: the number of times that the robocall task was acknowledged.
        # *   **denyCount**: the number of times that the robocall task was denied.
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # *   **customCount**: the number of times that the robocall task was customized.
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # *   **defaultCount**: the default number of calls.
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # *   ****
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

