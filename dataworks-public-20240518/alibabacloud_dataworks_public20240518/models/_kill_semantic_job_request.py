# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KillSemanticJobRequest(DaraModel):
    def __init__(
        self,
        executor_job_id: str = None,
        project_id: int = None,
        retry_times: int = None,
    ):
        # The executor job ID of the run to stop. Use the Data.ExecutorJobId value from the RunSemanticJob response or the ExecutorJobId value from a ListSemanticJobRuns record.
        # 
        # This parameter is required.
        self.executor_job_id = executor_job_id
        # The ID of the DataWorks workspace to which the job belongs. Use the ProjectId value from the CreateSemanticJob response or a ListSemanticJobs list item.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The number of retries when sending the stop request to the executor. This parameter is optional. If specified, use a non-negative integer. After the call, confirm the final status by calling GetSemanticJobDetail.
        self.retry_times = retry_times

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

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorJobId') is not None:
            self.executor_job_id = m.get('ExecutorJobId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        return self

