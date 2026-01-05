# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClonePolarFsBasicSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
        request_id: str = None,
        source_path: str = None,
        target_path: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.polar_fs_instance_id = polar_fs_instance_id
        # Id of the request
        self.request_id = request_id
        self.source_path = source_path
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        return self

