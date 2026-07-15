# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTensorboardRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        max_running_time_minutes: int = None,
        priority: str = None,
        workspace_id: str = None,
    ):
        # Visibility of the task. Valid values:
        # 
        # - PUBLIC: Visible to all users in this workspace.
        # 
        # - PRIVATE: Visible only to you and administrators in this workspace.
        self.accessibility = accessibility
        # Maximum runtime. Unit: minutes.
        self.max_running_time_minutes = max_running_time_minutes
        self.priority = priority
        # Workspace ID. For more information about how to get a workspace ID, see [ListWorkspaces]().
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

        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

