# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HostAlias(DaraModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames

        if self.ip is not None:
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self

