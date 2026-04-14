# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentServiceOrderVO(DaraModel):
    def __init__(
        self,
        agent_service: str = None,
        deep_research_quota: int = None,
        deep_research_used: int = None,
        expire_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        model_call_quota: int = None,
        model_call_used: int = None,
        order_instance_id: str = None,
        service_num: int = None,
        skill_plan_call_quota: int = None,
        skill_plan_call_used: int = None,
        status: str = None,
    ):
        self.agent_service = agent_service
        self.deep_research_quota = deep_research_quota
        self.deep_research_used = deep_research_used
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.model_call_quota = model_call_quota
        self.model_call_used = model_call_used
        self.order_instance_id = order_instance_id
        self.service_num = service_num
        self.skill_plan_call_quota = skill_plan_call_quota
        self.skill_plan_call_used = skill_plan_call_used
        self.status = status

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

        if self.deep_research_used is not None:
            result['DeepResearchUsed'] = self.deep_research_used

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.model_call_quota is not None:
            result['ModelCallQuota'] = self.model_call_quota

        if self.model_call_used is not None:
            result['ModelCallUsed'] = self.model_call_used

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.service_num is not None:
            result['ServiceNum'] = self.service_num

        if self.skill_plan_call_quota is not None:
            result['SkillPlanCallQuota'] = self.skill_plan_call_quota

        if self.skill_plan_call_used is not None:
            result['SkillPlanCallUsed'] = self.skill_plan_call_used

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentService') is not None:
            self.agent_service = m.get('AgentService')

        if m.get('DeepResearchQuota') is not None:
            self.deep_research_quota = m.get('DeepResearchQuota')

        if m.get('DeepResearchUsed') is not None:
            self.deep_research_used = m.get('DeepResearchUsed')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModelCallQuota') is not None:
            self.model_call_quota = m.get('ModelCallQuota')

        if m.get('ModelCallUsed') is not None:
            self.model_call_used = m.get('ModelCallUsed')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('ServiceNum') is not None:
            self.service_num = m.get('ServiceNum')

        if m.get('SkillPlanCallQuota') is not None:
            self.skill_plan_call_quota = m.get('SkillPlanCallQuota')

        if m.get('SkillPlanCallUsed') is not None:
            self.skill_plan_call_used = m.get('SkillPlanCallUsed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

