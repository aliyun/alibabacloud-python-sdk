# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIpProtectionResponseBody(DaraModel):
    def __init__(
        self,
        ip_protection: str = None,
        request_id: str = None,
    ):
        # IP protection switch, On: 1 Off: 0
        self.ip_protection = ip_protection
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_protection is not None:
            result['IpProtection'] = self.ip_protection

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtection') is not None:
            self.ip_protection = m.get('IpProtection')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

