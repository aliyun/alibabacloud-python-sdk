# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserGroupsMappingShrinkRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        group_names_shrink: str = None,
        input_region_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.file_system_id = file_system_id
        self.group_names_shrink = group_names_shrink
        # This parameter is required.
        self.input_region_id = input_region_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.group_names_shrink is not None:
            result['GroupNames'] = self.group_names_shrink

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('GroupNames') is not None:
            self.group_names_shrink = m.get('GroupNames')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

