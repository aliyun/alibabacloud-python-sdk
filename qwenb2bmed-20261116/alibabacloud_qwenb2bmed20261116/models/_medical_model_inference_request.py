# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bmed20261116 import models as main_models
from darabonba.model import DaraModel

class MedicalModelInferenceRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.MedicalModelInferenceRequestCommunication = None,
        data: main_models.MedicalModelInferenceRequestData = None,
        params: main_models.MedicalModelInferenceRequestParams = None,
    ):
        # The association ID, session, and application identity information for the current request.
        # 
        # This parameter is required.
        self.communication = communication
        # The business data that carries the messages for the current request.
        # 
        # This parameter is required.
        self.data = data
        # The extensible JSON object. The modelName parameter is required and its value must be an activated model selector. The directAgent parameter cannot be passed.
        # 
        # This parameter is required.
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
            temp_model = main_models.MedicalModelInferenceRequestCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.MedicalModelInferenceRequestData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('params') is not None:
            temp_model = main_models.MedicalModelInferenceRequestParams()
            self.params = temp_model.from_map(m.get('params'))

        return self

class MedicalModelInferenceRequestParams(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        response_streaming: bool = None,
    ):
        # Required. The model selector for this medical API is med_qwen4-vl-125.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The response mode. A value of false indicates that a complete JSON object is returned. A value of true indicates that Server-Sent Events (SSE) is returned.
        self.response_streaming = response_streaming

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.response_streaming is not None:
            result['responseStreaming'] = self.response_streaming

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('responseStreaming') is not None:
            self.response_streaming = m.get('responseStreaming')

        return self

class MedicalModelInferenceRequestData(DaraModel):
    def __init__(
        self,
        messages: List[main_models.MedicalModelInferenceRequestDataMessages] = None,
    ):
        # The list of messages arranged in conversation order. When hosted by the client, this list can include the session history provided by the client.
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
                temp_model = main_models.MedicalModelInferenceRequestDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class MedicalModelInferenceRequestDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        role: str = None,
    ):
        # The string or array of multimodal content blocks.
        # 
        # This parameter is required.
        self.content = content
        # The sender of the message. A value of user indicates the business user, and a value of assistant indicates the assistant.
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

class MedicalModelInferenceRequestCommunication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_scene: str = None,
        history_owner: str = None,
        request_id: str = None,
        session_id: str = None,
        user_info: main_models.MedicalModelInferenceRequestCommunicationUserInfo = None,
    ):
        # The business application ID. This parameter is required when no fixed application is configured.
        self.app_id = app_id
        # The optional business scenario tag.
        self.app_scene = app_scene
        # The host of the session history. This value must be the same as the value specified in the first call of the session.
        # 
        # This parameter is required.
        self.history_owner = history_owner
        # The customer business request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The customer session ID, which is reused for continued conversations.
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
            temp_model = main_models.MedicalModelInferenceRequestCommunicationUserInfo()
            self.user_info = temp_model.from_map(m.get('userInfo'))

        return self

class MedicalModelInferenceRequestCommunicationUserInfo(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        user_id: str = None,
        user_ip: str = None,
        user_name: str = None,
    ):
        # The terminal device identifier provided by the customer.
        self.device_id = device_id
        # The business user identifier in the customer application. This value is provided based on the user binding or delegation configuration of the business gateway credentials.
        self.user_id = user_id
        # The business user IP address provided by the customer.
        self.user_ip = user_ip
        # The business user name provided by the customer.
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

