# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SendRuntimeQrCodeConfigChannelMessageRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        code: str = None,
        runtime_ids: List[str] = None,
        runtime_type: str = None,
    ):
        # The agent platform type.
        # 
        # This parameter is required.
        self.agent_platform = agent_platform
        # The agent provider.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The third-party channel code, such as dingtalk-connector (DingTalk), feishu (Lark), or wecom (WeCom). If the current agent platform and provider do not support the channel, the error code ChannelConfig.NotSupported is returned, and no messages are sent.
        # 
        # This parameter is required.
        self.code = code
        # The IDs of the runtime resources, such as cloud desktop IDs. You can specify 1 to 200 IDs.
        # 
        # This parameter is required.
        self.runtime_ids = runtime_ids
        # The runtime environment type of the runtime resource. Currently, only CloudDesktop is supported.
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

        if self.runtime_ids is not None:
            result['RuntimeIds'] = self.runtime_ids

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

        if m.get('RuntimeIds') is not None:
            self.runtime_ids = m.get('RuntimeIds')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

