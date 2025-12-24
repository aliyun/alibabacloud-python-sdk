# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class CreateServiceCronScalerRequest(DaraModel):
    def __init__(
        self,
        exclude_dates: List[str] = None,
        scale_jobs: List[main_models.CreateServiceCronScalerRequestScaleJobs] = None,
    ):
        # The points in time that are excluded when you schedule a CronHPA job. The points in time must be specified by using a cron expression.
        self.exclude_dates = exclude_dates
        # The description of the CronHPA job.
        # 
        # This parameter is required.
        self.scale_jobs = scale_jobs

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

        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k1 in self.scale_jobs:
                result['ScaleJobs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')

        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k1 in m.get('ScaleJobs'):
                temp_model = main_models.CreateServiceCronScalerRequestScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k1))

        return self

class CreateServiceCronScalerRequestScaleJobs(DaraModel):
    def __init__(
        self,
        name: str = None,
        schedule: str = None,
        target_size: int = None,
        time_zone: str = None,
    ):
        # The name of the CronHPA job.
        self.name = name
        # The cron expression that is used to configure the execution time of the CronHPA job. For more information about how to configure cron expressions, see **Description of special characters** in this topic.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The number of instances that you want to configure for the CronHPA job.
        # 
        # This parameter is required.
        self.target_size = target_size
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.target_size is not None:
            result['TargetSize'] = self.target_size

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

