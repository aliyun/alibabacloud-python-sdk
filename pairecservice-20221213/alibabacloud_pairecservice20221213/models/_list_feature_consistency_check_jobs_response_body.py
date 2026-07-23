# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobsResponseBody(DaraModel):
    def __init__(
        self,
        feature_consistency_check_jobs: List[main_models.ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of feature consistency check jobs.
        self.feature_consistency_check_jobs = feature_consistency_check_jobs
        # The request ID.
        self.request_id = request_id
        # The total number of jobs.
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_jobs:
            for v1 in self.feature_consistency_check_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureConsistencyCheckJobs'] = []
        if self.feature_consistency_check_jobs is not None:
            for k1 in self.feature_consistency_check_jobs:
                result['FeatureConsistencyCheckJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_jobs = []
        if m.get('FeatureConsistencyCheckJobs') is not None:
            for k1 in m.get('FeatureConsistencyCheckJobs'):
                temp_model = main_models.ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs()
                self.feature_consistency_check_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs(DaraModel):
    def __init__(
        self,
        config: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_consistency_check_job_config_name: str = None,
        feature_consistency_check_job_id: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        logs: List[str] = None,
        status: str = None,
    ):
        # The configuration of the job.
        self.config = config
        # The ID of the feature consistency check configuration.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # The name of the feature consistency check job configuration.
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name
        # The ID of the feature consistency check job.
        self.feature_consistency_check_job_id = feature_consistency_check_job_id
        # The end time of the job.
        self.gmt_end_time = gmt_end_time
        # The start time of the job.
        self.gmt_start_time = gmt_start_time
        # A list of log entries.
        self.logs = logs
        # The status of the job. Valid values:
        # 
        # - `ToRun`: Waiting to run.
        # 
        # - `Running`: In progress.
        # 
        # - `Success`: Successful.
        # 
        # - `Failure`: Failed.
        # 
        # - `Stopped`: Stopped or canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id

        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name

        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')

        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')

        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

