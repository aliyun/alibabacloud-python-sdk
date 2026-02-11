# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckServiceLinkedRoleForDeletingRequest(DaraModel):
    def __init__(
        self,
        deletion_task_id: str = None,
        region_id: str = None,
        role_arn: str = None,
        spiregion_id: str = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.deletion_task_id = deletion_task_id
        self.region_id = region_id
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.spiregion_id = spiregion_id
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

