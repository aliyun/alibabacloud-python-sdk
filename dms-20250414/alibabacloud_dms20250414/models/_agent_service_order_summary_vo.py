# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentServiceOrderSummaryVO(DaraModel):
    def __init__(
        self,
        agent_service: str = None,
        deep_research_quota: int = None,
        model_call_quota: int = None,
        order_count: int = None,
        service_num_total: int = None,
        skill_plan_call_quota: int = None,
    ):
        self.agent_service = agent_service
        self.deep_research_quota = deep_research_quota
        self.model_call_quota = model_call_quota
        self.order_count = order_count
        self.service_num_total = service_num_total
        self.skill_plan_call_quota = skill_plan_call_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_service is not None:
            result['AgentService'] = self.agent_service

        if self.deep_research_quota is not None:
            result['DeepResearchQuota'] = self.deep_research_quota

        if self.model_call_quota is not None:
            result['ModelCallQuota'] = self.model_call_quota

        if self.order_count is not None:
            result['OrderCount'] = self.order_count

        if self.service_num_total is not None:
            result['ServiceNumTotal'] = self.service_num_total

        if self.skill_plan_call_quota is not None:
            result['SkillPlanCallQuota'] = self.skill_plan_call_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentService') is not None:
            self.agent_service = m.get('AgentService')

        if m.get('DeepResearchQuota') is not None:
            self.deep_research_quota = m.get('DeepResearchQuota')

        if m.get('ModelCallQuota') is not None:
            self.model_call_quota = m.get('ModelCallQuota')

        if m.get('OrderCount') is not None:
            self.order_count = m.get('OrderCount')

        if m.get('ServiceNumTotal') is not None:
            self.service_num_total = m.get('ServiceNumTotal')

        if m.get('SkillPlanCallQuota') is not None:
            self.skill_plan_call_quota = m.get('SkillPlanCallQuota')

        return self

