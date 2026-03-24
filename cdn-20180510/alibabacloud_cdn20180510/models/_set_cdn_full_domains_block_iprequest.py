# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCdnFullDomainsBlockIPRequest(DaraModel):
    def __init__(
        self,
        block_interval: int = None,
        iplist: str = None,
        operation_type: str = None,
        update_type: str = None,
    ):
        # The duration for which IP addresses or CIDR blocks are blocked. Unit: seconds. The value **0** specifies that IP addresses or CIDR blocks are permanently blocked. This parameter is available only if you set **OperationType** to **block**.
        self.block_interval = block_interval
        # The IP addresses that you want to block or unblock. Separate multiple IP addresses with commas (,). You can specify up to 1,000 IP addresses.
        # 
        # This parameter is required.
        self.iplist = iplist
        # The type of the operation.
        # 
        # *   block
        # *   unblock
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # The type of the blocking duration. This parameter is available only if you set **OperationType** to **block**. Valid values:
        # 
        # *   **cover**: The blocking duration that is specified in the request takes effect.
        # *   **uncover**: The longer one of the blocking duration that is specified in the request and the remaining blocking duration takes effect.
        # *   Default value: cover.
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_interval is not None:
            result['BlockInterval'] = self.block_interval

        if self.iplist is not None:
            result['IPList'] = self.iplist

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.update_type is not None:
            result['UpdateType'] = self.update_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockInterval') is not None:
            self.block_interval = m.get('BlockInterval')

        if m.get('IPList') is not None:
            self.iplist = m.get('IPList')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')

        return self

