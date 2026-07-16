# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable_preset_model: bool = None,
        name: str = None,
        resource_group_id: str = None,
    ):
        self.description = description
        self.enable_preset_model = enable_preset_model
        self.name = name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.enable_preset_model is not None:
            result['enablePresetModel'] = self.enable_preset_model

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enablePresetModel') is not None:
            self.enable_preset_model = m.get('enablePresetModel')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

