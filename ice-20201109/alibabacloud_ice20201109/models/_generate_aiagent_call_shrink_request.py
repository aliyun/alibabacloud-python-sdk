# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAIAgentCallShrinkRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        agent_config_shrink: str = None,
        chat_sync_config_shrink: str = None,
        expire: int = None,
        session_id: str = None,
        template_config_shrink: str = None,
        user_data: str = None,
        user_id: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        self.agent_config_shrink = agent_config_shrink
        self.chat_sync_config_shrink = chat_sync_config_shrink
        # The time when the token expires. Unit: seconds. Default value: 3600. Valid values: 0 to 604800.
        self.expire = expire
        self.session_id = session_id
        # The template configurations of the AI agent. The specified configurations are merged with the template configurations that are specified in the console. If you do not specify this parameter, the system uses the default configurations for an AI agent created in the console.
        self.template_config_shrink = template_config_shrink
        self.user_data = user_data
        # The username of the AI agent in the channel. If you do not specify this parameter, the system automatically generates a username. The value can be up to 64 characters in length.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.agent_config_shrink is not None:
            result['AgentConfig'] = self.agent_config_shrink

        if self.chat_sync_config_shrink is not None:
            result['ChatSyncConfig'] = self.chat_sync_config_shrink

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.template_config_shrink is not None:
            result['TemplateConfig'] = self.template_config_shrink

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
            self.agent_config_shrink = m.get('AgentConfig')

        if m.get('ChatSyncConfig') is not None:
            self.chat_sync_config_shrink = m.get('ChatSyncConfig')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TemplateConfig') is not None:
            self.template_config_shrink = m.get('TemplateConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

