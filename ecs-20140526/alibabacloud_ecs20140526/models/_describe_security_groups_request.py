# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupsRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        fuzzy_query: bool = None,
        is_query_ecs_count: bool = None,
        max_results: int = None,
        network_type: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        security_group_ids: str = None,
        security_group_name: str = None,
        security_group_type: str = None,
        service_managed: bool = None,
        tag: List[main_models.DescribeSecurityGroupsRequestTag] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # - true: performs only a dry run. The system checks the request for potential issues, including AccessKey validity, RAM user authorization, and required parameters. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # - false: performs a dry run and performs the actual request. If the check succeeds, a 2XX HTTP status code is returned and the resource status is queried.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # > This parameter is deprecated.
        self.fuzzy_query = fuzzy_query
        # Specifies whether to query the capacity information of the security group. When set to True, the `EcsCount` and `AvailableInstanceAmount` values in the response are valid.
        # > This parameter is deprecated.
        self.is_query_ecs_count = is_query_ecs_count
        # The maximum number of entries per page for a paged query. Once this parameter is set, the query uses the combination of `MaxResults` and `NextToken` parameters.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The network type of the security group. Valid values:
        # 
        # - vpc: Virtual Private Cloud (VPC).
        # - classic: classic network.
        self.network_type = network_type
        # The query token. Set the value to the NextToken value returned in the previous call to this operation. You do not need to set this parameter for the first call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to be deprecated. We recommend that you use NextToken and MaxResults for paged queries.
        self.page_number = page_number
        # > This parameter is about to be deprecated. We recommend that you use NextToken and MaxResults for paged queries.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the latest region list of Alibaba Cloud.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the security group belongs. When you use this parameter to filter resources, the number of resources cannot exceed 1000. You can call [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) to query the list of resource groups.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The list of security group IDs. A maximum of 100 security group IDs are supported at a time. The IDs are separated by commas (,) in the format of a JSON array.
        self.security_group_ids = security_group_ids
        # The name of the security group.
        self.security_group_name = security_group_name
        # The type of the security group. Valid values:
        # - normal: basic security group.
        # - enterprise: advanced security group.
        # 
        # > If you do not specify this parameter, all types of security groups are queried.
        self.security_group_type = security_group_type
        # Specifies whether the security group is managed. Valid values:
        # 
        # - true: The security group is managed.
        # - false: The security group is not managed.
        self.service_managed = service_managed
        # The list of tags.
        self.tag = tag
        # The ID of the VPC to which the security group belongs.
        self.vpc_id = vpc_id

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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.fuzzy_query is not None:
            result['FuzzyQuery'] = self.fuzzy_query

        if self.is_query_ecs_count is not None:
            result['IsQueryEcsCount'] = self.is_query_ecs_count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        if self.security_group_type is not None:
            result['SecurityGroupType'] = self.security_group_type

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FuzzyQuery') is not None:
            self.fuzzy_query = m.get('FuzzyQuery')

        if m.get('IsQueryEcsCount') is not None:
            self.is_query_ecs_count = m.get('IsQueryEcsCount')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        if m.get('SecurityGroupType') is not None:
            self.security_group_type = m.get('SecurityGroupType')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSecurityGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeSecurityGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the security group. Valid values of N: 1 to 20.
        # 
        # When you use a single tag to filter resources, the number of resources with the tag cannot exceed 1000. When you use multiple tags to filter resources, the number of resources bound with all specified tags cannot exceed 1000. If the number of resources exceeds 1000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query.
        self.key = key
        # The tag value of the security group. Valid values of N: 1 to 20.
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

