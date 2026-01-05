# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelPolarFsFileQuotaRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_path_ids: str = None,
        polar_fs_instance_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.file_path_ids = file_path_ids
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.file_path_ids is not None:
            result['FilePathIds'] = self.file_path_ids

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FilePathIds') is not None:
            self.file_path_ids = m.get('FilePathIds')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

