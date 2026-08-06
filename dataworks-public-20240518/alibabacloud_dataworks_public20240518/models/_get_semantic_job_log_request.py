# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSemanticJobLogRequest(DaraModel):
    def __init__(
        self,
        executor_job_id: str = None,
        project_id: int = None,
    ):
        # The executor job ID. Use the Data.ExecutorJobId from the RunSemanticJob response or the ExecutorJobId from a ListSemanticJobRuns record.
        # 
        # This parameter is required.
        self.executor_job_id = executor_job_id
        # The ID of the DataWorks workspace to which the task belongs. Use the ProjectId from the CreateSemanticJob response or a ListSemanticJobs list item.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_job_id is not None:
            result['ExecutorJobId'] = self.executor_job_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorJobId') is not None:
            self.executor_job_id = m.get('ExecutorJobId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

