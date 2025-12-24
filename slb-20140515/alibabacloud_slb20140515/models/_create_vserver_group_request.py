# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateVServerGroupRequest(DaraModel):
    def __init__(
        self,
        backend_servers: str = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateVServerGroupRequestTag] = None,
        vserver_group_name: str = None,
    ):
        # The backend servers that you want to add. Configure the following parameters:
        # 
        # *   **ServerId**:  required. The ID of the backend server. Specify the ID in a string. You can specify the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. If you set ServerId to the ID of an ENI or an elastic container instance, you must configure the Type parameter.
        # 
        # *   **Weight**: the weight of the backend server. Valid values: 0 to 100. Default value: 100. If you set the weight of a backend server to 0, no requests are forwarded to the backend server.
        # 
        # *   **Description**: optional. The description of the backend server. Specify the description in a string. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs (default)**: ECS instance
        #     *   **eni**: ENI.
        #     *   **eni**: elastic container instance.
        # 
        # > You can specify ENIs and elastic container instances as backend servers only for high-performance SLB instances.
        # 
        # *   **ServerIp**: The IP address of the ECS instance or ENI.
        # *   **Port**: the backend port.
        # 
        # Examples:
        # 
        # - Add an ECS instance:
        # 
        #   `[{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"test-112" }]`
        # - Add an ENI:
        # 
        #   ` [{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-112" }]`
        # - Add an ENI with multiple IP addresses:
        # 
        #    `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-113" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``172.166.**.**``", "Port":"80","Description":"test-113" }]`
        # - Add an elastic container instance:
        # 
        #   ` [{ "ServerId": "eci-xxxxxxxxx", "Weight": "100", "Type": "eci", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-114" }]`
        # 
        # > You can add only running backend servers to SLB instances. You can specify at most 20 backend servers.
        self.backend_servers = backend_servers
        # The ID of the Server Load Balancer (SLB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SLB instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag
        # The name of the vServer group.
        # 
        # The name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (_).
        self.vserver_group_name = vserver_group_name

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
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

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

        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

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
                temp_model = main_models.CreateVServerGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')

        return self

class CreateVServerGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
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

