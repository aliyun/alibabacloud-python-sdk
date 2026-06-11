# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataMountInfo(DaraModel):
    def __init__(
        self,
        mount_folder_name: str = None,
        oss_bucket: str = None,
        prefix: str = None,
        read_only: bool = None,
    ):
        # The name of the mount directory. The actual mount path is prefixed with /Workspace/data/.
        self.mount_folder_name = mount_folder_name
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The prefix. If this parameter is not specified, the root directory is used.
        self.prefix = prefix
        # Whether to mount the data volume as read-only.
        # 
        # Default value: false.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_folder_name is not None:
            result['MountFolderName'] = self.mount_folder_name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountFolderName') is not None:
            self.mount_folder_name = m.get('MountFolderName')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        return self

