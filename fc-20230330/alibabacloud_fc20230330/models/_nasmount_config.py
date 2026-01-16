# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NASMountConfig(DaraModel):
    def __init__(
        self,
        enable_tls: bool = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.enable_tls = enable_tls
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')

        return self

