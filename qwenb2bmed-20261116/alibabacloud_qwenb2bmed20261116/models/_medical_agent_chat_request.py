# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bmed20261116 import models as main_models
from darabonba.model import DaraModel

class MedicalAgentChatRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.MedicalAgentChatRequestCommunication = None,
        data: main_models.MedicalAgentChatRequestData = None,
        params: main_models.MedicalAgentChatRequestParams = None,
    ):
        # The correlation ID, session, and application identity information for this request.
        # 
        # This parameter is required.
        self.communication = communication
        # The business data that carries the message for this request.
        # 
        # This parameter is required.
        self.data = data
        # The optional extensible JSON object. The directAgent parameter can be omitted or set to med_qa. Other parameters are passed based on the parameters supported by the medical agent.
        self.params = params

    def validate(self):
        if self.communication:
            self.communication.validate()
        if self.data:
            self.data.validate()
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.params is not None:
            result['params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communication') is not None:
            temp_model = main_models.MedicalAgentChatRequestCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.MedicalAgentChatRequestData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('params') is not None:
            temp_model = main_models.MedicalAgentChatRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        return self

class MedicalAgentChatRequestParams(DaraModel):
    def __init__(
        self,
        deepthink: str = None,
        direct_agent: str = None,
        response_streaming: bool = None,
    ):
        # Specifies whether to enable deep thinking for the medical agent.
        self.deepthink = deepthink
        # This parameter can be omitted. If explicitly provided, the value must be med_qa.
        self.direct_agent = direct_agent
        # The response mode. A value of false returns a complete JSON response, and true returns Server-Sent Events (SSE).
        self.response_streaming = response_streaming

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deepthink is not None:
            result['deepthink'] = self.deepthink

        if self.direct_agent is not None:
            result['directAgent'] = self.direct_agent

        if self.response_streaming is not None:
            result['responseStreaming'] = self.response_streaming

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deepthink') is not None:
            self.deepthink = m.get('deepthink')

        if m.get('directAgent') is not None:
            self.direct_agent = m.get('directAgent')

        if m.get('responseStreaming') is not None:
            self.response_streaming = m.get('responseStreaming')

        return self

class MedicalAgentChatRequestData(DaraModel):
    def __init__(
        self,
        messages: List[main_models.MedicalAgentChatRequestDataMessages] = None,
    ):
        # The list of messages arranged in conversation order. When the history owner is CLIENT, this list can include the session history provided by the client.
        # 
        # This parameter is required.
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.MedicalAgentChatRequestDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class MedicalAgentChatRequestDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        role: str = None,
    ):
        # The string or array of multimodal content blocks.
        # 
        # This parameter is required.
        self.content = content
        # The sender of the message. A value of user indicates the business user, and assistant indicates the assistant.
        # 
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class MedicalAgentChatRequestCommunication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_scene: str = None,
        history_owner: str = None,
        request_id: str = None,
        session_id: str = None,
        user_info: main_models.MedicalAgentChatRequestCommunicationUserInfo = None,
    ):
        # The business application ID. This parameter is required if no fixed application is configured.
        self.app_id = app_id
        # The optional business scenario tag.
        self.app_scene = app_scene
        # The session history owner. This value must be the same as the one used in the first call of the session.
        # 
        # This parameter is required.
        self.history_owner = history_owner
        # The customer business request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The customer session ID. Reuse this ID to continue the conversation.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The business user and device information provided by the customer. Identity fields are passed based on the configuration of the business gateway credentials.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_scene is not None:
            result['appScene'] = self.app_scene

        if self.history_owner is not None:
            result['historyOwner'] = self.history_owner

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_info is not None:
            result['userInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appScene') is not None:
            self.app_scene = m.get('appScene')

        if m.get('historyOwner') is not None:
            self.history_owner = m.get('historyOwner')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userInfo') is not None:
            temp_model = main_models.MedicalAgentChatRequestCommunicationUserInfo()
            self.user_info = temp_model.from_map(m.get('userInfo'))

        return self



class MedicalAgentChatRequestCommunicationUserInfo(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        user_id: str = None,
        user_ip: str = None,
        user_name: str = None,
    ):
        # The terminal device identifier provided by the customer.
        self.device_id = device_id
        # The business user identifier in the customer application. This is provided based on the user binding or delegation configuration of the business gateway credentials.
        self.user_id = user_id
        # The IP address of the business user provided by the customer.
        self.user_ip = user_ip
        # The name of the business user provided by the customer.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_ip is not None:
            result['userIp'] = self.user_ip

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userIp') is not None:
            self.user_ip = m.get('userIp')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

