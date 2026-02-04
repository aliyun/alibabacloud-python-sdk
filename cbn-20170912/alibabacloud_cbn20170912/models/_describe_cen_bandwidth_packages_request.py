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
        # The filter configurations.
        self.filter = filter
        # Specifies whether to include renewal data. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.include_reservation_data = include_reservation_data
        # The logical operator between the filter conditions. Valid values:
        # 
        # *   **false** (default): **AND** Bandwidth plans that meet all filter conditions are returned.
        # *   **true**: **OR** Bandwidth plans that meet one of the filter conditions are returned.
        self.is_or_key = is_or_key
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
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
        # The tag keys.
        # 
        # The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag values.
        # 
        # The tag values can be 0 to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # The tag value of each tag key must be unique. You can specify at most 20 tag values in each call.
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
        # The filter conditions. You can use filter conditions to filter the bandwidth plans that you want to query. The following filter conditions are supported:
        # 
        # *   **CenId**: CEN instance ID
        # 
        # *   **Status**: bandwidth plan status. Valid values:
        # 
        #     *   **Idle**: not associated with a CEN instance.
        #     *   **InUse**: associated with a CEN instance.
        # 
        # *   **CenBandwidthPackageId**: bandwidth plan ID
        # 
        # *   **Name**: bandwidth plan name You can specify one or more filter conditions. The maximum value of **N** is **5**.
        self.key = key
        # Specify a filter value based on the **Key** parameter. You can specify multiple filter values for each **Key**. The logical operator between filter values is **OR**. If one filter value is matched, the filter condition is matched.
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

