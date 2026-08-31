# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCpfsAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The access point ID.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c****.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya****.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

