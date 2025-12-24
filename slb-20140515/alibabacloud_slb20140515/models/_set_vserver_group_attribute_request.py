# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVServerGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        backend_servers: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
    ):
        # The backend servers. This operation only can be used to modify the weights of backend servers and names of vServer groups. Configure the following parameters:
        # 
        # *   **ServerId**: Required. The ID of the backend server. Specify the value in a string. You can specify the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. If you set **ServerId** to the ID of an ENI or an elastic container instance, you must configure the **Type** parameter.
        # 
        # *   **Weight**: the weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If you set the weight of a backend server to 0, no requests are forwarded to the backend server.
        # 
        # *   **Description**: Optional. The description of the backend server. Specify the value in a string. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs** (default): ECS instance
        #     *   **eni**: ENI
        #     *   **eci**: elastic container instance
        # 
        # >  You can specify ENIs and elastic container instances as backend servers only for high-performance CLB instances.
        # 
        # *   **ServerIp**: the IP address of an ENI or an elastic container instance.
        # *   **Port**: the backend port.
        # 
        # Examples:
        # 
        # *   Add ECS instances:
        # 
        #     `[{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add ENIs:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add ENIs with multiple IP addresses:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-113" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``172.166.**.**``", "Port":"80","Description":"test-113" }]`
        # 
        # *   Add elastic container instances:
        # 
        #     `[{ "ServerId": "eci-xxxxxxxxx", "Weight": "100", "Type": "eci", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-114" }]`
        # 
        # >  You can add only running backend servers to SLB instances. You can specify at most 20 backend servers in each call.
        self.backend_servers = backend_servers
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Server Load Balancer (SLB) instance, which cannot be modified.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The vServer group ID, which cannot be modified.
        # 
        # This parameter is required.
        self.vserver_group_id = vserver_group_id
        # The vServer group name. You can specify a name.
        self.vserver_group_name = vserver_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers

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

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')

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

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')

        return self

