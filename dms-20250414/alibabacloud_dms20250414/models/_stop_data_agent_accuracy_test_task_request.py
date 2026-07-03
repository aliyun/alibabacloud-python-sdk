# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopDataAgentAccuracyTestTaskRequest(DaraModel):
    def __init__(
        self,
        accuracy_test_task_id: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The ID of the accuracy test task.
        self.accuracy_test_task_id = accuracy_test_task_id
        # The region ID.
        self.region_id = region_id
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test_task_id is not None:
            result['AccuracyTestTaskId'] = self.accuracy_test_task_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestTaskId') is not None:
            self.accuracy_test_task_id = m.get('AccuracyTestTaskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

