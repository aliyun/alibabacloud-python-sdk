# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentRuntimeRequest(DaraModel):
    def __init__(
        self,
        agent_runtime_version: str = None,
    ):
        # 指定要获取的智能体运行时版本，如果不指定则返回最新版本
        self.agent_runtime_version = agent_runtime_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_version is not None:
            result['agentRuntimeVersion'] = self.agent_runtime_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeVersion') is not None:
            self.agent_runtime_version = m.get('agentRuntimeVersion')

        return self

