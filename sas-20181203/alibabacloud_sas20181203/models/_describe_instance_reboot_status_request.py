# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceRebootStatusRequest(DaraModel):
    def __init__(
        self,
        uuids: str = None,
    ):
        # The UUIDs of the servers that you restart. Separate multiple UUIDs with commas (,).
        # 
        # This parameter is required.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

