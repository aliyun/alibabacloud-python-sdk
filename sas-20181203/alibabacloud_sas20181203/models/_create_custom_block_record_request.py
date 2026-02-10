# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomBlockRecordRequest(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        bound: str = None,
        expire_time: int = None,
        resource_owner_id: int = None,
        uuids: str = None,
    ):
        # The IP address that you want to specify in the policy.
        # 
        # This parameter is required.
        self.block_ip = block_ip
        # The traffic direction that you want to specify in the policy. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # This parameter is required.
        self.bound = bound
        # The expiration time of the policy.
        # 
        # This parameter is required.
        self.expire_time = expire_time
        self.resource_owner_id = resource_owner_id
        # The UUIDs of the servers. Separate multiple UUIDs with commas (,).
        # 
        # This parameter is required.
        self.uuids = uuids

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

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

