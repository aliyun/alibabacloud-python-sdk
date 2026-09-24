# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAiVoiceAgentDetailNewRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        branch_id: str = None,
        version_id: str = None,
    ):
        # The agent ID.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The branch ID. If this parameter is left empty, the currently active branch is automatically used.
        self.branch_id = branch_id
        # The version ID. If this parameter is left empty, the latest published version of the corresponding branch is used. This parameter must be used together with BranchId.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

