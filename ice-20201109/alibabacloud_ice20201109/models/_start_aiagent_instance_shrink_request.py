# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAIAgentInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        agent_config_shrink: str = None,
        chat_sync_config_shrink: str = None,
        runtime_config_shrink: str = None,
        session_id: str = None,
        template_config_shrink: str = None,
        user_data: str = None,
    ):
        # The ID of the AI agent created in the [IMS](https://ims.console.aliyun.com/ai/robot/list) console.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        self.agent_config_shrink = agent_config_shrink
        # 同步聊天记录配置。
        self.chat_sync_config_shrink = chat_sync_config_shrink
        # This parameter is required.
        self.runtime_config_shrink = runtime_config_shrink
        self.session_id = session_id
        self.template_config_shrink = template_config_shrink
        self.user_data = user_data

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

        if self.runtime_config_shrink is not None:
            result['RuntimeConfig'] = self.runtime_config_shrink

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.template_config_shrink is not None:
            result['TemplateConfig'] = self.template_config_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AgentConfig') is not None:
            self.agent_config_shrink = m.get('AgentConfig')

        if m.get('ChatSyncConfig') is not None:
            self.chat_sync_config_shrink = m.get('ChatSyncConfig')

        if m.get('RuntimeConfig') is not None:
            self.runtime_config_shrink = m.get('RuntimeConfig')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TemplateConfig') is not None:
            self.template_config_shrink = m.get('TemplateConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

