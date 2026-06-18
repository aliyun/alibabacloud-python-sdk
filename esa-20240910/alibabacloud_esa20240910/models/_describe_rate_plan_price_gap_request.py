# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRatePlanPriceGapRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order_type: str = None,
        target_plan_code: str = None,
        target_plan_name: str = None,
    ):
        # The target plan name. You can obtain this value from the [DescribeRatePlanPrice](~~DescribeRatePlanPrice~~) operation.
        self.instance_id = instance_id
        # The specification change type. Valid values:
        # - DOWNGRADE: downgrade.
        # - UPGRADE: upgrade.
        self.order_type = order_type
        # The specification change type. Valid values:
        # - DOWNGRADE: downgrade.
        # - UPGRADE: upgrade.
        self.target_plan_code = target_plan_code
        # The name of the target plan for the specification change.
        self.target_plan_name = target_plan_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.target_plan_code is not None:
            result['TargetPlanCode'] = self.target_plan_code

        if self.target_plan_name is not None:
            result['TargetPlanName'] = self.target_plan_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('TargetPlanCode') is not None:
            self.target_plan_code = m.get('TargetPlanCode')

        if m.get('TargetPlanName') is not None:
            self.target_plan_name = m.get('TargetPlanName')

        return self

