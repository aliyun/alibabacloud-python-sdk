# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMultiZoneAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        region_id: str = None,
        zone_combination: str = None,
    ):
        # The billing method. Valid values:
        # - Prepaid: subscription.
        # - Postpaid: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zone combination. If this parameter is not specified, all zone combinations in the region are queried.
        self.zone_combination = zone_combination

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_combination is not None:
            result['ZoneCombination'] = self.zone_combination

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneCombination') is not None:
            self.zone_combination = m.get('ZoneCombination')

        return self

