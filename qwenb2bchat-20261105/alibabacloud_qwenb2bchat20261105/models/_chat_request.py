# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bchat20261105 import models as main_models
from darabonba.model import DaraModel

class ChatRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.ChatRequestCommunication = None,
        data: main_models.ChatRequestData = None,
        params: main_models.ChatRequestParams = None,
    ):
        # The correlation ID, session, and application identity information for the current request.
        # 
        # This parameter is required.
        self.communication = communication
        # The business data that carries the messages for the current request.
        # 
        # This parameter is required.
        self.data = data
        # An optional extensible JSON object. responseStreaming is an optional boolean value. A value of false returns a complete JSON response, and a value of true returns a Server-Sent Events (SSE) response.
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
            temp_model = main_models.ChatRequestCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.ChatRequestData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('params') is not None:
            temp_model = main_models.ChatRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        return self

class ChatRequestParams(DaraModel):
    def __init__(
        self,
        deepthink: str = None,
        direct_agent: str = None,
        enable_text_image_mixed: bool = None,
        max_tokens: int = None,
        output_audio: bool = None,
        response_streaming: bool = None,
        temperature: float = None,
        top_p: float = None,
    ):
        # The deep thinking switch.
        self.deepthink = deepthink
        # The agent selector for the current turn.
        self.direct_agent = direct_agent
        # The mixed text and image output switch.
        self.enable_text_image_mixed = enable_text_image_mixed
        # The maximum number of output tokens for the model.
        self.max_tokens = max_tokens
        # The HTTP audio output switch.
        self.output_audio = output_audio
        # Specifies whether to use Server-Sent Events (SSE) for conversation responses.
        self.response_streaming = response_streaming
        # The model sampling temperature.
        self.temperature = temperature
        # The nucleus sampling probability for the model.
        self.top_p = top_p

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

        if self.enable_text_image_mixed is not None:
            result['enableTextImageMixed'] = self.enable_text_image_mixed

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.output_audio is not None:
            result['outputAudio'] = self.output_audio

        if self.response_streaming is not None:
            result['responseStreaming'] = self.response_streaming

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.top_p is not None:
            result['topP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deepthink') is not None:
            self.deepthink = m.get('deepthink')

        if m.get('directAgent') is not None:
            self.direct_agent = m.get('directAgent')

        if m.get('enableTextImageMixed') is not None:
            self.enable_text_image_mixed = m.get('enableTextImageMixed')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('outputAudio') is not None:
            self.output_audio = m.get('outputAudio')

        if m.get('responseStreaming') is not None:
            self.response_streaming = m.get('responseStreaming')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

class ChatRequestData(DaraModel):
    def __init__(
        self,
        messages: List[main_models.ChatRequestDataMessages] = None,
    ):
        # The list of messages arranged in conversational order. When history is managed by the client, it can include the session history provided by the client.
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
                temp_model = main_models.ChatRequestDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class ChatRequestDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        role: str = None,
    ):
        # The text or an array of supported multimodal content blocks.
        # 
        # This parameter is required.
        self.content = content
        # The sender of the message. user indicates the business user, and assistant indicates the assistant.
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

class ChatRequestCommunication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_scene: str = None,
        history_owner: str = None,
        request_id: str = None,
        session_id: str = None,
        user_info: main_models.ChatRequestCommunicationUserInfo = None,
    ):
        # The application ID provided based on the gateway credential identity configuration.
        self.app_id = app_id
        # The optional business scene marker.
        self.app_scene = app_scene
        # The owner of the session history, which must be consistent with the first call of the session.
        # 
        # This parameter is required.
        self.history_owner = history_owner
        # The business request ID of the customer.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The session ID of the customer, which is reused for continued chats.
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
            temp_model = main_models.ChatRequestCommunicationUserInfo()
            self.user_info = temp_model.from_map(m.get('userInfo'))

        return self



class ChatRequestCommunicationUserInfo(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        user_id: str = None,
        user_ip: str = None,
        user_name: str = None,
    ):
        # The terminal device identifier provided by the customer.
        self.device_id = device_id
        # The business user identifier within the customer application, provided based on the user binding or delegation configuration of the business gateway credentials.
        self.user_id = user_id
        # The IP address of the business user provided by the customer.
        self.user_ip = user_ip
        # The username of the business user provided by the customer.
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

