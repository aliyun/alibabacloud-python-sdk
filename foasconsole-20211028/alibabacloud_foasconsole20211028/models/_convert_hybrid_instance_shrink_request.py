# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertHybridInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        # The order instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region.
        # 
        # This parameter is required.
        self.region = region
        # The maximum resource specifications available for the pay-as-you-go portion of hybrid billing.
        # 
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')

        return self

