# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PolarFsMountConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mount_dir: str = None,
        remote_dir: str = None,
    ):
        self.instance_id = instance_id
        self.mount_dir = mount_dir
        self.remote_dir = remote_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.remote_dir is not None:
            result['remoteDir'] = self.remote_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('remoteDir') is not None:
            self.remote_dir = m.get('remoteDir')

        return self

