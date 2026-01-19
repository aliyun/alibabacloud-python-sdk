# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeCampaignStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRealtimeCampaignStatsResponseBodyData = None,
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
            temp_model = main_models.GetRealtimeCampaignStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRealtimeCampaignStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        breaking_agents: int = None,
        caps: int = None,
        logged_in_agents: int = None,
        outbound_scenario_breaking_agents: int = None,
        outbound_scenario_ready_agents: int = None,
        outbound_scenario_talking_agents: int = None,
        outbound_scenario_working_agents: int = None,
        ready_agents: int = None,
        talking_agents: int = None,
        total_agents: int = None,
        working_agents: int = None,
    ):
        self.breaking_agents = breaking_agents
        self.caps = caps
        self.logged_in_agents = logged_in_agents
        self.outbound_scenario_breaking_agents = outbound_scenario_breaking_agents
        self.outbound_scenario_ready_agents = outbound_scenario_ready_agents
        self.outbound_scenario_talking_agents = outbound_scenario_talking_agents
        self.outbound_scenario_working_agents = outbound_scenario_working_agents
        self.ready_agents = ready_agents
        self.talking_agents = talking_agents
        self.total_agents = total_agents
        self.working_agents = working_agents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.breaking_agents is not None:
            result['BreakingAgents'] = self.breaking_agents

        if self.caps is not None:
            result['Caps'] = self.caps

        if self.logged_in_agents is not None:
            result['LoggedInAgents'] = self.logged_in_agents

        if self.outbound_scenario_breaking_agents is not None:
            result['OutboundScenarioBreakingAgents'] = self.outbound_scenario_breaking_agents

        if self.outbound_scenario_ready_agents is not None:
            result['OutboundScenarioReadyAgents'] = self.outbound_scenario_ready_agents

        if self.outbound_scenario_talking_agents is not None:
            result['OutboundScenarioTalkingAgents'] = self.outbound_scenario_talking_agents

        if self.outbound_scenario_working_agents is not None:
            result['OutboundScenarioWorkingAgents'] = self.outbound_scenario_working_agents

        if self.ready_agents is not None:
            result['ReadyAgents'] = self.ready_agents

        if self.talking_agents is not None:
            result['TalkingAgents'] = self.talking_agents

        if self.total_agents is not None:
            result['TotalAgents'] = self.total_agents

        if self.working_agents is not None:
            result['WorkingAgents'] = self.working_agents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakingAgents') is not None:
            self.breaking_agents = m.get('BreakingAgents')

        if m.get('Caps') is not None:
            self.caps = m.get('Caps')

        if m.get('LoggedInAgents') is not None:
            self.logged_in_agents = m.get('LoggedInAgents')

        if m.get('OutboundScenarioBreakingAgents') is not None:
            self.outbound_scenario_breaking_agents = m.get('OutboundScenarioBreakingAgents')

        if m.get('OutboundScenarioReadyAgents') is not None:
            self.outbound_scenario_ready_agents = m.get('OutboundScenarioReadyAgents')

        if m.get('OutboundScenarioTalkingAgents') is not None:
            self.outbound_scenario_talking_agents = m.get('OutboundScenarioTalkingAgents')

        if m.get('OutboundScenarioWorkingAgents') is not None:
            self.outbound_scenario_working_agents = m.get('OutboundScenarioWorkingAgents')

        if m.get('ReadyAgents') is not None:
            self.ready_agents = m.get('ReadyAgents')

        if m.get('TalkingAgents') is not None:
            self.talking_agents = m.get('TalkingAgents')

        if m.get('TotalAgents') is not None:
            self.total_agents = m.get('TotalAgents')

        if m.get('WorkingAgents') is not None:
            self.working_agents = m.get('WorkingAgents')

        return self

