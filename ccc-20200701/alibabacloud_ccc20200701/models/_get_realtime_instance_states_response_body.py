# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeInstanceStatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRealtimeInstanceStatesResponseBodyData = None,
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
            temp_model = main_models.GetRealtimeInstanceStatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRealtimeInstanceStatesResponseBodyData(DaraModel):
    def __init__(
        self,
        break_code_detail_list: List[main_models.GetRealtimeInstanceStatesResponseBodyDataBreakCodeDetailList] = None,
        breaking_agents: int = None,
        instance_id: str = None,
        interactive_calls: int = None,
        logged_in_agents: int = None,
        longest_waiting_time: int = None,
        ready_agents: int = None,
        talking_agents: int = None,
        total_agents: int = None,
        waiting_calls: int = None,
        working_agents: int = None,
    ):
        self.break_code_detail_list = break_code_detail_list
        self.breaking_agents = breaking_agents
        self.instance_id = instance_id
        self.interactive_calls = interactive_calls
        self.logged_in_agents = logged_in_agents
        self.longest_waiting_time = longest_waiting_time
        self.ready_agents = ready_agents
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

        if self.interactive_calls is not None:
            result['InteractiveCalls'] = self.interactive_calls

        if self.logged_in_agents is not None:
            result['LoggedInAgents'] = self.logged_in_agents

        if self.longest_waiting_time is not None:
            result['LongestWaitingTime'] = self.longest_waiting_time

        if self.ready_agents is not None:
            result['ReadyAgents'] = self.ready_agents

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
                temp_model = main_models.GetRealtimeInstanceStatesResponseBodyDataBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k1))

        if m.get('BreakingAgents') is not None:
            self.breaking_agents = m.get('BreakingAgents')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InteractiveCalls') is not None:
            self.interactive_calls = m.get('InteractiveCalls')

        if m.get('LoggedInAgents') is not None:
            self.logged_in_agents = m.get('LoggedInAgents')

        if m.get('LongestWaitingTime') is not None:
            self.longest_waiting_time = m.get('LongestWaitingTime')

        if m.get('ReadyAgents') is not None:
            self.ready_agents = m.get('ReadyAgents')

        if m.get('TalkingAgents') is not None:
            self.talking_agents = m.get('TalkingAgents')

        if m.get('TotalAgents') is not None:
            self.total_agents = m.get('TotalAgents')

        if m.get('WaitingCalls') is not None:
            self.waiting_calls = m.get('WaitingCalls')

        if m.get('WorkingAgents') is not None:
            self.working_agents = m.get('WorkingAgents')

        return self

class GetRealtimeInstanceStatesResponseBodyDataBreakCodeDetailList(DaraModel):
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

