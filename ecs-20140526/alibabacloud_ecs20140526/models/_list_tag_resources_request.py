# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
        tag_filter: List[main_models.ListTagResourcesRequestTagFilter] = None,
    ):
        # The token for the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the ECS resource. Valid values of N: 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # - instance: ECS instance
        # - disk: cloud disk
        # - snapshot: snapshot
        # - image: image
        # - securitygroup: security group
        # - volume: storage volume
        # - eni: Elastic Network Interface (ENI)
        # - ddh: dedicated host
        # - ddhcluster: dedicated host cluster
        # - keypair: SSH key pair
        # - launchtemplate: launch template
        # - reservedinstance: reserved instance
        # - snapshotpolicy: automatic snapshot policy
        # - elasticityassurance: elasticity assurance
        # - capacityreservation: capacity reservation
        # - command: Cloud Assistant command
        # - invocation: Cloud Assistant command execution or file delivery result
        # - activation: Cloud Assistant managed instance activation code
        # - managedinstance: Cloud Assistant managed instance
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tags.
        self.tag = tag
        # The tag filtering rules.
        # 
        # 
        # > This parameter is in invitational preview and is not publicly available.
        self.tag_filter = tag_filter

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.tag_filter:
            for v1 in self.tag_filter:
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

        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k1 in self.tag_filter:
                result['TagFilter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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

        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k1 in m.get('TagFilter'):
                temp_model = main_models.ListTagResourcesRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTagFilter(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # The tag key used for fuzzy match when querying ECS resources. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 5.
        # 
        # TagFilter.N is used to fuzzy query ECS resources bound to specific tags. It consists of a key and one or more values. Fuzzy queries may have a delay of 2 seconds and only support scenarios where the number of resources after fuzzy filtering is less than or equal to 5,000.
        # 
        # - When you fuzzy query ECS resources by tag key (TagFilter.N.TagKey), the tag value (TagFilter.N.TagValues.N) must be empty. For example, to fuzzy search for ECS resources with the tag key environment, you can set TagFilter.1.TagKey to env* (prefix match), *env* (infix match), or env (exact match), and TagFilter.1.TagValues must be empty.
        # 
        # - When you fuzzy query ECS resources by tag value (TagFilter.N.TagValues.N), the tag key (TagFilter.N.TagKey) must be set to an exact value. For example, to fuzzy search for ECS resources with the tag key env and the tag value product, you must set TagFilter.1.TagKey exactly to env, and you can set TagFilter.1.TagValues.1 to proc* (prefix match), *proc* (infix match), or proc (exact match). You can use only one search method under the same TagKey. If multiple different search methods are set, the first method prevails.
        # 
        # - Tag keys have an intersection relationship. Only ECS resources that meet all the specified tag keys are returned.
        # 
        # - Tag values under the same tag key have a union relationship. ECS resources that meet any of the specified tag values for the tag key are returned.
        # 
        # > You cannot use TagFilter.N and Tag.N at the same time. Otherwise, an error message is returned.
        self.tag_key = tag_key
        # The tag value used for fuzzy match when querying ECS resources. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 5. For the specific metric description, see the description of the TagFilter.N.TagKey parameter.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key used for exact match when querying ECS resources. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # Usage notes for the Tag.N parameter:
        # 
        # - Method 1: Used to exactly query ECS resources bound to specific tags. It consists of a key-value pair.
        # 
        #     - If only Tag.N.Key is specified, all resources associated with the tag key are returned.
        # 
        #     - If only Tag.N.Value is specified, the InvalidParameter.TagValue error is returned.
        # 
        #     - If multiple tag key-value pairs are specified, only ECS resources that meet all the tag key-value pairs are returned.
        # 
        # - Method 2: Used to query resources in non-default resource groups. The Key is fixed as acs:rm:rgId, and the corresponding Value is the resource group ID.
        # 
        #     - If Key is set to acs:rm:rgId, Value can only be a non-default resource group ID. If the specified resource group ID is the default resource group, an error message is returned.
        # 
        #     - If Key is set to acs:rm:rgId, you cannot specify other tag key-value pairs. If you query resources corresponding to both resource groups and tags by using multiple Tag.N parameters at the same time, an error message is returned.
        self.key = key
        # The tag value used for exact match when querying ECS resources. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # > When Key is set to acs:rm:rgId, this parameter can only be set to a resource group ID, and the resource group ID cannot be the default resource group.
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

