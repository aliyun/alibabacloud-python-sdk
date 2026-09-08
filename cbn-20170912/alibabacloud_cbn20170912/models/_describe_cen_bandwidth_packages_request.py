# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenBandwidthPackagesRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeCenBandwidthPackagesRequestFilter] = None,
        include_reservation_data: bool = None,
        is_or_key: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeCenBandwidthPackagesRequestTag] = None,
    ):
        # The filter information.
        self.filter = filter
        # Specifies whether to include renewal data. Valid values:
        # 
        # - **true**: Includes renewal data.
        # 
        # - **false**: Does not include renewal data.
        self.include_reservation_data = include_reservation_data
        # The logical relationship between filter conditions. Valid values:
        # 
        # - **false** (default): The filter conditions have an **AND** relationship. A bandwidth package must match all filter conditions to be returned.
        # 
        # - **true**: The filter conditions have an **OR** relationship. A bandwidth package that matches any filter condition is returned.
        self.is_or_key = is_or_key
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the list. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for a paged query. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information list.
        # 
        # You can specify up to 20 tags at a time.
        self.tag = tag

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data

        if self.is_or_key is not None:
            result['IsOrKey'] = self.is_or_key

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeCenBandwidthPackagesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')

        if m.get('IsOrKey') is not None:
            self.is_or_key = m.get('IsOrKey')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeCenBandwidthPackagesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCenBandwidthPackagesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # Once specified, the tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value of the resource.
        # 
        # The tag value can be empty or a string of up to 128 characters. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values at a time.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeCenBandwidthPackagesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition.
        # You can use filter conditions to filter the bandwidth package instances to query. The following filter conditions are supported:
        # 
        # - **CenId**: The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # - **Status**: The status of the bandwidth package instance. Valid values:
        # 
        #     - **Idle**: Not associated.
        #     - **InUse**: Associated.
        # 
        # - **CenBandwidthPackageId**: The ID of the bandwidth package.
        # 
        # - **Name**: The name of the bandwidth package.
        # You can specify one or more filter conditions. The maximum value of **N** is **5**.
        self.key = key
        # The filter values based on the specified **Key**. You can specify multiple filter values for a single **Key**. The filter values have an **OR** relationship, which means that a bandwidth package matching any of the filter values is considered a match for the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

