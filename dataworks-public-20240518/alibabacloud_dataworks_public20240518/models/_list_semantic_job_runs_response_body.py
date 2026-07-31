# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListSemanticJobRunsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSemanticJobRunsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The paginated run record results. Use the JobRunId to download the results of a specific run, and use the ExecutorJobId to query details, logs, or stop a run.
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
            temp_model = main_models.ListSemanticJobRunsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSemanticJobRunsResponseBodyData(DaraModel):
    def __init__(
        self,
        job_runs: List[main_models.ListSemanticJobRunsResponseBodyDataJobRuns] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of run records.
        self.job_runs = job_runs
        # The page number returned, starting from 1.
        self.page_number = page_number
        # The number of records per page returned.
        self.page_size = page_size
        # The total number of run records that match the current job criteria.
        self.total_count = total_count

    def validate(self):
        if self.job_runs:
            for v1 in self.job_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobRuns'] = []
        if self.job_runs is not None:
            for k1 in self.job_runs:
                result['JobRuns'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_runs = []
        if m.get('JobRuns') is not None:
            for k1 in m.get('JobRuns'):
                temp_model = main_models.ListSemanticJobRunsResponseBodyDataJobRuns()
                self.job_runs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSemanticJobRunsResponseBodyDataJobRuns(DaraModel):
    def __init__(
        self,
        executor_job_id: str = None,
        gmt_create: int = None,
        job_name: str = None,
        job_run_id: str = None,
        user_id: str = None,
    ):
        # The executor job ID. Pass this value to the ExecutorJobId parameter of GetSemanticJobDetail, GetSemanticJobLog, or KillSemanticJob.
        self.executor_job_id = executor_job_id
        # The time when the run record was created. The value is a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The name of the job to which this run belongs. This value can be used to re-run the job, query run records, or download results.
        self.job_name = job_name
        # The semantic job run ID. Pass this value to the JobRunId parameter of DownloadSemanticResults to download the results of this run.
        self.job_run_id = job_run_id
        # The ID of the user who submitted this run.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_job_id is not None:
            result['ExecutorJobId'] = self.executor_job_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_run_id is not None:
            result['JobRunId'] = self.job_run_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorJobId') is not None:
            self.executor_job_id = m.get('ExecutorJobId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobRunId') is not None:
            self.job_run_id = m.get('JobRunId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

