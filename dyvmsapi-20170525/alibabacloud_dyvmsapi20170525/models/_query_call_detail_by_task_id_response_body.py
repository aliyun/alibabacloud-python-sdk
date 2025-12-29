# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCallDetailByTaskIdResponseBody(DaraModel):
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
        # The call details of the outbound robocall task, in the JSON format.
        # 
        # *   **startDate**: the time when the call was answered.
        # 
        # *   **stateDesc**: the reason why the call was hung up. If the status code of early media was returned, this parameter indicates the reason why the status code of early media was used.
        # 
        # *   **statusCode**: the status code.
        # 
        # *   **EndDate**: the time when the call was ended.
        # 
        # *   **calleeShowNumber**: the calling number displayed to the called party.
        # 
        # *   **callee**: the called number.
        # 
        # *   **duration**: the billing duration.
        # 
        # *   **gmtCreate**: the time when the outbound robocall task was created.
        # 
        # *   **hangupDirection**: the party who hung up.
        # 
        # *   **tags**: the call tags.
        # 
        # *   **dialogCount**: the number of conversation rounds in the call.
        # 
        # *   **sureCount**: the number of times that the robocall task was acknowledged.
        # 
        # *   **denyCount**: the number of times that the robocall task was denied.
        # 
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # 
        # *   **customCount**: the number of times that the robocall task was customized.
        # 
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # 
        # *   **recordFile**: the download URL of the recording file. The URL is valid only for 48 hours. The recording file must be downloaded in time.
        # 
        # *   **callId**: the call ID.
        # 
        # *   **recordStatus**: indicates whether a recording file was available. Valid values:
        # 
        #     *   1: A recording file was available.
        #     *   2: No recording file was available.
        # 
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # 
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # 
        # *   **callee**: the called number.
        # 
        # *   **dialogDetail**: the conversation details. The value is a JSON array that contains the following parameters:
        # 
        #     *   **role**: the role who spoke.
        #     *   **content**: the content of the speech.
        #     *   **time**: the start time of the speech.
        # 
        # > The preceding parameters are for reference only. The actually returned parameters prevail.
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

