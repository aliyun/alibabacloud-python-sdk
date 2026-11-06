# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallPolarClawSkillsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        region_id: str = None,
        scope: str = None,
        uninstall_skill_names: str = None,
    ):
        # The task-level target agent (workspace). If not specified, the default agent is used.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query region details.
        self.region_id = region_id
        # The task-level scope. Valid values: workspace (default) and global. This parameter is mutually exclusive with AgentId.
        self.scope = scope
        # The names of the skills to uninstall.
        # 
        # This parameter is required.
        self.uninstall_skill_names = uninstall_skill_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.uninstall_skill_names is not None:
            result['UninstallSkillNames'] = self.uninstall_skill_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('UninstallSkillNames') is not None:
            self.uninstall_skill_names = m.get('UninstallSkillNames')

        return self

