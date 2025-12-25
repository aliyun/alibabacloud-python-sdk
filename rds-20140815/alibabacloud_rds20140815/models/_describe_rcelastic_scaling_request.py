# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCElasticScalingRequest(DaraModel):
    def __init__(
        self,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        support_case: str = None,
    ):
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id
        self.support_case = support_case

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_case is not None:
            result['SupportCase'] = self.support_case

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportCase') is not None:
            self.support_case = m.get('SupportCase')

        return self

