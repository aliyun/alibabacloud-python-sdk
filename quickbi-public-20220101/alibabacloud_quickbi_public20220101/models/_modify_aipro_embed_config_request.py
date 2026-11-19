# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAiproEmbedConfigRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        ai_pro_id: str = None,
        chat_history_status: int = None,
        config: str = None,
        memory_enabled: int = None,
        show_name: str = None,
        upload_enabled: int = None,
    ):
        # The nickname of the agent. The default value is Intelligent Data Analytics Assistant when you create a configuration.
        self.agent_name = agent_name
        # The AIPro configuration ID. If this parameter is not specified or is left empty, a new configuration is created. If this parameter is specified, the existing configuration is updated.
        self.ai_pro_id = ai_pro_id
        # Specifies whether to display the chat history. Valid values:
        # 
        # - 1: Display.
        # - 0: Do not display.
        # 
        # Default value: 1.
        self.chat_history_status = chat_history_status
        # The JSON string of the embedding appearance configuration saved on the frontend.
        self.config = config
        # Specifies whether to enable memory. Valid values:
        # 
        # - 1: Enable.
        # - 0: Disable.
        # 
        # Default value: 0.
        self.memory_enabled = memory_enabled
        # The name of the configuration. This parameter is required and must be unique within the organization when you create a configuration. If this parameter is left empty when you update a configuration, the name is not updated.
        self.show_name = show_name
        # Specifies whether to allow file uploads. Valid values:
        # 
        # - 1: Allow.
        # - 0: Do not allow.
        # 
        # Default value: 0.
        self.upload_enabled = upload_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.ai_pro_id is not None:
            result['AiProId'] = self.ai_pro_id

        if self.chat_history_status is not None:
            result['ChatHistoryStatus'] = self.chat_history_status

        if self.config is not None:
            result['Config'] = self.config

        if self.memory_enabled is not None:
            result['MemoryEnabled'] = self.memory_enabled

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.upload_enabled is not None:
            result['UploadEnabled'] = self.upload_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AiProId') is not None:
            self.ai_pro_id = m.get('AiProId')

        if m.get('ChatHistoryStatus') is not None:
            self.chat_history_status = m.get('ChatHistoryStatus')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('MemoryEnabled') is not None:
            self.memory_enabled = m.get('MemoryEnabled')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('UploadEnabled') is not None:
            self.upload_enabled = m.get('UploadEnabled')

        return self

