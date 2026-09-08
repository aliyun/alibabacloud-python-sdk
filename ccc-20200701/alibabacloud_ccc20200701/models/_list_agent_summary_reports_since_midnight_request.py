# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentSummaryReportsSinceMidnightRequest(DaraModel):
    def __init__(
        self,
        agent_ids: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id: str = None,
    ):
        # Filter by a list of agent IDs, with up to 100 IDs.
        # 
        # > If the agent ID list is not empty, the system directly queries based on the provided agent ID list. In this case, the pageSize and pageNumber parameters are invalid, and the data is returned directly. For example, if the request parameter is pageNumber = 3, the response parameter will also be pageNumber = 3.
        self.agent_ids = agent_ids
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Page number, ranging from 1 to 100. Optional. Default value: 1.
        self.page_number = page_number
        # Page size, ranging from 1 to 100. Optional. Default value: 10.
        self.page_size = page_size
        # Filter by skill group ID.
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

