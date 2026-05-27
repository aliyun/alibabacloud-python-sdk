# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssignWuyingServerPrivateAddressesResponseBody(DaraModel):
    def __init__(
        self,
        assigned_private_ip_addresses: List[str] = None,
        request_id: str = None,
    ):
        self.assigned_private_ip_addresses = assigned_private_ip_addresses
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_private_ip_addresses is not None:
            result['AssignedPrivateIpAddresses'] = self.assigned_private_ip_addresses

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedPrivateIpAddresses') is not None:
            self.assigned_private_ip_addresses = m.get('AssignedPrivateIpAddresses')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

