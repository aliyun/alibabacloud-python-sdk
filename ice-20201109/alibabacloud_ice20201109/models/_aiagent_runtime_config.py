# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AIAgentRuntimeConfig(DaraModel):
    def __init__(
        self,
        agent_user_id: str = None,
        auth_token: str = None,
        avatar_chat_3d: main_models.AIAgentRuntimeConfigAvatarChat3D = None,
        channel_id: str = None,
        vision_chat: main_models.AIAgentRuntimeConfigVisionChat = None,
        voice_chat: main_models.AIAgentRuntimeConfigVoiceChat = None,
    ):
        self.agent_user_id = agent_user_id
        self.auth_token = auth_token
        self.avatar_chat_3d = avatar_chat_3d
        self.channel_id = channel_id
        self.vision_chat = vision_chat
        self.voice_chat = voice_chat

    def validate(self):
        if self.avatar_chat_3d:
            self.avatar_chat_3d.validate()
        if self.vision_chat:
            self.vision_chat.validate()
        if self.voice_chat:
            self.voice_chat.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_user_id is not None:
            result['AgentUserId'] = self.agent_user_id

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.avatar_chat_3d is not None:
            result['AvatarChat3D'] = self.avatar_chat_3d.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.vision_chat is not None:
            result['VisionChat'] = self.vision_chat.to_map()

        if self.voice_chat is not None:
            result['VoiceChat'] = self.voice_chat.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUserId') is not None:
            self.agent_user_id = m.get('AgentUserId')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('AvatarChat3D') is not None:
            temp_model = main_models.AIAgentRuntimeConfigAvatarChat3D()
            self.avatar_chat_3d = temp_model.from_map(m.get('AvatarChat3D'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('VisionChat') is not None:
            temp_model = main_models.AIAgentRuntimeConfigVisionChat()
            self.vision_chat = temp_model.from_map(m.get('VisionChat'))

        if m.get('VoiceChat') is not None:
            temp_model = main_models.AIAgentRuntimeConfigVoiceChat()
            self.voice_chat = temp_model.from_map(m.get('VoiceChat'))

        return self

class AIAgentRuntimeConfigVoiceChat(DaraModel):
    def __init__(
        self,
        agent_user_id: str = None,
        auth_token: str = None,
        channel_id: str = None,
    ):
        self.agent_user_id = agent_user_id
        self.auth_token = auth_token
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_user_id is not None:
            result['AgentUserId'] = self.agent_user_id

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUserId') is not None:
            self.agent_user_id = m.get('AgentUserId')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        return self

class AIAgentRuntimeConfigVisionChat(DaraModel):
    def __init__(
        self,
        agent_user_id: str = None,
        auth_token: str = None,
        channel_id: str = None,
    ):
        self.agent_user_id = agent_user_id
        self.auth_token = auth_token
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_user_id is not None:
            result['AgentUserId'] = self.agent_user_id

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUserId') is not None:
            self.agent_user_id = m.get('AgentUserId')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        return self

class AIAgentRuntimeConfigAvatarChat3D(DaraModel):
    def __init__(
        self,
        agent_user_id: str = None,
        auth_token: str = None,
        channel_id: str = None,
    ):
        self.agent_user_id = agent_user_id
        self.auth_token = auth_token
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_user_id is not None:
            result['AgentUserId'] = self.agent_user_id

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUserId') is not None:
            self.agent_user_id = m.get('AgentUserId')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        return self

