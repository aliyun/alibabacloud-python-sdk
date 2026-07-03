# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataStorageRequest(DaraModel):
    def __init__(
        self,
        data_storage_region_id: str = None,
        delivery_status: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The log storage region.
        # 
        # This parameter is required.
        self.data_storage_region_id = data_storage_region_id
        # The global switch for log delivery in Log Management. This parameter is not yet available. Valid values:
        # 
        # - enable: Enables global delivery.
        # 
        # - disable: Disables global delivery.
        self.delivery_status = delivery_status
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The region where the Data Management center for threat analysis is located. This region must be the same as the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: The assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: The assets are in a region outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can specify this parameter to switch to the perspective of the member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_storage_region_id is not None:
            result['DataStorageRegionId'] = self.data_storage_region_id

        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataStorageRegionId') is not None:
            self.data_storage_region_id = m.get('DataStorageRegionId')

        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

