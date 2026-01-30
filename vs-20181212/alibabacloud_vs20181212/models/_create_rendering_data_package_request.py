# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRenderingDataPackageRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        instance_billing_cycle: str = None,
        rendering_instance_id: str = None,
    ):
        self.category = category
        self.description = description
        self.instance_billing_cycle = instance_billing_cycle
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

