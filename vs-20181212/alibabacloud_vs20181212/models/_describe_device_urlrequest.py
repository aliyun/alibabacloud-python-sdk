# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeviceURLRequest(DaraModel):
    def __init__(
        self,
        auth: bool = None,
        expire: int = None,
        id: str = None,
        mode: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        stream: str = None,
        type: str = None,
    ):
        self.auth = auth
        self.expire = expire
        # This parameter is required.
        self.id = id
        self.mode = mode
        # This parameter is required.
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        # This parameter is required.
        self.stream = stream
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

