# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListAgentStatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAgentStatesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAgentStatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAgentStatesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAgentStatesResponseBodyDataList] = None,
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
                temp_model = main_models.ListAgentStatesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgentStatesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        break_code: str = None,
        dn: str = None,
        instance_id: str = None,
        login_name: str = None,
        outbound_scenario: bool = None,
        state: str = None,
        state_duration: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.break_code = break_code
        self.dn = dn
        self.instance_id = instance_id
        self.login_name = login_name
        self.outbound_scenario = outbound_scenario
        self.state = state
        self.state_duration = state_duration

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

        if self.dn is not None:
            result['Dn'] = self.dn

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.state is not None:
            result['State'] = self.state

        if self.state_duration is not None:
            result['StateDuration'] = self.state_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')

        if m.get('Dn') is not None:
            self.dn = m.get('Dn')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StateDuration') is not None:
            self.state_duration = m.get('StateDuration')

        return self

