# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListRouteTargetGroupsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        max_results: int = None,
        member_id: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_target_group_ids: List[str] = None,
        tag: List[main_models.ListRouteTargetGroupsRequestTag] = None,
        vpc_id: str = None,
    ):
        # Client token used to ensure idempotence of the request. Generate a unique parameter value from your client to ensure uniqueness across different requests. ClientToken only supports ASCII characters. Note: If you do not specify this, the system will automatically use the RequestId of the API request as the ClientToken identifier. The RequestId is different for each API request.
        self.client_token = client_token
        # Page size, with a range of **1** to **50**. Default value: **50**.
        self.max_results = max_results
        # Route target group member instance ID.
        # Filters the route target groups that contain the specified member instance ID.
        self.member_id = member_id
        # Token for the next query. Value: If it is the first query or there is no next query, this field does not need to be filled. If there is a next query, the value should be the NextToken returned from the previous API call.
        self.next_token = next_token
        # The region ID of the VPC to which the route target group belongs. You can obtain the region ID by calling the DescribeRegions interface.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group ID. For more information about resource groups, see What is a Resource Group?
        self.resource_group_id = resource_group_id
        # List of route target group instance IDs.
        # 
        # Up to 50 instance IDs can be queried at a time.
        self.route_target_group_ids = route_target_group_ids
        # List of tags.
        self.tag = tag
        # The ID of the VPC to which the route target group belongs.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_target_group_ids is not None:
            result['RouteTargetGroupIds'] = self.route_target_group_ids

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteTargetGroupIds') is not None:
            self.route_target_group_ids = m.get('RouteTargetGroupIds')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListRouteTargetGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListRouteTargetGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Resource tag key. Up to 20 tag keys are supported. If you need to pass this value, you cannot input an empty string.
        # 
        # A tag key can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # Resource tag value. Up to 20 tag values are supported. If you need to pass this value, you can input an empty string.
        # 
        # A tag value can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

