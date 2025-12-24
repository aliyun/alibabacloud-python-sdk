# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddBackendServersRequest(DaraModel):
    def __init__(
        self,
        backend_servers: str = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The list of backend servers that you want to add. Set the following parameters:
        # 
        # *   **ServerId**: Required. This value must be a string. Enter the ID of an ECS instance, elastic network interface (ENI), or elastic container instance. If **ServerId** is set to the ID of an ENI or elastic container instance, **Type** is required.
        # 
        # *   **Weight**: the weight of the backend server. Valid values: **0** to **100**. Default value: **100**.
        # 
        #     If the value is set to 0, no requests are forwarded to the backend server.
        # 
        # *   **Description**: Optional. The description of the backend server. This value must be a string. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs** (default): an ECS instance
        #     *   **eni**: an ENI
        #     *   **eci**: an elastic container instance
        # 
        # >  You can specify ENIs and elastic container instances as the backend servers only for high-performance CLB instances.
        # 
        # *   **ServerIp**: the IP address of the ECS instance, ENI, or elastic container instance
        # *   **Port**: the backend port
        # 
        # Examples:
        # 
        # *   ECS instance: `[{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"test-112" }]`
        # *   ENI: `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-112" }]`
        # *   ENI with multiple IP addresses: `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-113" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``172.166.**.**``", "Port":"80","Description":"test-113" }]`
        # *   Elastic container instance: `[{ "ServerId": "eci-xxxxxxxxx", "Weight": "100", "Type": "eci", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-114" }]`
        # 
        # >  The backend servers that you add to a CLB instance must be in the Running state. You can add at most 20 backend servers to a CLB instance in each request.
        self.backend_servers = backend_servers
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

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

        return self

