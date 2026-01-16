# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDedicatedIpWarmUpInfoRequest(DaraModel):
    def __init__(
        self,
        dedicated_ip: str = None,
    ):
        self.dedicated_ip = dedicated_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')

        return self

