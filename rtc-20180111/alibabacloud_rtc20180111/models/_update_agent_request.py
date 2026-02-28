# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        task_id: str = None,
        voice_chat_config: main_models.UpdateAgentRequestVoiceChatConfig = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.task_id = task_id
        self.voice_chat_config = voice_chat_config

    def validate(self):
        if self.voice_chat_config:
            self.voice_chat_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.voice_chat_config is not None:
            result['VoiceChatConfig'] = self.voice_chat_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VoiceChatConfig') is not None:
            temp_model = main_models.UpdateAgentRequestVoiceChatConfig()
            self.voice_chat_config = temp_model.from_map(m.get('VoiceChatConfig'))

        return self

class UpdateAgentRequestVoiceChatConfig(DaraModel):
    def __init__(
        self,
        chat_mode: int = None,
        interrupt_mode: int = None,
    ):
        self.chat_mode = chat_mode
        self.interrupt_mode = interrupt_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_mode is not None:
            result['ChatMode'] = self.chat_mode

        if self.interrupt_mode is not None:
            result['InterruptMode'] = self.interrupt_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatMode') is not None:
            self.chat_mode = m.get('ChatMode')

        if m.get('InterruptMode') is not None:
            self.interrupt_mode = m.get('InterruptMode')

        return self

