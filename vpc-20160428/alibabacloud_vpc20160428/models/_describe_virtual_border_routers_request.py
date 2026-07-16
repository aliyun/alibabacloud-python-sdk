# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualBorderRoutersRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeVirtualBorderRoutersRequestFilter] = None,
        include_cross_account_vbr: bool = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.DescribeVirtualBorderRoutersRequestTags] = None,
    ):
        # The filter information.
        self.filter = filter
        # Specifies whether to include cross-account Virtual Border Routers.
        # 
        # - **true**: Included.
        # 
        # - **false** (default): Not included.
        self.include_cross_account_vbr = include_cross_account_vbr
        self.owner_id = owner_id
        # The page number of the list. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page in a paged query. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the VBR. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the resource.
        self.tags = tags

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
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

        if self.include_cross_account_vbr is not None:
            result['IncludeCrossAccountVbr'] = self.include_cross_account_vbr

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeVirtualBorderRoutersRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('IncludeCrossAccountVbr') is not None:
            self.include_cross_account_vbr = m.get('IncludeCrossAccountVbr')

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeVirtualBorderRoutersRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You must specify at least 1 tag key and can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

class DescribeVirtualBorderRoutersRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. You can specify up to 5 filter conditions. The following filter conditions are supported:
        # 
        # * **PhysicalConnectionId**: instance ID of the Express Connect circuit instance.
        # 
        # * **VbrId**: instance ID of the Virtual Border Router instance.
        # 
        # * **Status**: the status of the Virtual Border Router.
        # 
        # * **Name**: the name of the Virtual Border Router.
        # 
        # * **AccessPointId**: instance ID of the access point.
        # 
        # * **eccId**: instance ID of the Express Cloud Connect instance.
        # 
        # * **type**: the type of the Express Connect circuit.
        self.key = key
        # The filter value based on the specified Key. You can specify multiple filter values for a Key. The relationship between filter values is OR, which means that a match is found if any of the filter values is met.
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

