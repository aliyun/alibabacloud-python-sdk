# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListDataDiagnosisJobsResponseBody(DaraModel):
    def __init__(
        self,
        data_diagnosis_jobs: List[main_models.ListDataDiagnosisJobsResponseBodyDataDiagnosisJobs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_diagnosis_jobs = data_diagnosis_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_diagnosis_jobs:
            for v1 in self.data_diagnosis_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDiagnosisJobs'] = []
        if self.data_diagnosis_jobs is not None:
            for k1 in self.data_diagnosis_jobs:
                result['DataDiagnosisJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_diagnosis_jobs = []
        if m.get('DataDiagnosisJobs') is not None:
            for k1 in m.get('DataDiagnosisJobs'):
                temp_model = main_models.ListDataDiagnosisJobsResponseBodyDataDiagnosisJobs()
                self.data_diagnosis_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataDiagnosisJobsResponseBodyDataDiagnosisJobs(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        config: str = None,
        data_diagnosis_config_id: str = None,
        data_diagnosis_config_name: str = None,
        data_diagnosis_job_id: str = None,
        gmt_create_time: str = None,
        gmt_start_time: str = None,
        job_source: str = None,
        logs: List[str] = None,
        status: str = None,
        type: str = None,
    ):
        self.biz_date = biz_date
        self.config = config
        self.data_diagnosis_config_id = data_diagnosis_config_id
        self.data_diagnosis_config_name = data_diagnosis_config_name
        self.data_diagnosis_job_id = data_diagnosis_job_id
        self.gmt_create_time = gmt_create_time
        self.gmt_start_time = gmt_start_time
        self.job_source = job_source
        self.logs = logs
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.config is not None:
            result['Config'] = self.config

        if self.data_diagnosis_config_id is not None:
            result['DataDiagnosisConfigId'] = self.data_diagnosis_config_id

        if self.data_diagnosis_config_name is not None:
            result['DataDiagnosisConfigName'] = self.data_diagnosis_config_name

        if self.data_diagnosis_job_id is not None:
            result['DataDiagnosisJobId'] = self.data_diagnosis_job_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.job_source is not None:
            result['JobSource'] = self.job_source

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DataDiagnosisConfigId') is not None:
            self.data_diagnosis_config_id = m.get('DataDiagnosisConfigId')

        if m.get('DataDiagnosisConfigName') is not None:
            self.data_diagnosis_config_name = m.get('DataDiagnosisConfigName')

        if m.get('DataDiagnosisJobId') is not None:
            self.data_diagnosis_job_id = m.get('DataDiagnosisJobId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('JobSource') is not None:
            self.job_source = m.get('JobSource')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

