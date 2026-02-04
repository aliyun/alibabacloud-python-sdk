# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
    ):
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query and no next queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the resource is deployed.
        # 
        # You can ignore this parameter if ResourceType is set to Cen or BandwidthPackage.
        self.region_id = region_id
        # The IDs of the CEN instances.
        # 
        # You can specify at most 20 IDs in each call.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource to which you want to add the tag. Valid values:
        # 
        # **Cen**: CEN instance
        # 
        # **BandwidthPackage**: bandwidth plan
        # 
        # **TransitRouter**: transit router
        # 
        # **TransitRouterVpcAttachment**: virtual private cloud (VPC) connection
        # 
        # **TransitRouterVbrAttachment**: virtual border router (VBR) connection
        # 
        # **TransitRouterPeerAttachment**: inter-region connection
        # 
        # **TransitRouterVpnAttachment**: VPN connection
        # 
        # **TransitRouterRouteTable**: route table
        # 
        # **Flowlog**: flow log
        # 
        # **TransitRouterMulticastDomain**: multicast domain
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The information about the tags that are added to the CEN instance.
        # 
        # You can query at most 20 tags in each call.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot exceed 64 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value cannot exceed 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag values.
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

