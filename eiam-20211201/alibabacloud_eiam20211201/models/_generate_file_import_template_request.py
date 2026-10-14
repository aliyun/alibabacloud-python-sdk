# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GenerateFileImportTemplateRequest(DaraModel):
    def __init__(
        self,
        field_selection_enabled: bool = None,
        instance_id: str = None,
        selected_field_names: List[str] = None,
        target_type: str = None,
    ):
        # Specifies whether field selection mode is enabled.
        self.field_selection_enabled = field_selection_enabled
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The selected fields.
        self.selected_field_names = selected_field_names
        # The synchronization target type.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_selection_enabled is not None:
            result['FieldSelectionEnabled'] = self.field_selection_enabled

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.selected_field_names is not None:
            result['SelectedFieldNames'] = self.selected_field_names

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldSelectionEnabled') is not None:
            self.field_selection_enabled = m.get('FieldSelectionEnabled')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SelectedFieldNames') is not None:
            self.selected_field_names = m.get('SelectedFieldNames')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

