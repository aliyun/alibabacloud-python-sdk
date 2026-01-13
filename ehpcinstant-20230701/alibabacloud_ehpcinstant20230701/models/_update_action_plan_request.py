# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateActionPlanRequest(DaraModel):
    def __init__(
        self,
        action_plan_id: str = None,
        desired_capacity: float = None,
        enabled: str = None,
        interval_minutes: int = None,
    ):
        # The ID of the execution plan.
        self.action_plan_id = action_plan_id
        # The expected scale of resources for the execution plan. If the ResourceType parameter is set to VcpuCapacity, the execution plan is expected to have 10000 vCPUs.
        self.desired_capacity = desired_capacity
        # Whether to enable the execution plan. Valid values:
        # 
        # *   true: enables the execution plan.
        # 
        # *   false: The execution plan is disabled.
        # 
        #     **
        # 
        #     **Note:** After an execution plan is disabled, the created Instant jobs are not automatically managed by the execution plan.
        self.enabled = enabled
        self.interval_minutes = interval_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_id is not None:
            result['ActionPlanId'] = self.action_plan_id

        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanId') is not None:
            self.action_plan_id = m.get('ActionPlanId')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        return self

