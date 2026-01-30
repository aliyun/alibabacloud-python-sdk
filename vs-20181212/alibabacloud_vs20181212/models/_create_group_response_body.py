# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupResponseBody(DaraModel):
    def __init__(
        self,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: int = None,
        id: str = None,
        request_id: str = None,
    ):
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip

        if self.gb_port is not None:
            result['GbPort'] = self.gb_port

        if self.id is not None:
            result['Id'] = self.id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')

        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

