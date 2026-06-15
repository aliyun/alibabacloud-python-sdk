# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRenewalPriceRequest(DaraModel):
    def __init__(
        self,
        expected_renew_day: int = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        price_unit: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        # The unified expiration day. If you specify this parameter, the system queries the price for renewing the instance until the unified expiration day. Valid values: 1 to 28.
        # 
        # For more information about the unified expiration day feature, see [Unify Instance Expiration Dates](https://help.aliyun.com/document_detail/108486.html).
        # 
        # > You cannot specify both the renewal duration parameters (`Period` and `PeriodUnit`) and the unified expiration day parameter (`ExpectedRenewDay`) at the same time.
        self.expected_renew_day = expected_renew_day
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies the renewal duration. Valid values:
        # 
        # - When the `PriceUnit` parameter is set to `Month`: 1 to 9.
        # 
        # - When the `PriceUnit` parameter is set to `Year`: 1 to 3.
        # 
        # Default Value: 1.
        # 
        # > You cannot specify both the renewal duration parameters (`Period` and `PeriodUnit`) and the unified expiration day parameter (`ExpectedRenewDay`) at the same time.
        self.period = period
        # Specifies the renewal period. Valid values:
        # 
        # - Month: The renewal period is one month.
        # 
        # - Year: The renewal period is one year.
        # 
        # Default Value: Month.
        self.price_unit = price_unit
        # The Region ID of the instance. You can invoke [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud Regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID for which to query the renewal price. When the parameter `ResourceType` is set to `instance`, `ResourceId` can be interpreted as `InstanceId`.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type for which to query the renewal price. Valid value: instance.
        # 
        # Default Value: instance.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expected_renew_day is not None:
            result['ExpectedRenewDay'] = self.expected_renew_day

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedRenewDay') is not None:
            self.expected_renew_day = m.get('ExpectedRenewDay')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

