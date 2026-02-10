# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableBruteForceRecordRequest(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        bound: str = None,
        id: int = None,
        port: str = None,
        resource_owner_id: int = None,
        uuid: str = None,
    ):
        # The IP address that is specified in the policy.
        # 
        # This parameter is required.
        self.block_ip = block_ip
        # The traffic direction that is specified in the policy. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.bound = bound
        # The ID of the policy that you want to enable.
        # 
        # > You can call the [DescribeBruteForceRecords](~~DescribeBruteForceRecords~~) operation to query the IDs of policies.
        self.id = id
        # The port number.
        self.port = port
        self.resource_owner_id = resource_owner_id
        # The UUID of the server.
        # 
        # This parameter is required.
        self.uuid = uuid

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

        if self.id is not None:
            result['Id'] = self.id

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

