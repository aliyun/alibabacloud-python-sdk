# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddBackendServersShrinkRequest(DaraModel):
    def __init__(
        self,
        backend_servers_shrink: str = None,
        load_balancer_id: str = None,
    ):
        # The list of backend servers that you want to add to the Edge Load Balancer (ELB) instance. You can add up to 20 backend servers at a time.
        # 
        # >  Only Edge Node Service (ENS) instances that are in the running state can be added to the ELB instance as backend servers.
        # 
        # This parameter is required.
        self.backend_servers_shrink = backend_servers_shrink
        # The frontend port that is used by the Edge Load Balance (ELB) instance. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_servers_shrink is not None:
            result['BackendServers'] = self.backend_servers_shrink

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers_shrink = m.get('BackendServers')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        return self

