# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamResourceCidrsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_cidrs: List[main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The list of resources in the IPAM pool.
        self.ipam_resource_cidrs = ipam_resource_cidrs
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_cidrs:
            for v1 in self.ipam_resource_cidrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamResourceCidrs'] = []
        if self.ipam_resource_cidrs is not None:
            for k1 in self.ipam_resource_cidrs:
                result['IpamResourceCidrs'].append(k1.to_map() if k1 else None)

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

        self.ipam_resource_cidrs = []
        if m.get('IpamResourceCidrs') is not None:
            for k1 in m.get('IpamResourceCidrs'):
                temp_model = main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrs()
                self.ipam_resource_cidrs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamResourceCidrsResponseBodyIpamResourceCidrs(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        cidr: str = None,
        compliance_status: str = None,
        ip_count_detail: main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail = None,
        ip_usage: str = None,
        ipam_allocation_id: str = None,
        ipam_id: str = None,
        ipam_pool_id: str = None,
        ipam_scope_id: str = None,
        management_status: str = None,
        overlap_detail: List[main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail] = None,
        overlap_status: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The CIDR block of the resource.
        self.cidr = cidr
        # The compliance status of the resource.
        # 
        # *   **Compliant**
        # *   **Noncompliant**
        # *   **Ignored** Ignored resources are not monitored.
        # *   **Unmanaged**: The resource does not have a CIDR block allocated from the IPAM pool. IPAM does not monitor whether the CIDR block of the resource meets the allocation rules of the IP address pool.
        self.compliance_status = compliance_status
        self.ip_count_detail = ip_count_detail
        # The IP usage that is displayed in decimal form.
        self.ip_usage = ip_usage
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_allocation_id = ipam_allocation_id
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The management status of the resource.
        # 
        # *   **Managed**: The resource has a CIDR block allocated from an IPAM pool. IPAM is monitoring whether the allocated CIDR block overlaps with other CIDR blocks and whether the allocated CIDR block meets the allocation rules.
        # *   **Unmanaged**: The resource does not have a CIDR block allocated from the IPAM pool. IPAM is monitoring whether the resource has CIDR blocks that meet the allocation rules. Monitor whether CIDR blocks overlap with each other.
        # *   **Ignored**: The resource is not monitored. Ignored resources are not monitored. If you ignore a resource, CIDR blocks allocated to the resource are returned to the IPAM pool and will not be automatically allocated to the resource (if automatic allocation rules are specified).
        self.management_status = management_status
        # List of resources that overlap with the current resource.
        self.overlap_detail = overlap_detail
        # The overlapping status of the resource.
        # 
        # *   **Nonoverlapping**
        # *   **Overlapping**
        # *   **Ignored** Ignored resources are not monitored.
        self.overlap_status = overlap_status
        # The resource ID.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The effective region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of resource. Valid values:
        # 
        # *   **VPC**
        # *   **VSwitch**
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The status of the resource in the IPAM pool. Valid values:
        # 
        # *   **Created**
        # *   **Deleted**
        self.status = status
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ip_count_detail:
            self.ip_count_detail.validate()
        if self.overlap_detail:
            for v1 in self.overlap_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.compliance_status is not None:
            result['ComplianceStatus'] = self.compliance_status

        if self.ip_count_detail is not None:
            result['IpCountDetail'] = self.ip_count_detail.to_map()

        if self.ip_usage is not None:
            result['IpUsage'] = self.ip_usage

        if self.ipam_allocation_id is not None:
            result['IpamAllocationId'] = self.ipam_allocation_id

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.management_status is not None:
            result['ManagementStatus'] = self.management_status

        result['OverlapDetail'] = []
        if self.overlap_detail is not None:
            for k1 in self.overlap_detail:
                result['OverlapDetail'].append(k1.to_map() if k1 else None)

        if self.overlap_status is not None:
            result['OverlapStatus'] = self.overlap_status

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

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('ComplianceStatus') is not None:
            self.compliance_status = m.get('ComplianceStatus')

        if m.get('IpCountDetail') is not None:
            temp_model = main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail()
            self.ip_count_detail = temp_model.from_map(m.get('IpCountDetail'))

        if m.get('IpUsage') is not None:
            self.ip_usage = m.get('IpUsage')

        if m.get('IpamAllocationId') is not None:
            self.ipam_allocation_id = m.get('IpamAllocationId')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('ManagementStatus') is not None:
            self.management_status = m.get('ManagementStatus')

        self.overlap_detail = []
        if m.get('OverlapDetail') is not None:
            for k1 in m.get('OverlapDetail'):
                temp_model = main_models.ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail()
                self.overlap_detail.append(temp_model.from_map(k1))

        if m.get('OverlapStatus') is not None:
            self.overlap_status = m.get('OverlapStatus')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListIpamResourceCidrsResponseBodyIpamResourceCidrsOverlapDetail(DaraModel):
    def __init__(
        self,
        overlap_resource_cidr: str = None,
        overlap_resource_id: str = None,
        overlap_resource_region: str = None,
    ):
        # The CIDR that overlaps with the current resource.
        self.overlap_resource_cidr = overlap_resource_cidr
        # Instance ID that overlaps with the current resource.
        self.overlap_resource_id = overlap_resource_id
        # The region of instance that overlaps with the current resource.
        self.overlap_resource_region = overlap_resource_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overlap_resource_cidr is not None:
            result['OverlapResourceCidr'] = self.overlap_resource_cidr

        if self.overlap_resource_id is not None:
            result['OverlapResourceId'] = self.overlap_resource_id

        if self.overlap_resource_region is not None:
            result['OverlapResourceRegion'] = self.overlap_resource_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverlapResourceCidr') is not None:
            self.overlap_resource_cidr = m.get('OverlapResourceCidr')

        if m.get('OverlapResourceId') is not None:
            self.overlap_resource_id = m.get('OverlapResourceId')

        if m.get('OverlapResourceRegion') is not None:
            self.overlap_resource_region = m.get('OverlapResourceRegion')

        return self

class ListIpamResourceCidrsResponseBodyIpamResourceCidrsIpCountDetail(DaraModel):
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

