# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarFsAttributeRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
        query_fuse_mount_info: bool = None,
    ):
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        self.query_fuse_mount_info = query_fuse_mount_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.query_fuse_mount_info is not None:
            result['QueryFuseMountInfo'] = self.query_fuse_mount_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('QueryFuseMountInfo') is not None:
            self.query_fuse_mount_info = m.get('QueryFuseMountInfo')

        return self

