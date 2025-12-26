# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CacheInfo(DaraModel):
    def __init__(
        self,
        mount_point: str = None,
        port: str = None,
    ):
        self.mount_point = mount_point
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

