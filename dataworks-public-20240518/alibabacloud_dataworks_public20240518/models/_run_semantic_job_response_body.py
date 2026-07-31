# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class RunSemanticJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.RunSemanticJobResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The run information for this submission. A successful submission does not mean that the semantic model output has been generated. Use the detail operation to confirm the status before downloading results.
        self.data = data
        # The request ID. Used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.RunSemanticJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RunSemanticJobResponseBodyData(DaraModel):
    def __init__(
        self,
        current_sql_index: int = None,
        env: str = None,
        exec_types: List[int] = None,
        executor_job_id: str = None,
        job_run_id: str = None,
        statuses: List[int] = None,
    ):
        # The current SQL fragment index returned by the executor in the submission response.
        self.current_sql_index = current_sql_index
        # The runtime environment identifier returned by the executor in the submission response.
        self.env = env
        # The list of execution type codes returned by the executor in the submission response.
        self.exec_types = exec_types
        # The executor job identifier. Pass this value to the ExecutorJobId parameter of GetSemanticJobDetail, GetSemanticJobLog, or KillSemanticJob.
        self.executor_job_id = executor_job_id
        # The unique identifier of this run. Pass this value to the JobRunId parameter of DownloadSemanticResults to obtain the output of this run.
        self.job_run_id = job_run_id
        # The list of status codes returned by the executor in the submission response. The status at the submission stage does not indicate that the results are complete.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_sql_index is not None:
            result['CurrentSqlIndex'] = self.current_sql_index

        if self.env is not None:
            result['Env'] = self.env

        if self.exec_types is not None:
            result['ExecTypes'] = self.exec_types

        if self.executor_job_id is not None:
            result['ExecutorJobId'] = self.executor_job_id

        if self.job_run_id is not None:
            result['JobRunId'] = self.job_run_id

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentSqlIndex') is not None:
            self.current_sql_index = m.get('CurrentSqlIndex')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExecTypes') is not None:
            self.exec_types = m.get('ExecTypes')

        if m.get('ExecutorJobId') is not None:
            self.executor_job_id = m.get('ExecutorJobId')

        if m.get('JobRunId') is not None:
            self.job_run_id = m.get('JobRunId')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

