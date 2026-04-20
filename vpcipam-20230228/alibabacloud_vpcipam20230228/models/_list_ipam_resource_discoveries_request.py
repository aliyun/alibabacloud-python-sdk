# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamResourceDiscoveriesRequest(DaraModel):
    def __init__(
        self,
        ipam_resource_discovery_ids: List[str] = None,
        ipam_resource_discovery_name: str = None,
        is_shared: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.ListIpamResourceDiscoveriesRequestTags] = None,
        type: str = None,
    ):
        # The IDs of resource discovery instances. Valid values of N: 1 to 100. A maximum of 100 resource discoveries can be queried at a time.
        self.ipam_resource_discovery_ids = ipam_resource_discovery_ids
        # The name of the resource discovery.
        # 
        # The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        # Whether it is a shared resource discovery.
        self.is_shared = is_shared
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where you want to query resource discovery. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group that resource discovery belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag.
        self.tags = tags
        # The type of resource discovery.
        # 
        # > Supported types:
        # > - system: default resource discovery created by the system.
        # > - custom: custom resource discovery created by users.
        self.type = type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_resource_discovery_ids is not None:
            result['IpamResourceDiscoveryIds'] = self.ipam_resource_discovery_ids

        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name

        if self.is_shared is not None:
            result['IsShared'] = self.is_shared

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryIds') is not None:
            self.ipam_resource_discovery_ids = m.get('IpamResourceDiscoveryIds')

        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')

        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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
                temp_model = main_models.ListIpamResourceDiscoveriesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListIpamResourceDiscoveriesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The tag key must start with a letter but cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify at most 20 tag values. The tag value cannot be an empty string.
        # 
        # A tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

