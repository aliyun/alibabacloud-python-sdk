# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRatePlanSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        instance_id: str = None,
        order_type: str = None,
        target_plan_code: str = None,
        target_plan_name: str = None,
    ):
        # Specifies whether to enable auto payment.
        self.auto_pay = auto_pay
        self.charge_type = charge_type
        self.instance_id = instance_id
        # The specification update type. Valid values:
        # 
        # *   DOWNGRADE
        # *   UPGRADE
        self.order_type = order_type
        self.target_plan_code = target_plan_code
        self.target_plan_name = target_plan_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

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
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('TargetPlanCode') is not None:
            self.target_plan_code = m.get('TargetPlanCode')

        if m.get('TargetPlanName') is not None:
            self.target_plan_name = m.get('TargetPlanName')

        return self

