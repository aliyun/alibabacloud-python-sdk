# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancesByExpireTimeRequest(DaraModel):
    def __init__(
        self,
        expire_period: int = None,
        expired: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
        proxy_id: str = None,
    ):
        # The number of remaining days for which the instances are available. Valid values: **0 to 180**.
        self.expire_period = expire_period
        # Specifies whether to query instances that have expired. Valid values:
        # 
        # *   **True**: queries instances that have expired.
        # *   **False**: does not query instances that have expired.
        self.expired = expired
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Valid values: any **non-zero** positive integer.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1 to 100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to obtain the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag that is added to the instance. Each tag is a key-value pair that consists of two parts: TagKey and TagValue. You can specify a maximum of five tags in the following format for each request: `{"key1":"value1","key2":"value2"...}`.
        self.tags = tags
        # A deprecated parameter. You do not need to configure this parameter.
        self.proxy_id = proxy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_period is not None:
            result['ExpirePeriod'] = self.expire_period

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.proxy_id is not None:
            result['proxyId'] = self.proxy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirePeriod') is not None:
            self.expire_period = m.get('ExpirePeriod')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('proxyId') is not None:
            self.proxy_id = m.get('proxyId')

        return self

