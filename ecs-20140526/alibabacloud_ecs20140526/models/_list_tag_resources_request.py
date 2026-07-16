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
        # The pagination token to retrieve the next page of results.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the resource is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of an ECS resource. The value of N ranges from 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # - instance: ECS instance
        # 
        # - disk: disk
        # 
        # - snapshot: snapshot
        # 
        # - image: image
        # 
        # - securitygroup: security group
        # 
        # - volume: volume
        # 
        # - eni: elastic network interface
        # 
        # - ddh: dedicated host
        # 
        # - ddhcluster: dedicated host cluster
        # 
        # - keypair: SSH key pair
        # 
        # - launchtemplate: launch template
        # 
        # - reservedinstance: reserved instance
        # 
        # - snapshotpolicy: snapshot policy
        # 
        # - elasticityassurance: Elasticity Assurance
        # 
        # - capacityreservation: capacity reservation
        # 
        # - command: Cloud Assistant command
        # 
        # - invocation: The result of a command execution or file delivery in Cloud Assistant
        # 
        # - activation: Cloud Assistant managed instance activation code
        # 
        # - managedinstance: Cloud Assistant managed instance
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # A list of tags.
        self.tag = tag
        # A list of tag filters.
        # 
        # > This parameter is in invitation-only preview and is not yet available.
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
        # The tag key to use for a fuzzy match. The tag key must be 1 to 128 characters in length. The value of N ranges from 1 to 5.
        # 
        # Use the `TagFilter.N` parameter to perform a fuzzy match on tags to find matching ECS resources. Each filter consists of one key and one or more values. A fuzzy match may have a 2-second latency and is supported only for queries that return 5,000 or fewer resources after filtering.
        # 
        # - To perform a fuzzy match by tag key (`TagFilter.N.TagKey`), you must leave the tag values (`TagFilter.N.TagValues.N`) empty. For example, to search for ECS resources that have the tag key `environment`, you can set `TagFilter.1.TagKey` to `env*` (prefix match), `*env*` (substring match), or `env` (exact match), but you must leave `TagFilter.1.TagValues` empty.
        # 
        # - To perform a fuzzy match by tag value (`TagFilter.N.TagValues.N`), you must set the tag key (`TagFilter.N.TagKey`) to an exact value. For example, to search for ECS resources with the tag key `env` and the tag value `product`, you must set `TagFilter.1.TagKey` to `env`. You can then set `TagFilter.1.TagValues.1` to `proc*` (prefix match), `*proc*` (substring match), or `proc` (exact match). For the same `TagKey`, you can use only one search pattern. If you specify multiple patterns, the system uses only the first pattern.
        # 
        # - Tag keys are combined by using a logical AND. The operation returns only the ECS resources that match all specified tag keys.
        # 
        # - Tag values for the same tag key are combined by using a logical OR. The operation returns the ECS resources that match any of the specified tag values for that tag key.
        # 
        # > You cannot specify both the `TagFilter.N` and `Tag.N` parameters in the same request.
        self.tag_key = tag_key
        # The tag values to use for a fuzzy match. The tag value must be 1 to 128 characters in length. The value of N ranges from 1 to 5. For more information, see the description of the `TagFilter.N.TagKey` parameter.
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
        # The tag key to use for an exact match. The tag key must be 1 to 128 characters in length. The value of N ranges from 1 to 20.
        # 
        # Usage notes for the `Tag.N` parameter:
        # 
        # - Method 1: To find ECS resources that have specific tags.
        # 
        #   - If you specify only `Tag.N.Key`, the operation returns all resources that have the specified tag key.
        # 
        #   - If you specify only `Tag.N.Value`, the operation returns an `InvalidParameter.TagValue` error.
        # 
        #   - If you specify multiple tag key-value pairs, the operation returns only the ECS resources that match all specified pairs.
        # 
        # - Method 2: To query resources in a non-default resource group.
        # 
        #   - If you set `Key` to `acs:rm:rgId`, you must set `Value` to the ID of a non-default resource group. If you specify the ID of the default resource group, the operation returns an error.
        # 
        #   - If you set `Key` to `acs:rm:rgId`, you cannot specify other tag key-value pairs. If you use multiple `Tag.N` parameters to query for resources by both resource group and tag, the operation returns an error.
        self.key = key
        # The tag value to use for an exact match. The tag value must be 1 to 128 characters in length. The value of N ranges from 1 to 20.
        # 
        # > When `Key` is `acs:rm:rgId`, you must set this parameter to the ID of a non-default resource group.
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

