# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListCampaignTrendingReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCampaignTrendingReportResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCampaignTrendingReportResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCampaignTrendingReportResponseBodyData(DaraModel):
    def __init__(
        self,
        break_agents: int = None,
        concurrency: int = None,
        datetime: int = None,
        logged_in_agents: int = None,
        outbound_scenario_breaking_agents: str = None,
        outbound_scenario_ready_agents: str = None,
        outbound_scenario_talking_agents: str = None,
        outbound_scenario_working_agents: str = None,
        ready_agents: int = None,
        talk_agents: int = None,
        work_agents: int = None,
    ):
        self.break_agents = break_agents
        self.concurrency = concurrency
        self.datetime = datetime
        self.logged_in_agents = logged_in_agents
        self.outbound_scenario_breaking_agents = outbound_scenario_breaking_agents
        self.outbound_scenario_ready_agents = outbound_scenario_ready_agents
        self.outbound_scenario_talking_agents = outbound_scenario_talking_agents
        self.outbound_scenario_working_agents = outbound_scenario_working_agents
        self.ready_agents = ready_agents
        self.talk_agents = talk_agents
        self.work_agents = work_agents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.break_agents is not None:
            result['BreakAgents'] = self.break_agents

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.datetime is not None:
            result['Datetime'] = self.datetime

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

        if self.talk_agents is not None:
            result['TalkAgents'] = self.talk_agents

        if self.work_agents is not None:
            result['WorkAgents'] = self.work_agents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakAgents') is not None:
            self.break_agents = m.get('BreakAgents')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')

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

        if m.get('TalkAgents') is not None:
            self.talk_agents = m.get('TalkAgents')

        if m.get('WorkAgents') is not None:
            self.work_agents = m.get('WorkAgents')

        return self

