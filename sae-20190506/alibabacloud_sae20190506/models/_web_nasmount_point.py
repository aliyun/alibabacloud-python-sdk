# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebNASMountPoint(DaraModel):
    def __init__(
        self,
        mount_dir: str = None,
        nas_addr: str = None,
        nas_path: str = None,
    ):
        self.mount_dir = mount_dir
        self.nas_addr = nas_addr
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir

        if self.nas_addr is not None:
            result['NasAddr'] = self.nas_addr

        if self.nas_path is not None:
            result['NasPath'] = self.nas_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')

        if m.get('NasAddr') is not None:
            self.nas_addr = m.get('NasAddr')

        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')

        return self

