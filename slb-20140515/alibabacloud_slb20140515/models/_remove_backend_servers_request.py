# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveBackendServersRequest(DaraModel):
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
        # The backend servers that you want to remove.
        # 
        # *   **ServerId**: The IDs of the backend servers. Set the value to a string. This parameter is required.
        # 
        # *   **Type**: the type of the backend server. Valid values:
        # 
        #     *   **ecs** (default): Elastic Compute Service (ECS) instance
        #     *   **eni**: elastic network interface (ENI)
        #     *   **eci**: elastic container instance
        # 
        # *   **Weight**: the weight of the backend server. Valid values: **0** to **100**. Set the value to an integer.
        # 
        # You can specify at most 20 backend servers in each call. Examples:
        # 
        # *   Remove ECS instances:
        # 
        # `[{"ServerId":"i-bp1fq61enf4loa5i****", "Type": "ecs","Weight":"100"}]`
        # 
        # *   Remove ENIs:
        # 
        # `[{"ServerId":"eni-2ze1sdp5****","Type": "eni","Weight":"100"}]`
        # 
        # *   Remove elastic container instances:
        # 
        # `[{"ServerId":"eci-2ze1sdp5****","Type": "eci","Weight":"100"}]`
        # 
        # This parameter is required.
        self.backend_servers = backend_servers
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CLB instance is deployed.
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

