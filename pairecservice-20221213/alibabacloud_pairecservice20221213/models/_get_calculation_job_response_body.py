# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCalculationJobResponseBody(DaraModel):
    def __init__(
        self,
        abmetric_id: str = None,
        abmetric_name: str = None,
        biz_date: str = None,
        config: str = None,
        gmt_ran_time: str = None,
        job_message: List[str] = None,
        job_source: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the AB metric.
        self.abmetric_id = abmetric_id
        # The name of the AB metric.
        self.abmetric_name = abmetric_name
        # The business date.
        self.biz_date = biz_date
        # The job configuration.
        self.config = config
        # The runtime of the job.
        self.gmt_ran_time = gmt_ran_time
        # The job messages.
        self.job_message = job_message
        # The job source. Valid values:
        # 
        # - CronOffline: An offline cron job.
        # 
        # - DataRerun: A data rerun task.
        self.job_source = job_source
        # The request ID.
        self.request_id = request_id
        # The status of the calculation job. Valid values:
        # 
        # - Success: The job completed successfully.
        # 
        # - Failure: The job failed.
        # 
        # - Initializing: The job is initializing.
        # 
        # - Running: The job is running.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abmetric_id is not None:
            result['ABMetricId'] = self.abmetric_id

        if self.abmetric_name is not None:
            result['ABMetricName'] = self.abmetric_name

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.config is not None:
            result['Config'] = self.config

        if self.gmt_ran_time is not None:
            result['GmtRanTime'] = self.gmt_ran_time

        if self.job_message is not None:
            result['JobMessage'] = self.job_message

        if self.job_source is not None:
            result['JobSource'] = self.job_source

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricId') is not None:
            self.abmetric_id = m.get('ABMetricId')

        if m.get('ABMetricName') is not None:
            self.abmetric_name = m.get('ABMetricName')

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('GmtRanTime') is not None:
            self.gmt_ran_time = m.get('GmtRanTime')

        if m.get('JobMessage') is not None:
            self.job_message = m.get('JobMessage')

        if m.get('JobSource') is not None:
            self.job_source = m.get('JobSource')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

