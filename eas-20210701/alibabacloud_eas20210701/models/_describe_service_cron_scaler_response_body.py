# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceCronScalerResponseBody(DaraModel):
    def __init__(
        self,
        exclude_dates: List[str] = None,
        request_id: str = None,
        scale_jobs: List[main_models.DescribeServiceCronScalerResponseBodyScaleJobs] = None,
        service_name: str = None,
    ):
        # The points in time that are excluded when you schedule a CronHPA job. The points in time must be specified by using a cron expression.
        self.exclude_dates = exclude_dates
        # The request ID.
        self.request_id = request_id
        # The CronHPA jobs.
        self.scale_jobs = scale_jobs
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.scale_jobs:
            for v1 in self.scale_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k1 in self.scale_jobs:
                result['ScaleJobs'].append(k1.to_map() if k1 else None)

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k1 in m.get('ScaleJobs'):
                temp_model = main_models.DescribeServiceCronScalerResponseBodyScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k1))

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeServiceCronScalerResponseBodyScaleJobs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        last_probe_time: str = None,
        message: str = None,
        name: str = None,
        schedule: str = None,
        state: str = None,
        target_size: int = None,
    ):
        # The time when the most recent CronHPA job was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the most recent CronHPA job ran. The time is displayed in UTC.
        self.last_probe_time = last_probe_time
        # The returned message.
        self.message = message
        # The name of the CronHPA job.
        self.name = name
        # The cron expression that is used to configure the execution time of the CronHPA job.
        self.schedule = schedule
        # The status of the most recent CronHPA job.
        self.state = state
        # The number of instances that you expect to configure for the CronHPA job.
        self.target_size = target_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_probe_time is not None:
            result['LastProbeTime'] = self.last_probe_time

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.state is not None:
            result['State'] = self.state

        if self.target_size is not None:
            result['TargetSize'] = self.target_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastProbeTime') is not None:
            self.last_probe_time = m.get('LastProbeTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')

        return self

