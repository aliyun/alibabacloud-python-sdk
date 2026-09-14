# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AbolishCrossProjectPipelineRunRequest(DaraModel):
    def __init__(
        self,
        pipeline_run_id: str = None,
        project_id: int = None,
        reason: str = None,
    ):
        # The ID of the cross-workspace publish flow.
        # 
        # This parameter is required.
        self.pipeline_run_id = pipeline_run_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The reason for stopping the cross-workspace publish flow.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

