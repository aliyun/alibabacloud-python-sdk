# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebOSSMountPoint(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_dir: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.mount_dir = mount_dir
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path

        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')

        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        return self

