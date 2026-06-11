# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListRayJobResponseBody(DaraModel):
    def __init__(
        self,
        ray_jobs: List[main_models.ListRayJobResponseBodyRayJobs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ray_jobs = ray_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ray_jobs:
            for v1 in self.ray_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['rayJobs'] = []
        if self.ray_jobs is not None:
            for k1 in self.ray_jobs:
                result['rayJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ray_jobs = []
        if m.get('rayJobs') is not None:
            for k1 in m.get('rayJobs'):
                temp_model = main_models.ListRayJobResponseBodyRayJobs()
                self.ray_jobs.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListRayJobResponseBodyRayJobs(DaraModel):
    def __init__(
        self,
        cluster_state: str = None,
        creator_name: str = None,
        cu_hours: float = None,
        dashboard_url: str = None,
        duration: int = None,
        end_time: int = None,
        name: str = None,
        resource_queue: str = None,
        start_time: int = None,
        status: str = None,
        submission_id: str = None,
        submit_time: int = None,
    ):
        self.cluster_state = cluster_state
        self.creator_name = creator_name
        self.cu_hours = cu_hours
        self.dashboard_url = dashboard_url
        self.duration = duration
        self.end_time = end_time
        self.name = name
        self.resource_queue = resource_queue
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_state is not None:
            result['clusterState'] = self.cluster_state

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        if self.dashboard_url is not None:
            result['dashboardUrl'] = self.dashboard_url

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.name is not None:
            result['name'] = self.name

        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.submission_id is not None:
            result['submissionId'] = self.submission_id

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterState') is not None:
            self.cluster_state = m.get('clusterState')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        if m.get('dashboardUrl') is not None:
            self.dashboard_url = m.get('dashboardUrl')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submissionId') is not None:
            self.submission_id = m.get('submissionId')

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        return self

