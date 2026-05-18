# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVscMountPointShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        instance_ids_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        self.instance_ids_shrink = instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        return self

