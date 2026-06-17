# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClonePolarFsBasicSnapshotRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
        source_path: str = None,
        target_path: str = None,
    ):
        # The ID of the database cluster.
        self.dbcluster_id = dbcluster_id
        # The ID of the Polarlakebase instance.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The source path of the file resource. This parameter is empty if the type is local.
        self.source_path = source_path
        # The destination path.
        self.target_path = target_path

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

        if self.source_path is not None:
            result['SourcePath'] = self.source_path

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        return self

