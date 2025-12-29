# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyControlStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        control_strategy_list_shrink: str = None,
        product_type: str = None,
        region_id: str = None,
    ):
        # List of security alarm rules.
        self.control_strategy_list_shrink = control_strategy_list_shrink
        # Product type, currently only supports **ANT_CLOUD_AUTH** (Financial-grade Real Person), all others are phased out.
        self.product_type = product_type
        # Region ID of the intelligent access gateway instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_strategy_list_shrink is not None:
            result['ControlStrategyList'] = self.control_strategy_list_shrink

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlStrategyList') is not None:
            self.control_strategy_list_shrink = m.get('ControlStrategyList')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

