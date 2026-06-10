# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRenewalPriceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_type: str = None,
    ):
        # The instance ID. The value for this parameter depends on the resource type:
        # 
        # - If `ResourceType` is set to `Desktop`, set `InstanceId` to the cloud desktop ID.
        # 
        # - If `ResourceType` is set to `DesktopGroup`, set `InstanceId` to the desktop pool ID.
        # 
        # - If `ResourceType` is set to `Bandwidth`, set `InstanceId` to the premium bandwidth ID.
        self.instance_id = instance_id
        # The instance IDs. The values to provide depend on the resource type (`ResourceType`).
        self.instance_ids = instance_ids
        # The renewal duration. The valid values depend on the `PeriodUnit` parameter.
        # 
        # - If `PeriodUnit` is set to `Month`, the valid values are 1, 2, 3, and 6.
        # 
        # - If `PeriodUnit` is set to `Year`, the valid values are 1, 2, and 3.
        # 
        # Default value: 1.
        self.period = period
        # The time unit for the `Period` parameter.
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to get a list of regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

