# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRoutersRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        feature_filter: List[main_models.ListTransitRoutersRequestFeatureFilter] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[main_models.ListTransitRoutersRequestTag] = None,
        transit_router_id: str = None,
        transit_router_name: str = None,
        type: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The feature to be filtered.
        self.feature_filter = feature_filter
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1** to **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the transit router is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the transit router.
        # 
        # - **Creating**: The transit router is being created.
        # 
        # - **Active**: The transit router is available.
        # 
        # - **Modifying**: The transit router is being modified.
        # 
        # - **Deleting**: The transit router is being deleted.
        # 
        # - **Upgrading**: The transit router is being upgraded.
        self.status = status
        # The tags.
        # 
        # You can specify up to 20 tags.
        self.tag = tag
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The name of the transit router.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.transit_router_name = transit_router_name
        # The type of the transit router.
        # 
        # - **Enterprise**: Enterprise Edition.
        # 
        # - **Basic**: Basic Edition.
        self.type = type

    def validate(self):
        if self.feature_filter:
            for v1 in self.feature_filter:
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
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        result['FeatureFilter'] = []
        if self.feature_filter is not None:
            for k1 in self.feature_filter:
                result['FeatureFilter'].append(k1.to_map() if k1 else None)

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        self.feature_filter = []
        if m.get('FeatureFilter') is not None:
            for k1 in m.get('FeatureFilter'):
                temp_model = main_models.ListTransitRoutersRequestFeatureFilter()
                self.feature_filter.append(temp_model.from_map(k1))

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTransitRoutersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListTransitRoutersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be an empty string or a string of up to 128 characters. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each tag key must have a unique tag value. You can specify up to 20 tag values.
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

class ListTransitRoutersRequestFeatureFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The key of the feature to be filtered.
        # The following key is supported:
        # 
        # - **Multicast**: the multicast feature.
        self.key = key
        # A list of values for the feature.
        # If you set the key to **Multicast**, you can specify only one value. Valid values:
        # 
        # - **Enabled**: Multicast is supported.
        # 
        # - **Disabled**: Multicast is not supported.
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

