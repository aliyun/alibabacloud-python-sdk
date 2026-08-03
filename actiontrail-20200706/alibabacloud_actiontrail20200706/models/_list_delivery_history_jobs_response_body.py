# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class ListDeliveryHistoryJobsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_history_jobs: List[main_models.ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of data backfill tasks.
        self.delivery_history_jobs = delivery_history_jobs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.delivery_history_jobs:
            for v1 in self.delivery_history_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeliveryHistoryJobs'] = []
        if self.delivery_history_jobs is not None:
            for k1 in self.delivery_history_jobs:
                result['DeliveryHistoryJobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_history_jobs = []
        if m.get('DeliveryHistoryJobs') is not None:
            for k1 in m.get('DeliveryHistoryJobs'):
                temp_model = main_models.ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs()
                self.delivery_history_jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDeliveryHistoryJobsResponseBodyDeliveryHistoryJobs(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: str = None,
        home_region: str = None,
        job_id: int = None,
        job_status: int = None,
        start_time: str = None,
        trail_name: str = None,
        updated_time: str = None,
    ):
        # The time when the task was created.
        self.created_time = created_time
        # The time when the task ended.
        self.end_time = end_time
        # The home region.
        self.home_region = home_region
        # The task ID.
        self.job_id = job_id
        # The status of the task. Valid values:
        # 
        # - 0: The task is being initialized.
        # 
        # - 1: The task is delivering events.
        # 
        # - 2: The task is complete.
        # 
        # - 3: The task failed.
        self.job_status = job_status
        # The time when the task started.
        self.start_time = start_time
        # The name of the trail.
        self.trail_name = trail_name
        # The time when the task was last updated.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.home_region is not None:
            result['HomeRegion'] = self.home_region

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

