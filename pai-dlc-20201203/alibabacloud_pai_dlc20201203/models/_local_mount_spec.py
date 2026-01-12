# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LocalMountSpec(DaraModel):
    def __init__(
        self,
        local_path: str = None,
        mount_mode: str = None,
        mount_path: str = None,
    ):
        self.local_path = local_path
        self.mount_mode = mount_mode
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_path is not None:
            result['LocalPath'] = self.local_path

        if self.mount_mode is not None:
            result['MountMode'] = self.mount_mode

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalPath') is not None:
            self.local_path = m.get('LocalPath')

        if m.get('MountMode') is not None:
            self.mount_mode = m.get('MountMode')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

