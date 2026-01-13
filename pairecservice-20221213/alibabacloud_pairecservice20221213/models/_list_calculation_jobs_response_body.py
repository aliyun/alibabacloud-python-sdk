# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListCalculationJobsResponseBody(DaraModel):
    def __init__(
        self,
        calculation_jobs: List[main_models.ListCalculationJobsResponseBodyCalculationJobs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.calculation_jobs = calculation_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.calculation_jobs:
            for v1 in self.calculation_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CalculationJobs'] = []
        if self.calculation_jobs is not None:
            for k1 in self.calculation_jobs:
                result['CalculationJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calculation_jobs = []
        if m.get('CalculationJobs') is not None:
            for k1 in m.get('CalculationJobs'):
                temp_model = main_models.ListCalculationJobsResponseBodyCalculationJobs()
                self.calculation_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCalculationJobsResponseBodyCalculationJobs(DaraModel):
    def __init__(
        self,
        abmetric_name: str = None,
        biz_date: str = None,
        calculation_job_id: str = None,
        config: str = None,
        gmt_ran_time: str = None,
        job_message: List[str] = None,
        job_source: str = None,
        status: str = None,
    ):
        self.abmetric_name = abmetric_name
        self.biz_date = biz_date
        self.calculation_job_id = calculation_job_id
        self.config = config
        self.gmt_ran_time = gmt_ran_time
        self.job_message = job_message
        self.job_source = job_source
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abmetric_name is not None:
            result['ABMetricName'] = self.abmetric_name

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.calculation_job_id is not None:
            result['CalculationJobId'] = self.calculation_job_id

        if self.config is not None:
            result['Config'] = self.config

        if self.gmt_ran_time is not None:
            result['GmtRanTime'] = self.gmt_ran_time

        if self.job_message is not None:
            result['JobMessage'] = self.job_message

        if self.job_source is not None:
            result['JobSource'] = self.job_source

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricName') is not None:
            self.abmetric_name = m.get('ABMetricName')

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('CalculationJobId') is not None:
            self.calculation_job_id = m.get('CalculationJobId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('GmtRanTime') is not None:
            self.gmt_ran_time = m.get('GmtRanTime')

        if m.get('JobMessage') is not None:
            self.job_message = m.get('JobMessage')

        if m.get('JobSource') is not None:
            self.job_source = m.get('JobSource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

