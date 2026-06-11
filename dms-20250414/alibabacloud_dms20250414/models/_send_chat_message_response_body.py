# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class SendChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SendChatMessageResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response data.
        self.data = data
        # The error code. A value of `Success` indicates that the request was successful.
        self.error_code = error_code
        # The error message. This field is empty if the request is successful.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SendChatMessageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SendChatMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        message: str = None,
        session_id: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # Describes the result of the request.
        self.message = message
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.message is not None:
            result['Message'] = self.message

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

