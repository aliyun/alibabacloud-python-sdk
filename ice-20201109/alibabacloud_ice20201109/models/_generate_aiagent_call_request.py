# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GenerateAIAgentCallRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        agent_config: main_models.AIAgentConfig = None,
        chat_sync_config: main_models.GenerateAIAgentCallRequestChatSyncConfig = None,
        expire: int = None,
        session_id: str = None,
        template_config: main_models.AIAgentTemplateConfig = None,
        user_data: str = None,
        user_id: str = None,
    ):
        # The AI agent ID.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # The agent template configuration. The configuration you provide merges with the agent template configuration in the console. If you omit this parameter, the agent uses the default configuration from the console.
        # 
        # > Compatibility with `TemplateConfig`: Fields in `AgentConfig` take precedence. If a field is specified in `TemplateConfig` but not in `AgentConfig`, the system uses the value from `TemplateConfig`. We recommend using `AgentConfig` instead of `TemplateConfig`.
        self.agent_config = agent_config
        # The chat synchronization configuration.
        self.chat_sync_config = chat_sync_config
        # Optional. The expiration time of the token in seconds. Default value: 3600. Value range: 0 to 604800.
        self.expire = expire
        # A unique identifier for the session. If not provided, a new session is created.
        self.session_id = session_id
        # - This configuration merges with the agent template configuration in the console.
        # 
        # - If you omit this parameter, the agent uses the default configuration from the console.
        # 
        # > The agent template configuration. This parameter is deprecated. Use the AgentConfig parameter instead.
        self.template_config = template_config
        # User data.
        self.user_data = user_data
        # The username in the channel. If you do not specify a username, one is automatically generated. The username can be up to 64 characters in length.
        self.user_id = user_id

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.chat_sync_config:
            self.chat_sync_config.validate()
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.agent_config is not None:
            result['AgentConfig'] = self.agent_config.to_map()

        if self.chat_sync_config is not None:
            result['ChatSyncConfig'] = self.chat_sync_config.to_map()

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AgentConfig') is not None:
            temp_model = main_models.AIAgentConfig()
            self.agent_config = temp_model.from_map(m.get('AgentConfig'))

        if m.get('ChatSyncConfig') is not None:
            temp_model = main_models.GenerateAIAgentCallRequestChatSyncConfig()
            self.chat_sync_config = temp_model.from_map(m.get('ChatSyncConfig'))

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.AIAgentTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GenerateAIAgentCallRequestChatSyncConfig(DaraModel):
    def __init__(
        self,
        imaiagent_id: str = None,
        receiver_id: str = None,
    ):
        # The ID of the Instant Messaging (IM) agent.
        self.imaiagent_id = imaiagent_id
        # The user ID of the recipient.
        self.receiver_id = receiver_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.imaiagent_id is not None:
            result['IMAIAgentId'] = self.imaiagent_id

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IMAIAgentId') is not None:
            self.imaiagent_id = m.get('IMAIAgentId')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        return self

