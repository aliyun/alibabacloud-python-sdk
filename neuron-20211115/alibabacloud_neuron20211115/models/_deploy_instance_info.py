# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployInstanceInfo(DaraModel):
    def __init__(
        self,
        ip: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.ip = ip
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['ip'] = self.ip

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

