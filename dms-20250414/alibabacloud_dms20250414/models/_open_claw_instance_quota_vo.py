# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenClawInstanceQuotaVO(DaraModel):
    def __init__(
        self,
        aliyun_account_uid: str = None,
        deep_research_call_quota: str = None,
        deep_research_call_used: str = None,
        instance_gmt_create: str = None,
        instance_id: str = None,
        instance_name: str = None,
        last_metering_time: str = None,
        model_call_quota: str = None,
        model_call_used: str = None,
        refresh_day: str = None,
        skill_plan_call_quota: str = None,
        skill_plan_call_used: str = None,
    ):
        self.aliyun_account_uid = aliyun_account_uid
        self.deep_research_call_quota = deep_research_call_quota
        self.deep_research_call_used = deep_research_call_used
        self.instance_gmt_create = instance_gmt_create
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.last_metering_time = last_metering_time
        self.model_call_quota = model_call_quota
        self.model_call_used = model_call_used
        self.refresh_day = refresh_day
        self.skill_plan_call_quota = skill_plan_call_quota
        self.skill_plan_call_used = skill_plan_call_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_account_uid is not None:
            result['AliyunAccountUid'] = self.aliyun_account_uid

        if self.deep_research_call_quota is not None:
            result['DeepResearchCallQuota'] = self.deep_research_call_quota

        if self.deep_research_call_used is not None:
            result['DeepResearchCallUsed'] = self.deep_research_call_used

        if self.instance_gmt_create is not None:
            result['InstanceGmtCreate'] = self.instance_gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.last_metering_time is not None:
            result['LastMeteringTime'] = self.last_metering_time

        if self.model_call_quota is not None:
            result['ModelCallQuota'] = self.model_call_quota

        if self.model_call_used is not None:
            result['ModelCallUsed'] = self.model_call_used

        if self.refresh_day is not None:
            result['RefreshDay'] = self.refresh_day

        if self.skill_plan_call_quota is not None:
            result['SkillPlanCallQuota'] = self.skill_plan_call_quota

        if self.skill_plan_call_used is not None:
            result['SkillPlanCallUsed'] = self.skill_plan_call_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAccountUid') is not None:
            self.aliyun_account_uid = m.get('AliyunAccountUid')

        if m.get('DeepResearchCallQuota') is not None:
            self.deep_research_call_quota = m.get('DeepResearchCallQuota')

        if m.get('DeepResearchCallUsed') is not None:
            self.deep_research_call_used = m.get('DeepResearchCallUsed')

        if m.get('InstanceGmtCreate') is not None:
            self.instance_gmt_create = m.get('InstanceGmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('LastMeteringTime') is not None:
            self.last_metering_time = m.get('LastMeteringTime')

        if m.get('ModelCallQuota') is not None:
            self.model_call_quota = m.get('ModelCallQuota')

        if m.get('ModelCallUsed') is not None:
            self.model_call_used = m.get('ModelCallUsed')

        if m.get('RefreshDay') is not None:
            self.refresh_day = m.get('RefreshDay')

        if m.get('SkillPlanCallQuota') is not None:
            self.skill_plan_call_quota = m.get('SkillPlanCallQuota')

        if m.get('SkillPlanCallUsed') is not None:
            self.skill_plan_call_used = m.get('SkillPlanCallUsed')

        return self

