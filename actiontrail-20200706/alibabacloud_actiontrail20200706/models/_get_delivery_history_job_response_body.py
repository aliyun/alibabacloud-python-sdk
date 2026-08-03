# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetDeliveryHistoryJobResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: str = None,
        home_region: str = None,
        job_id: int = None,
        job_status: int = None,
        request_id: str = None,
        start_time: str = None,
        status: List[main_models.GetDeliveryHistoryJobResponseBodyStatus] = None,
        trail_name: str = None,
        updated_time: str = None,
    ):
        # The time when the task was created.
        self.created_time = created_time
        # The time when the task ended.
        self.end_time = end_time
        # The home region of the trail.
        self.home_region = home_region
        # The ID of the task.
        self.job_id = job_id
        # The task status. Valid values:
        # 
        # - 0: The task is initializing.
        # 
        # - 1: The task is delivering historical events.
        # 
        # - 2: The task is complete.
        # 
        # - 3: The task fails.
        self.job_status = job_status
        # The ID of the request.
        self.request_id = request_id
        # The time when the task started.
        self.start_time = start_time
        # A list of task statuses in each region.
        self.status = status
        # The name of the trail based on which the task delivers events.
        self.trail_name = trail_name
        # The time when the task was updated.
        self.updated_time = updated_time

    def validate(self):
        if self.status:
            for v1 in self.status:
                 if v1:
                    v1.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Status'] = []
        if self.status is not None:
            for k1 in self.status:
                result['Status'].append(k1.to_map() if k1 else None)

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.status = []
        if m.get('Status') is not None:
            for k1 in m.get('Status'):
                temp_model = main_models.GetDeliveryHistoryJobResponseBodyStatus()
                self.status.append(temp_model.from_map(k1))

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class GetDeliveryHistoryJobResponseBodyStatus(DaraModel):
    def __init__(
        self,
        region: str = None,
        status: int = None,
    ):
        # The ID of the region.
        self.region = region
        # The task status in each region. Valid values:
        # 
        # - 0: The task is initializing.
        # 
        # - 1: The task is delivering historical events.
        # 
        # - 2: The task is complete.
        # 
        # - 3: The task fails.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

