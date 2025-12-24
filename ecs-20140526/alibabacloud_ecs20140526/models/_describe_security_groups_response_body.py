# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        security_groups: main_models.DescribeSecurityGroupsResponseBodySecurityGroups = None,
        total_count: int = None,
    ):
        # A pagination token. If the return value of this parameter is empty when MaxResults and NextToken are used for a paged query, no next page exists.
        self.next_token = next_token
        # The page number.
        # 
        # > This parameter will be deprecated in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # > This parameter will be deprecated in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.page_size = page_size
        # The region ID of the security group.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The information about the security groups.
        self.security_groups = security_groups
        # The total number of security groups returned. If `MaxResults` and `NextToken` are specified in the request, the value of this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroups') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m.get('SecurityGroups'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSecurityGroupsResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        security_group: List[main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            for v1 in self.security_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k1 in self.security_group:
                result['SecurityGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group = []
        if m.get('SecurityGroup') is not None:
            for k1 in m.get('SecurityGroup'):
                temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup(DaraModel):
    def __init__(
        self,
        available_instance_amount: int = None,
        creation_time: str = None,
        description: str = None,
        ecs_count: int = None,
        group_to_group_rule_count: int = None,
        resource_group_id: str = None,
        rule_count: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
        security_group_type: str = None,
        service_id: int = None,
        service_managed: bool = None,
        tags: main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTags = None,
        vpc_id: str = None,
    ):
        # The number of private IP addresses that can be added to the security group. For more information, see the "Security group capacity" section in [Basic security groups and advanced security groups](~~605897#section-kj9-e46-6v5~~).
        # 
        # If you set IsQueryEcsCount to True, the return value of AvailableInstanceAmount is valid.
        # 
        # >  This parameter is deprecated. The returned quantity is provided only for reference. The actual quantity may differ from the returned quantity.
        self.available_instance_amount = available_instance_amount
        # The time when the security group was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the security group.
        self.description = description
        # The number of private IP addresses that are contained in the security group. For more information, see the "Security group capacity" section in [Basic security groups and advanced security groups](~~605897#section-kj9-e46-6v5~~).
        # 
        # If you set IsQueryEcsCount to True, the return value of EcsCount is valid.
        # 
        # >  This parameter is deprecated. The returned quantity is provided only for reference. The actual quantity may differ from the returned quantity.
        self.ecs_count = ecs_count
        # The number of rules that reference security groups in the security group.
        self.group_to_group_rule_count = group_to_group_rule_count
        # The ID of the resource group to which the security group belongs.
        self.resource_group_id = resource_group_id
        # The number of rules in the security group.
        self.rule_count = rule_count
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the security group.
        self.security_group_name = security_group_name
        # The type of the security group. Valid values:
        # 
        # *   normal: basic security group
        # *   enterprise: advanced security group
        self.security_group_type = security_group_type
        # The ID of the distributor to which the security group belongs.
        self.service_id = service_id
        # Indicates whether the user of the security group is an Alibaba Cloud service or a distributor.
        self.service_managed = service_managed
        # The tags of the security group.
        self.tags = tags
        # The ID of the VPC to which the security group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_amount is not None:
            result['AvailableInstanceAmount'] = self.available_instance_amount

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.group_to_group_rule_count is not None:
            result['GroupToGroupRuleCount'] = self.group_to_group_rule_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        if self.security_group_type is not None:
            result['SecurityGroupType'] = self.security_group_type

        if self.service_id is not None:
            result['ServiceID'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceAmount') is not None:
            self.available_instance_amount = m.get('AvailableInstanceAmount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('GroupToGroupRuleCount') is not None:
            self.group_to_group_rule_count = m.get('GroupToGroupRuleCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        if m.get('SecurityGroupType') is not None:
            self.security_group_type = m.get('SecurityGroupType')

        if m.get('ServiceID') is not None:
            self.service_id = m.get('ServiceID')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroupTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

