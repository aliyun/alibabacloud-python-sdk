# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRuntimeChannelQrCodeDetailRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        code: str = None,
        runtime_id: str = None,
        runtime_type: str = None,
    ):
        # The agent platform.
        # 
        # This parameter is required.
        self.agent_platform = agent_platform
        # The agent provider.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The channel code. It must be the same as the channel code used when initiating the QR code configuration channel, such as dingtalk-connector (DingTalk), feishu (Lark), or wecom (WeCom).
        # 
        # This parameter is required.
        self.code = code
        # The ID of the runtime, such as the ID of a cloud desktop.
        # 
        # This parameter is required.
        self.runtime_id = runtime_id
        # The runtime environment type of the runtime resource.
        # 
        # This parameter is required.
        self.runtime_type = runtime_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.code is not None:
            result['Code'] = self.code

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

