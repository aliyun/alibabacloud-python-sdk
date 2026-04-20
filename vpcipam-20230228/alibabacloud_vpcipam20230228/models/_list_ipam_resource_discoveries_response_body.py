# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamResourceDiscoveriesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_discoveries: List[main_models.ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries on each page.
        self.count = count
        # The list of resource discovery instances.
        self.ipam_resource_discoveries = ipam_resource_discoveries
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_discoveries:
            for v1 in self.ipam_resource_discoveries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamResourceDiscoveries'] = []
        if self.ipam_resource_discoveries is not None:
            for k1 in self.ipam_resource_discoveries:
                result['IpamResourceDiscoveries'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ipam_resource_discoveries = []
        if m.get('IpamResourceDiscoveries') is not None:
            for k1 in m.get('IpamResourceDiscoveries'):
                temp_model = main_models.ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries()
                self.ipam_resource_discoveries.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveries(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ipam_resource_discovery_description: str = None,
        ipam_resource_discovery_id: str = None,
        ipam_resource_discovery_name: str = None,
        ipam_resource_discovery_status: str = None,
        operating_region_list: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: List[main_models.ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags] = None,
        type: str = None,
    ):
        # The time when the resource was discovered.
        self.create_time = create_time
        # The description of the resource discovery.
        self.ipam_resource_discovery_description = ipam_resource_discovery_description
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The name of the resource discovery.
        self.ipam_resource_discovery_name = ipam_resource_discovery_name
        # The status of the resource discovery instance. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        self.ipam_resource_discovery_status = ipam_resource_discovery_status
        # The list of resource discovery regions.
        self.operating_region_list = operating_region_list
        # The Alibaba Cloud account that owns the resource discovery.
        self.owner_id = owner_id
        # The region ID of the queried resource discovery instance.
        self.region_id = region_id
        # The ID of the resource group that resource discovery belongs.
        self.resource_group_id = resource_group_id
        # The sharing status of the resource.
        # 
        # *   If the value is empty, the resource is as an average instance.
        # *   If the value is Shared, the resource discovery comes from a shared source.
        # *   If the value is Sharing, the resource discovery is being shared.
        self.share_type = share_type
        # The tag list.
        self.tags = tags
        # The type of resource discovery.
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ipam_resource_discovery_description is not None:
            result['IpamResourceDiscoveryDescription'] = self.ipam_resource_discovery_description

        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.ipam_resource_discovery_name is not None:
            result['IpamResourceDiscoveryName'] = self.ipam_resource_discovery_name

        if self.ipam_resource_discovery_status is not None:
            result['IpamResourceDiscoveryStatus'] = self.ipam_resource_discovery_status

        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IpamResourceDiscoveryDescription') is not None:
            self.ipam_resource_discovery_description = m.get('IpamResourceDiscoveryDescription')

        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('IpamResourceDiscoveryName') is not None:
            self.ipam_resource_discovery_name = m.get('IpamResourceDiscoveryName')

        if m.get('IpamResourceDiscoveryStatus') is not None:
            self.ipam_resource_discovery_status = m.get('IpamResourceDiscoveryStatus')

        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListIpamResourceDiscoveriesResponseBodyIpamResourceDiscoveriesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

