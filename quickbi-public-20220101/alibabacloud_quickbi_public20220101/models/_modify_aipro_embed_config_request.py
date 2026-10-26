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
        self.agent_name = agent_name
        self.ai_pro_id = ai_pro_id
        self.chat_history_status = chat_history_status
        self.config = config
        self.memory_enabled = memory_enabled
        self.show_name = show_name
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

