# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AIUsageLimitPolicy(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        limit_policy_id: str = None,
        limit_value: int = None,
        metric_type: str = None,
        name: str = None,
        priority: int = None,
        reset_period: str = None,
        service_ids: List[str] = None,
        status: str = None,
        user_group_ids: List[str] = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.limit_policy_id = limit_policy_id
        self.limit_value = limit_value
        self.metric_type = metric_type
        self.name = name
        self.priority = priority
        self.reset_period = reset_period
        self.service_ids = service_ids
        self.status = status
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.limit_policy_id is not None:
            result['LimitPolicyId'] = self.limit_policy_id

        if self.limit_value is not None:
            result['LimitValue'] = self.limit_value

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reset_period is not None:
            result['ResetPeriod'] = self.reset_period

        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LimitPolicyId') is not None:
            self.limit_policy_id = m.get('LimitPolicyId')

        if m.get('LimitValue') is not None:
            self.limit_value = m.get('LimitValue')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResetPeriod') is not None:
            self.reset_period = m.get('ResetPeriod')

        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

