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
        # The expected resource scale of the execution plan. If ResourceType is set to VcpuCapacity, this field indicates that the execution plan expects to maintain 10,000 vCPUs.
        self.desired_capacity = desired_capacity
        # Specifies whether to enable the execution plan. Valid values:
        # 
        # - true: Enables the execution plan.
        # 
        # - false: Disables the execution plan.
        # >Notice: After the execution plan is disabled, already created Instant jobs are no longer automatically managed by the execution plan.
        self.enabled = enabled
        # The scheduling interval of the execution plan. Unit: minutes. Valid values: 10 to 10080. Default value: 60.
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

