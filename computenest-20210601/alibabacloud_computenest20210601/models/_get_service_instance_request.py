# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceInstanceRequest(DaraModel):
    def __init__(
        self,
        market_instance_id: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The MarketInstance ID.
        self.market_instance_id = market_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # >  You must specify either `ServiceInstanceId` or `MarketInstanceId`. Otherwise, the operation fails.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

