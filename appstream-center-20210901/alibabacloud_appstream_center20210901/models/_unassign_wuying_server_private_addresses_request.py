# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnassignWuyingServerPrivateAddressesRequest(DaraModel):
    def __init__(
        self,
        private_ip_addresses: List[str] = None,
        wuying_server_id: str = None,
    ):
        # This parameter is required.
        self.private_ip_addresses = private_ip_addresses
        # This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_ip_addresses is not None:
            result['PrivateIpAddresses'] = self.private_ip_addresses

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddresses') is not None:
            self.private_ip_addresses = m.get('PrivateIpAddresses')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

