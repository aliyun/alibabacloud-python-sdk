# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OssConfiguration(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        mount_point: str = None,
        permission: str = None,
        prefix: str = None,
        region: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        # The mount point for the OSS bucket.
        # 
        # This parameter is required.
        self.mount_point = mount_point
        # The access permission for the mount point.
        self.permission = permission
        # The object prefix or path within the OSS bucket.
        # 
        # This parameter is required.
        self.prefix = prefix
        # The region where the OSS bucket is located.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.mount_point is not None:
            result['mountPoint'] = self.mount_point

        if self.permission is not None:
            result['permission'] = self.permission

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('mountPoint') is not None:
            self.mount_point = m.get('mountPoint')

        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

