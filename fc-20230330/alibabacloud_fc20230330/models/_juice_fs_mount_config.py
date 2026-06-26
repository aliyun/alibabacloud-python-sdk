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
        # An array of strings containing additional command-line arguments for the mount command. For example, use these arguments to set cache sizes or other performance-tuning options.
        self.args = args
        # The path within the function\\"s local filesystem to mount the volume. For example, /mnt/data. This parameter is required.
        self.mount_dir = mount_dir
        # The subdirectory within the JuiceFS volume to mount. If not specified, the root of the volume is mounted.
        self.remote_dir = remote_dir
        # The authentication token to access the JuiceFS volume.
        self.token = token
        # The name of the JuiceFS volume to mount. This parameter is required.
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

