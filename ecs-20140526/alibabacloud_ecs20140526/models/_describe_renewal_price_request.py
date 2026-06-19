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
        # The unified expiration date. After you specify this parameter, the price for renewing the instance to the unified expiration date is returned. Valid values: 1 to 28.
        # 
        # For more information about the unified expiration date feature, see [Settings for instance expires](https://help.aliyun.com/document_detail/108486.html).
        # 
        # > The renewal duration parameters (`Period` and `PeriodUnit`) and the unified expiration date parameter (`ExpectedRenewDay`) cannot be set at the same time.
        self.expected_renew_day = expected_renew_day
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal duration. Valid values:
        # 
        # - When `PriceUnit` is set to `Month`: 1 to 9.
        # - When `PriceUnit` is set to `Year`: 1 to 3.
        # 
        # Default value: 1.
        # 
        # > The renewal duration parameters (`Period` and `PeriodUnit`) and the unified expiration date parameter (`ExpectedRenewDay`) cannot be set at the same time.
        self.period = period
        # The unit of the renewal duration. Valid values:
        # 
        # - Month: the renewal duration is measured in months.
        # - Year: the renewal duration is measured in years.
        # 
        # Default value: Month.
        self.price_unit = price_unit
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource whose renewal price you want to query. When `ResourceType` is set to `instance`, `ResourceId` is equivalent to `InstanceId`.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource whose renewal price you want to query. Valid values: instance.
        # 
        # Default value: instance.
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

