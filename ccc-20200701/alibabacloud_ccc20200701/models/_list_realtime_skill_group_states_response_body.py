# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListRealtimeSkillGroupStatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListRealtimeSkillGroupStatesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListRealtimeSkillGroupStatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRealtimeSkillGroupStatesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListRealtimeSkillGroupStatesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListRealtimeSkillGroupStatesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRealtimeSkillGroupStatesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        break_code_detail_list: List[main_models.ListRealtimeSkillGroupStatesResponseBodyDataListBreakCodeDetailList] = None,
        breaking_agents: int = None,
        instance_id: str = None,
        logged_in_agents: int = None,
        longest_waiting_time: int = None,
        outbound_scenario_ready_agents: int = None,
        ready_agents: int = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
        talking_agents: int = None,
        total_agents: int = None,
        waiting_calls: int = None,
        working_agents: int = None,
    ):
        self.break_code_detail_list = break_code_detail_list
        self.breaking_agents = breaking_agents
        self.instance_id = instance_id
        self.logged_in_agents = logged_in_agents
        self.longest_waiting_time = longest_waiting_time
        self.outbound_scenario_ready_agents = outbound_scenario_ready_agents
        self.ready_agents = ready_agents
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.talking_agents = talking_agents
        self.total_agents = total_agents
        self.waiting_calls = waiting_calls
        self.working_agents = working_agents

    def validate(self):
        if self.break_code_detail_list:
            for v1 in self.break_code_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BreakCodeDetailList'] = []
        if self.break_code_detail_list is not None:
            for k1 in self.break_code_detail_list:
                result['BreakCodeDetailList'].append(k1.to_map() if k1 else None)

        if self.breaking_agents is not None:
            result['BreakingAgents'] = self.breaking_agents

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logged_in_agents is not None:
            result['LoggedInAgents'] = self.logged_in_agents

        if self.longest_waiting_time is not None:
            result['LongestWaitingTime'] = self.longest_waiting_time

        if self.outbound_scenario_ready_agents is not None:
            result['OutboundScenarioReadyAgents'] = self.outbound_scenario_ready_agents

        if self.ready_agents is not None:
            result['ReadyAgents'] = self.ready_agents

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        if self.talking_agents is not None:
            result['TalkingAgents'] = self.talking_agents

        if self.total_agents is not None:
            result['TotalAgents'] = self.total_agents

        if self.waiting_calls is not None:
            result['WaitingCalls'] = self.waiting_calls

        if self.working_agents is not None:
            result['WorkingAgents'] = self.working_agents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.break_code_detail_list = []
        if m.get('BreakCodeDetailList') is not None:
            for k1 in m.get('BreakCodeDetailList'):
                temp_model = main_models.ListRealtimeSkillGroupStatesResponseBodyDataListBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k1))

        if m.get('BreakingAgents') is not None:
            self.breaking_agents = m.get('BreakingAgents')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoggedInAgents') is not None:
            self.logged_in_agents = m.get('LoggedInAgents')

        if m.get('LongestWaitingTime') is not None:
            self.longest_waiting_time = m.get('LongestWaitingTime')

        if m.get('OutboundScenarioReadyAgents') is not None:
            self.outbound_scenario_ready_agents = m.get('OutboundScenarioReadyAgents')

        if m.get('ReadyAgents') is not None:
            self.ready_agents = m.get('ReadyAgents')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        if m.get('TalkingAgents') is not None:
            self.talking_agents = m.get('TalkingAgents')

        if m.get('TotalAgents') is not None:
            self.total_agents = m.get('TotalAgents')

        if m.get('WaitingCalls') is not None:
            self.waiting_calls = m.get('WaitingCalls')

        if m.get('WorkingAgents') is not None:
            self.working_agents = m.get('WorkingAgents')

        return self

class ListRealtimeSkillGroupStatesResponseBodyDataListBreakCodeDetailList(DaraModel):
    def __init__(
        self,
        break_code: str = None,
        count: int = None,
    ):
        self.break_code = break_code
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.break_code is not None:
            result['BreakCode'] = self.break_code

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

