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
        # The synchronized expiration date. If you specify this parameter, the price for renewing a specified instance to the specified synchronized expiration date is queried. Valid values: 1 to 28.
        # 
        # For information about how to synchronize the expiration dates of instances, see [Synchronize the expiration dates of instances](https://help.aliyun.com/document_detail/108486.html).
        # 
        # > The renewal period-related parameter pair (`Period` and `PeriodUnit`) and the `ExpectedRenewDay` parameter are mutually exclusive.
        self.expected_renew_day = expected_renew_day
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal period. Valid values:
        # 
        # *   Valid values when the `PriceUnit` parameter is set to `Month`: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # *   Valid values when the `PriceUnit` parameter is set to `Year`: 1, 2, 3.
        # 
        # Default value: 1.
        # 
        # > The renewal period-related parameter pair (`Period` and `PeriodUnit`) and the `ExpectedRenewDay` parameter are mutually exclusive.
        self.period = period
        # The unit of the renewal period. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month.
        self.price_unit = price_unit
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource. If the `ResourceType` parameter is set to`  instance `, the value of the `ResourceId` parameter is the ID of the specified instance.``
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to instance.
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

