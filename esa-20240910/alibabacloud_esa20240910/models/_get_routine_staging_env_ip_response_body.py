# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetRoutineStagingEnvIpResponseBody(DaraModel):
    def __init__(
        self,
        ipv4: List[str] = None,
        request_id: str = None,
    ):
        # The IPv4 addresses.
        self.ipv4 = ipv4
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv4 is not None:
            result['IPV4'] = self.ipv4

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPV4') is not None:
            self.ipv4 = m.get('IPV4')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

