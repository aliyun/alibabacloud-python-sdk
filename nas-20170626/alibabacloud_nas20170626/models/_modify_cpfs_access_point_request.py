# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCpfsAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        description: str = None,
        file_system_id: str = None,
        region_id: str = None,
    ):
        # The access point ID.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The description of the access point.
        self.description = description
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, for example, cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, for example, bmcpfs-0015\\*\\*\\*\\*.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

