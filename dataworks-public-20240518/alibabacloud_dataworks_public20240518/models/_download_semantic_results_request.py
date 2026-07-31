# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadSemanticResultsRequest(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        job_run_id: str = None,
    ):
        # The node name. Use the Data.Name value from the CreateSemanticJob response, the Name value from a ListSemanticJobs list item, or the JobName value from a ListSemanticJobRuns record.
        # 
        # This parameter is required.
        self.job_name = job_name
        # The optional run ID. If you specify the Data.JobRunId value from the RunSemanticJob response or the JobRunId value from a ListSemanticJobRuns record, only the artifacts of that specific run are returned. If you do not specify this parameter, the artifacts of the latest run of the node are returned.
        self.job_run_id = job_run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_run_id is not None:
            result['JobRunId'] = self.job_run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobRunId') is not None:
            self.job_run_id = m.get('JobRunId')

        return self

