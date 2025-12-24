# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVServerGroupBackendServersRequest(DaraModel):
    def __init__(
        self,
        new_backend_servers: str = None,
        old_backend_servers: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vserver_group_id: str = None,
    ):
        # The backend servers that you want to add to the vServer group. Configure the following parameters:
        # 
        # *   **ServerId**: required. The IDs of the backend servers. Specify the IDs in a string. You can specify the IDs of ECS instances, ENIs, and elastic container instances. If you set **ServerId** to the IDs of ENIs or elastic container instances, you must configure the **Type** parameter.
        # 
        # *   **Weight**: the weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If you set the weight of a backend server to 0, no requests are forwarded to the backend server.
        # 
        # *   **Description**: optional. The description of the backend servers. Specify the description in a string. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/). periods (.), and underscores (_).
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs** (default): ECS instance
        #     *   **eni**: ENI
        #     *   **eci**: elastic container instance
        # 
        # >  You can specify ENIs and elastic container instances as backend servers only for high-performance SLB instances.
        # 
        # *   **ServerIp**: the IP address of the ENI or elastic container instance.
        # *   **Port**: the backend port.
        # 
        # Examples:
        # 
        # *   Add an ECS instance:
        # 
        #     `[{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add an ENI:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add an ENI with multiple IP addresses:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-113" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``172.166.**.**``", "Port":"80","Description":"test-113" }]`
        # 
        # *   Add an elastic container instance
        # 
        #     `[{ "ServerId": "eci-xxxxxxxxx", "Weight": "100", "Type": "eci", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-114" }]`
        # 
        # >  You can add only running backend servers to SLB instances. You can specify at most 20 backend servers in each call.
        self.new_backend_servers = new_backend_servers
        # The backend servers that you want to replace. Configure the following parameters:
        # 
        # *   **ServerId**: required. The IDs of the backend servers. Specify the IDs in a string. You can specify the IDs of Elastic Compute Service (ECS) instances, elastic network interfaces (ENIs), and elastic container instances. If you set **ServerId** to the IDs of ENIs or elastic container instances, you must configure the **Type** parameter.
        # 
        # *   **Weight**: the weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If you set the weight of a backend server to 0, no requests are forwarded to the backend server.
        # 
        # *   **Description**: optional. The description of the backend servers. Specify the description in a string. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/). periods (.), and underscores (_).
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs** (default): ECS instance
        #     *   **eni**: ENI
        #     *   **eci**: elastic container instance
        # 
        # >  You can specify ENIs and elastic container instances as backend servers only for high-performance SLB instances.
        # 
        # *   **ServerIp**: the IP address of the ENI or elastic container instance.
        # *   **Port**: the backend port.
        # 
        # Examples:
        # 
        # *   Add an ECS instance:
        # 
        #     `[{ "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add an ENI:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-112" }]`
        # 
        # *   Add an ENI with multiple IP addresses:
        # 
        #     `[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-113" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "``172.166.**.**``", "Port":"80","Description":"test-113" }]`
        # 
        # *   Add an elastic container instance
        # 
        #     `[{ "ServerId": "eci-xxxxxxxxx", "Weight": "100", "Type": "eci", "ServerIp": "``192.168.**.**``", "Port":"80","Description":"test-114" }]`
        # 
        # >  You can add only running backend servers to SLB instances. You can specify at most 20 backend servers in each call.
        self.old_backend_servers = old_backend_servers
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the vServer group.
        # 
        # This parameter is required.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_backend_servers is not None:
            result['NewBackendServers'] = self.new_backend_servers

        if self.old_backend_servers is not None:
            result['OldBackendServers'] = self.old_backend_servers

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewBackendServers') is not None:
            self.new_backend_servers = m.get('NewBackendServers')

        if m.get('OldBackendServers') is not None:
            self.old_backend_servers = m.get('OldBackendServers')

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

        return self

