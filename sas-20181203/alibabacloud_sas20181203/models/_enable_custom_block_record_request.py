# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableCustomBlockRecordRequest(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        bound: str = None,
        resource_owner_id: int = None,
    ):
        # The IP address that is specified in the policy.
        # 
        # This parameter is required.
        self.block_ip = block_ip
        # The traffic direction that is specified in the policy. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # This parameter is required.
        self.bound = bound
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.bound is not None:
            result['Bound'] = self.bound

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

