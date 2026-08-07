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
        # The token used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ECS resource ID. Valid values of N: 1 to 50.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # - instance: ECS instance.
        # - disk: cloud disk.
        # - snapshot: snapshot.
        # - image: image.
        # - securitygroup: security group.
        # - volume: storage volume.
        # - eni: Elastic Network Interface (ENI).
        # - ddh: dedicated host.
        # - ddhcluster: dedicated host cluster.
        # - keypair: SSH key pair.
        # - launchtemplate: launch template.
        # - reservedinstance: reserved instance.
        # - snapshotpolicy: automatic snapshot policy.
        # - elasticityassurance: elasticity assurance.
        # - capacityreservation: capacity reservation.
        # - command: Cloud Assistant command.
        # - invocation: Cloud Assistant command execution or file sending result.
        # - activation: Cloud Assistant managed instance activation code.
        # - managedinstance: Cloud Assistant managed instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        self.tag = tag
        # The tag filter rules.
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
        # The tag key used to perform a fuzzy search for ECS resources. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 5.
        # 
        # `TagFilter.N` is used to perform a fuzzy search for ECS resources that have the specified tags bound. It consists of a key and one or more values. A fuzzy search may have a latency of up to 2 seconds and supports only scenarios where the number of resources after fuzzy filtering is less than or equal to 5,000.
        # 
        # - When you perform a fuzzy search for ECS resources by tag key (`TagFilter.N.TagKey`), the tag value (`TagFilter.N.TagValues.N`) must be empty. For example, to perform a fuzzy search for ECS resources whose tag key is `environment`, you can set `TagFilter.1.TagKey` to `env*` (prefix match), `*env*` (infix match), or `env` (exact match), and `TagFilter.1.TagValues` must be empty.
        # 
        # - When you perform a fuzzy search for ECS resources by tag value (`TagFilter.N.TagValues.N`), the tag key (`TagFilter.N.TagKey`) must be set to an exact value. For example, to perform a fuzzy search for ECS resources whose tag key is `env` and tag value is `product`, `TagFilter.1.TagKey` must be set to the exact value `env`, and `TagFilter.1.TagValues.1` can be set to `proc*` (prefix match), `*proc*` (infix match), or `proc` (exact match). Only one search method can be used for the same `TagKey`. If multiple search methods are specified, the first method takes precedence.
        # 
        # - Tag keys have an AND relationship. Only ECS resources that match all specified tag keys are returned.
        # 
        # - Tag values under the same tag key have an OR relationship. ECS resources that match any of the tag values specified for a tag key are returned.
        # 
        # > The `TagFilter.N` and `Tag.N` parameters cannot be used at the same time. Otherwise, an error message is returned.
        self.tag_key = tag_key
        # The tag value used to perform a fuzzy search for ECS resources. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 5. For the metric description, see the `TagFilter.N.TagKey` parameter description.
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
        # The tag key used to perform an exact search for ECS resources. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # Usage notes of the `Tag.N` parameter:
        # 
        # - Method 1: Used to perform an exact search for ECS resources that have the specified tags bound. Each tag is a key-value pair.
        # 
        #     - If you specify only `Tag.N.Key`, all resources associated with the tag key are returned.
        # 
        #     - If you specify only `Tag.N.Value`, the `InvalidParameter.TagValue` error is returned.
        # 
        #     - If you specify multiple tag key-value pairs at the same time, only ECS resources that match all the specified tag key-value pairs are returned.
        # 
        # - Method 2: Used to query resource information in non-default resource groups. Set `Key` to `acs:rm:rgId` and set the corresponding `Value` to the resource group ID.
        # 
        #     - If `Key` is set to `acs:rm:rgId`, `Value` can only be set to a non-default resource group ID. If the specified resource group ID is the default resource group, an error message is returned.
        # 
        #     - If `Key` is set to `acs:rm:rgId`, you cannot specify other tag key-value pairs. If you use multiple `Tag.N` parameters to query resources by resource group and tags at the same time, an error message is returned.
        self.key = key
        # The tag value used to perform an exact search for ECS resources. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # > If `Key=acs:rm:rgId`, this parameter can only be set to a resource group ID, and the resource group ID cannot be the default resource group.
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

