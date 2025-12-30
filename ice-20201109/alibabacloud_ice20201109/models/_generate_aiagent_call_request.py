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
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        self.agent_config = agent_config
        self.chat_sync_config = chat_sync_config
        # The time when the token expires. Unit: seconds. Default value: 3600. Valid values: 0 to 604800.
        self.expire = expire
        self.session_id = session_id
        # The template configurations of the AI agent. The specified configurations are merged with the template configurations that are specified in the console. If you do not specify this parameter, the system uses the default configurations for an AI agent created in the console.
        self.template_config = template_config
        self.user_data = user_data
        # The username of the AI agent in the channel. If you do not specify this parameter, the system automatically generates a username. The value can be up to 64 characters in length.
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
        self.imaiagent_id = imaiagent_id
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

