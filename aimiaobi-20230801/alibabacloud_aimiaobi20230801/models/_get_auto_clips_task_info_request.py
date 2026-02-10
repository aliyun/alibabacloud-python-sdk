# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutoClipsTaskInfoRequest(DaraModel):
    def __init__(
        self,
        show_analysis_results: bool = None,
        show_resource_info: bool = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.show_analysis_results = show_analysis_results
        self.show_resource_info = show_resource_info
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_analysis_results is not None:
            result['ShowAnalysisResults'] = self.show_analysis_results

        if self.show_resource_info is not None:
            result['ShowResourceInfo'] = self.show_resource_info

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowAnalysisResults') is not None:
            self.show_analysis_results = m.get('ShowAnalysisResults')

        if m.get('ShowResourceInfo') is not None:
            self.show_resource_info = m.get('ShowResourceInfo')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

