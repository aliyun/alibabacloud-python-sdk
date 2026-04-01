# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstanceTypesShrinkRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        engine: str = None,
        instance_type_shrink: str = None,
        instance_type_family: str = None,
        region_id: str = None,
    ):
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The database engine. Set the value to MySQL.
        self.engine = engine
        # The instance types.
        self.instance_type_shrink = instance_type_shrink
        # The instance family. You can call the **DescribeRCInstanceTypeFamilies** operation to query the instance families of instances.
        self.instance_type_family = instance_type_family
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_type_shrink is not None:
            result['InstanceType'] = self.instance_type_shrink

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceType') is not None:
            self.instance_type_shrink = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

