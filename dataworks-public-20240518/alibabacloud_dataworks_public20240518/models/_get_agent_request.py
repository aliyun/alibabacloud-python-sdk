# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentRequest(DaraModel):
    def __init__(
        self,
        agent_version: int = None,
        name: str = None,
    ):
        # If omitted, the current definition is retrieved. If a published version is specified, the corresponding snapshot and the fixed versions of official skills and suite artifacts are retrieved. If a current unpublished version is specified, the draft is returned without fixed artifact versions. This is not the POP system parameter Version.
        self.agent_version = agent_version
        # The name of the skill to read.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

