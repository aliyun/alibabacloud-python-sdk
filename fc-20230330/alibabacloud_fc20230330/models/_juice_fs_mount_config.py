# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class JuiceFsMountConfig(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        mount_dir: str = None,
        remote_dir: str = None,
        token: str = None,
        volume_name: str = None,
    ):
        self.args = args
        self.mount_dir = mount_dir
        self.remote_dir = remote_dir
        self.token = token
        self.volume_name = volume_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.remote_dir is not None:
            result['remoteDir'] = self.remote_dir

        if self.token is not None:
            result['token'] = self.token

        if self.volume_name is not None:
            result['volumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('remoteDir') is not None:
            self.remote_dir = m.get('remoteDir')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')

        return self

