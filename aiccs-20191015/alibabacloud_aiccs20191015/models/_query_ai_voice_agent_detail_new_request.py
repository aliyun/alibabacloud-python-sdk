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
        # The ID of the agent.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The ID of the branch. If you do not specify this parameter, the active branch is used.
        self.branch_id = branch_id
        # The ID of the version. If you do not specify this parameter, the system uses the latest published version for the specified branch. You must specify BranchId when you use this parameter.
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

