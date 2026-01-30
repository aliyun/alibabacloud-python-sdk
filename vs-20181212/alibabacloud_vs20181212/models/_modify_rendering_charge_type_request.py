# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRenderingChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        instance_billing_cycle: str = None,
        instance_charge_type: str = None,
        period: str = None,
        rendering_instance_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.instance_billing_cycle = instance_billing_cycle
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        self.period = period
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.period is not None:
            result['Period'] = self.period

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

