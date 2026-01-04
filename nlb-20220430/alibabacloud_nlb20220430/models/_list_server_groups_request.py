# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListServerGroupsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        server_group_ids: List[str] = None,
        server_group_names: List[str] = None,
        server_group_type: str = None,
        tag: List[main_models.ListServerGroupsRequestTag] = None,
        vpc_id: str = None,
    ):
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   For the first request and last request, you do not need to specify this parameter.
        # *   You must specify the token obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The server group IDs. You can specify up to 20 server group IDs in each call.
        self.server_group_ids = server_group_ids
        # The names of the server groups to be queried. You can specify up to 20 names in each call.
        self.server_group_names = server_group_names
        # The type of server group. Valid values:
        # 
        # *   **Instance**: allows you to add servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type
        # The tags.
        self.tag = tag
        # The ID of the virtual private cloud (VPC) in which the server group is deployed.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.server_group_ids is not None:
            result['ServerGroupIds'] = self.server_group_ids

        if self.server_group_names is not None:
            result['ServerGroupNames'] = self.server_group_names

        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerGroupIds') is not None:
            self.server_group_ids = m.get('ServerGroupIds')

        if m.get('ServerGroupNames') is not None:
            self.server_group_names = m.get('ServerGroupNames')

        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListServerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListServerGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` and `acs:`, and cannot contain `http://` or `https://`.
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

