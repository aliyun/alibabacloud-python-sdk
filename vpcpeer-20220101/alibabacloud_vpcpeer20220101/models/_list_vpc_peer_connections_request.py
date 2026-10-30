# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcpeer20220101 import models as main_models
from darabonba.model import DaraModel

class ListVpcPeerConnectionsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListVpcPeerConnectionsRequestTags] = None,
        vpc_id: List[str] = None,
    ):
        # The instance ID of the VPC peering connection that you want to query.
        self.instance_id = instance_id
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The name of the VPC peering connection that you want to query.
        self.name = name
        # The token that is used to retrieve the next page of results. Valid values:
        # - If this is your first request or no subsequent request is to be sent, leave this parameter empty.
        # - If a subsequent request is to be sent, set the value to the NextToken value returned from the last API call.
        self.next_token = next_token
        # The region ID of the VPC peering connection that you want to query.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tags = tags
        # Filters the results by the VPC IDs of the initiator and acceptor. The filter does not distinguish between the initiator and the acceptor. If you specify only one VPC ID, the results are filtered based on the specified VPC ID.
        self.vpc_id = vpc_id

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVpcPeerConnectionsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListVpcPeerConnectionsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. If you specify this parameter, it cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. If you specify this parameter, it can be an empty string.
        # 
        # A tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

