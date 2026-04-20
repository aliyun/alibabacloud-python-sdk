# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamDiscoveredResourceResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_discovered_resources: List[main_models.ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries on each page.
        self.count = count
        # The list of resources.
        self.ipam_discovered_resources = ipam_discovered_resources
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
        if self.ipam_discovered_resources:
            for v1 in self.ipam_discovered_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamDiscoveredResources'] = []
        if self.ipam_discovered_resources is not None:
            for k1 in self.ipam_discovered_resources:
                result['IpamDiscoveredResources'].append(k1.to_map() if k1 else None)

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

        self.ipam_discovered_resources = []
        if m.get('IpamDiscoveredResources') is not None:
            for k1 in m.get('IpamDiscoveredResources'):
                temp_model = main_models.ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources()
                self.ipam_discovered_resources.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResources(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        cidr: str = None,
        discovery_time: str = None,
        ip_count_detail: main_models.ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail = None,
        ip_usage: str = None,
        ipam_resource_discovery_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The CIDR block of the resource.
        self.cidr = cidr
        # The time when the resource was discovered.
        # 
        # >  If the resource has not been modified since it was created, the discovery time remains unchanged.
        self.discovery_time = discovery_time
        self.ip_count_detail = ip_count_detail
        # The IP usage in decimal form.
        self.ip_usage = ip_usage
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The ID of the region to which the resource belongs.
        self.resource_region_id = resource_region_id
        # The resource type. Valid values:
        # 
        # *   **VPC**
        # *   **VSwitch**
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The ID of the VPC to which the resource belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ip_count_detail:
            self.ip_count_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.discovery_time is not None:
            result['DiscoveryTime'] = self.discovery_time

        if self.ip_count_detail is not None:
            result['IpCountDetail'] = self.ip_count_detail.to_map()

        if self.ip_usage is not None:
            result['IpUsage'] = self.ip_usage

        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('DiscoveryTime') is not None:
            self.discovery_time = m.get('DiscoveryTime')

        if m.get('IpCountDetail') is not None:
            temp_model = main_models.ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail()
            self.ip_count_detail = temp_model.from_map(m.get('IpCountDetail'))

        if m.get('IpUsage') is not None:
            self.ip_usage = m.get('IpUsage')

        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListIpamDiscoveredResourceResponseBodyIpamDiscoveredResourcesIpCountDetail(DaraModel):
    def __init__(
        self,
        free_ip_count: str = None,
        total_ip_count: str = None,
        used_ip_count: str = None,
    ):
        self.free_ip_count = free_ip_count
        self.total_ip_count = total_ip_count
        self.used_ip_count = used_ip_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count

        if self.total_ip_count is not None:
            result['TotalIpCount'] = self.total_ip_count

        if self.used_ip_count is not None:
            result['UsedIpCount'] = self.used_ip_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')

        if m.get('TotalIpCount') is not None:
            self.total_ip_count = m.get('TotalIpCount')

        if m.get('UsedIpCount') is not None:
            self.used_ip_count = m.get('UsedIpCount')

        return self

