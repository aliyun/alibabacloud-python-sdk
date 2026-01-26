# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentDownloadUrlV2Request(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        arch_type: str = None,
        os_type: str = None,
    ):
        # The agent type.\\
        # **Valid values:**
        # 
        # *   **JavaAgent**
        # *   **Instgo**
        # 
        # This parameter is required.
        self.agent_type = agent_type
        # The architecture type of the environment where the agent is installed.\\
        # This parameter is required and valid only when **AgentType** is set to **Instgo**.\\
        # **Valid values:**
        # 
        # *   **amd64**
        # *   **arm64**
        self.arch_type = arch_type
        # The operating system of the environment where the agent is installed.\\
        # This parameter is required and valid only when **AgentType** is set to **Instgo**.\\
        # **Valid values:**
        # 
        # *   **linux**
        # *   **darwin**
        # *   **windows**
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.arch_type is not None:
            result['ArchType'] = self.arch_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('ArchType') is not None:
            self.arch_type = m.get('ArchType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        return self

