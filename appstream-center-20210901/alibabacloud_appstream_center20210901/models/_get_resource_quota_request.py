# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceQuotaRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        product_type: str = None,
        resource_type: str = None,
    ):
        # The business region ID. If this parameter is omitted, the general quota that is not limited by region is queried. The quotas of different regions are not added together. This parameter must be consistent with the business region in What to do next.
        self.biz_region_id = biz_region_id
        # The billing method query condition. If this parameter is omitted, the general quota that is not limited by billing method is queried. The quotas of different billing methods are not added together. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        self.charge_type = charge_type
        # The product type. Set this parameter to the following value when you call the operation:
        # 
        # - `CloudApp`: WUYING Cloud App.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The business resource type to query. Valid values:
        # 
        # - `AppInstanceGroup`: the quantity quota for delivery groups. Unit: groups.
        # - `AppAuthUser`: the quantity quota for authorized users. Unit: users.
        # - `PoolNodeAmount`: the quantity quota for purchased resource nodes. Unit: nodes.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

