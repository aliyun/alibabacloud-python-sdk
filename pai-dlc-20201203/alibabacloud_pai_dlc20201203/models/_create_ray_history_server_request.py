# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRayHistoryServerRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        display_name: str = None,
        ecs_spec: str = None,
        max_runtime_minutes: int = None,
        resource_id: str = None,
        storage_path: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # This parameter is required.
        self.display_name = display_name
        self.ecs_spec = ecs_spec
        self.max_runtime_minutes = max_runtime_minutes
        self.resource_id = resource_id
        # This parameter is required.
        self.storage_path = storage_path
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.max_runtime_minutes is not None:
            result['MaxRuntimeMinutes'] = self.max_runtime_minutes

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('MaxRuntimeMinutes') is not None:
            self.max_runtime_minutes = m.get('MaxRuntimeMinutes')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

