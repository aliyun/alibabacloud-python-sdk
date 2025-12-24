# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerListenersRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeLoadBalancerListenersRequestTag] = None,
    ):
        # The description of the listener.
        self.description = description
        # The frontend port that is used by the CLB instance.
        self.listener_port = listener_port
        # The protocol used by the listener. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        # *   **http**
        # *   **https**
        self.listener_protocol = listener_protocol
        # The IDs of the CLB instances. You can specify up to 10 instance IDs.
        # 
        # >  If you do not use the SDK to call this operation, use the LoadBalancerId.N parameter.
        self.load_balancer_id = load_balancer_id
        # The number of entries to return in each call.
        # 
        # Valid values: **1** to **100**. If you do not specify this parameter, the default value **20** is used.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query and no subsequent queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the most recent region list.
        # 
        # >  If the endpoint of the selected region is slb.aliyuncs.com, the `RegionId` parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeLoadBalancerListenersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerListenersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. Valid values of N: **1 to 20**. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
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

