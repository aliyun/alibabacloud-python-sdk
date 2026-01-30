# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeviceGatewayRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        expire: int = None,
        id: str = None,
        owner_id: int = None,
    ):
        self.client_ip = client_ip
        self.expire = expire
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

