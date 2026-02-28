# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRealtimeAgentStatesRequest(DaraModel):
    def __init__(
        self,
        agent_id_list: str = None,
        agent_name: str = None,
        call_type_list: str = None,
        instance_id: str = None,
        media_type: str = None,
        outbound_scenario: bool = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        skill_group_id: str = None,
        state_list: str = None,
        work_mode_list: str = None,
    ):
        self.agent_id_list = agent_id_list
        self.agent_name = agent_name
        self.call_type_list = call_type_list
        # This parameter is required.
        self.instance_id = instance_id
        self.media_type = media_type
        self.outbound_scenario = outbound_scenario
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.query = query
        self.skill_group_id = skill_group_id
        self.state_list = state_list
        self.work_mode_list = work_mode_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id_list is not None:
            result['AgentIdList'] = self.agent_id_list

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.call_type_list is not None:
            result['CallTypeList'] = self.call_type_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.state_list is not None:
            result['StateList'] = self.state_list

        if self.work_mode_list is not None:
            result['WorkModeList'] = self.work_mode_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIdList') is not None:
            self.agent_id_list = m.get('AgentIdList')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('CallTypeList') is not None:
            self.call_type_list = m.get('CallTypeList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')

        if m.get('WorkModeList') is not None:
            self.work_mode_list = m.get('WorkModeList')

        return self

