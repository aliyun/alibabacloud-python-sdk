# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class StartAIAgentInstanceRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        agent_config: main_models.AIAgentConfig = None,
        chat_sync_config: main_models.StartAIAgentInstanceRequestChatSyncConfig = None,
        runtime_config: main_models.AIAgentRuntimeConfig = None,
        session_id: str = None,
        template_config: main_models.AIAgentTemplateConfig = None,
        user_data: str = None,
    ):
        # The ID of the AI agent created in the [IMS](https://ims.console.aliyun.com/ai/robot/list) console.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        self.agent_config = agent_config
        # 同步聊天记录配置。
        self.chat_sync_config = chat_sync_config
        # This parameter is required.
        self.runtime_config = runtime_config
        self.session_id = session_id
        self.template_config = template_config
        self.user_data = user_data

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.chat_sync_config:
            self.chat_sync_config.validate()
        if self.runtime_config:
            self.runtime_config.validate()
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

        if self.runtime_config is not None:
            result['RuntimeConfig'] = self.runtime_config.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('AgentConfig') is not None:
            temp_model = main_models.AIAgentConfig()
            self.agent_config = temp_model.from_map(m.get('AgentConfig'))

        if m.get('ChatSyncConfig') is not None:
            temp_model = main_models.StartAIAgentInstanceRequestChatSyncConfig()
            self.chat_sync_config = temp_model.from_map(m.get('ChatSyncConfig'))

        if m.get('RuntimeConfig') is not None:
            temp_model = main_models.AIAgentRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('RuntimeConfig'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.AIAgentTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class StartAIAgentInstanceRequestChatSyncConfig(DaraModel):
    def __init__(
        self,
        imaiagent_id: str = None,
        receiver_id: str = None,
    ):
        # IM的智能体Id。
        self.imaiagent_id = imaiagent_id
        # 接收用户Id。
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

