# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppAssistantAgentRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        biz_id: str = None,
        platform_type: str = None,
    ):
        self.agent_name = agent_name
        self.biz_id = biz_id
        self.platform_type = platform_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')

        return self

