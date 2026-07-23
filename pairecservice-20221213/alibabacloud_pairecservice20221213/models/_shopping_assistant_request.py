# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ShoppingAssistantRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        contents: main_models.ShoppingAssistantRequestContents = None,
        conversation_id: str = None,
        environment: str = None,
        input_message: main_models.ShoppingAssistantRequestInputMessage = None,
        instance_id: str = None,
        language: str = None,
        scene_id: str = None,
        service_id: str = None,
        session_id: str = None,
        uid: str = None,
    ):
        # The additional configuration.
        self.config = config
        # The contents.
        self.contents = contents
        # The conversation ID. This parameter is not yet effective.
        self.conversation_id = conversation_id
        # **The environment.**
        self.environment = environment
        # The input message.
        self.input_message = input_message
        # **The instance ID.**
        self.instance_id = instance_id
        # The language.
        self.language = language
        # **The scene ID.**
        self.scene_id = scene_id
        # **The service ID.**
        self.service_id = service_id
        # The session ID.
        self.session_id = session_id
        # user id。
        self.uid = uid

    def validate(self):
        if self.contents:
            self.contents.validate()
        if self.input_message:
            self.input_message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.contents is not None:
            result['Contents'] = self.contents.to_map()

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.input_message is not None:
            result['InputMessage'] = self.input_message.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Contents') is not None:
            temp_model = main_models.ShoppingAssistantRequestContents()
            self.contents = temp_model.from_map(m.get('Contents'))

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InputMessage') is not None:
            temp_model = main_models.ShoppingAssistantRequestInputMessage()
            self.input_message = temp_model.from_map(m.get('InputMessage'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class ShoppingAssistantRequestInputMessage(DaraModel):
    def __init__(
        self,
        content: List[main_models.ShoppingAssistantRequestInputMessageContent] = None,
    ):
        # The message content.
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ShoppingAssistantRequestInputMessageContent()
                self.content.append(temp_model.from_map(k1))

        return self

class ShoppingAssistantRequestInputMessageContent(DaraModel):
    def __init__(
        self,
        text: str = None,
        type: str = None,
    ):
        # The message content.
        self.text = text
        # The message type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ShoppingAssistantRequestContents(DaraModel):
    def __init__(
        self,
        text: str = None,
        type: str = None,
    ):
        # The message content.
        self.text = text
        # The message type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

