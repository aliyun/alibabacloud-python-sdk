# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeletePolarFsObjectsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        objects_to_delete: List[str] = None,
        polar_fs_instance_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.objects_to_delete = objects_to_delete
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

        if self.objects_to_delete is not None:
            result['ObjectsToDelete'] = self.objects_to_delete

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ObjectsToDelete') is not None:
            self.objects_to_delete = m.get('ObjectsToDelete')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

