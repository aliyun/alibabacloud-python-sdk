# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListRealtimeAgentStatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListRealtimeAgentStatesResponseBodyData = None,
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
            temp_model = main_models.ListRealtimeAgentStatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRealtimeAgentStatesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListRealtimeAgentStatesResponseBodyDataList] = None,
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
                temp_model = main_models.ListRealtimeAgentStatesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRealtimeAgentStatesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        break_code: str = None,
        call_type: str = None,
        counter_party: str = None,
        duration: int = None,
        extension: str = None,
        instance_id: str = None,
        mobile: str = None,
        outbound_scenario: bool = None,
        skill_group_id_list: List[str] = None,
        skill_group_name_list: List[str] = None,
        state: str = None,
        state_code: str = None,
        state_time: int = None,
        work_mode: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.break_code = break_code
        self.call_type = call_type
        self.counter_party = counter_party
        self.duration = duration
        self.extension = extension
        self.instance_id = instance_id
        self.mobile = mobile
        self.outbound_scenario = outbound_scenario
        self.skill_group_id_list = skill_group_id_list
        self.skill_group_name_list = skill_group_name_list
        self.state = state
        self.state_code = state_code
        self.state_time = state_time
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.break_code is not None:
            result['BreakCode'] = self.break_code

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.counter_party is not None:
            result['CounterParty'] = self.counter_party

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list

        if self.skill_group_name_list is not None:
            result['SkillGroupNameList'] = self.skill_group_name_list

        if self.state is not None:
            result['State'] = self.state

        if self.state_code is not None:
            result['StateCode'] = self.state_code

        if self.state_time is not None:
            result['StateTime'] = self.state_time

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CounterParty') is not None:
            self.counter_party = m.get('CounterParty')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')

        if m.get('SkillGroupNameList') is not None:
            self.skill_group_name_list = m.get('SkillGroupNameList')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StateCode') is not None:
            self.state_code = m.get('StateCode')

        if m.get('StateTime') is not None:
            self.state_time = m.get('StateTime')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

