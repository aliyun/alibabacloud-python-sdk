# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListActionPlanActivitiesResponseBody(DaraModel):
    def __init__(
        self,
        action_plan_activities: List[main_models.ListActionPlanActivitiesResponseBodyActionPlanActivities] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of execution details of the execution plan.
        self.action_plan_activities = action_plan_activities
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # Indicates the read position returned by the current call. An empty value means all data has been read.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Total data count under the current request conditions (optional; not returned by default).
        self.total_count = total_count

    def validate(self):
        if self.action_plan_activities:
            for v1 in self.action_plan_activities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionPlanActivities'] = []
        if self.action_plan_activities is not None:
            for k1 in self.action_plan_activities:
                result['ActionPlanActivities'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_plan_activities = []
        if m.get('ActionPlanActivities') is not None:
            for k1 in m.get('ActionPlanActivities'):
                temp_model = main_models.ListActionPlanActivitiesResponseBodyActionPlanActivities()
                self.action_plan_activities.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListActionPlanActivitiesResponseBodyActionPlanActivities(DaraModel):
    def __init__(
        self,
        action_plan_activity_id: str = None,
        created_capacity: float = None,
        destroy_capacity: float = None,
        end_time: str = None,
        jobs: List[main_models.ListActionPlanActivitiesResponseBodyActionPlanActivitiesJobs] = None,
        start_time: str = None,
        status: str = None,
    ):
        # The activity ID of the execution plan.
        self.action_plan_activity_id = action_plan_activity_id
        # The increased capacity of this execution plan activity.
        self.created_capacity = created_capacity
        # The capacity released by this execution plan activity.
        self.destroy_capacity = destroy_capacity
        # The end time of the execution plan activity.
        self.end_time = end_time
        # The list of Instant jobs involved in the execution plan.
        self.jobs = jobs
        # The start time of the implementation of the planned activity.
        self.start_time = start_time
        # The implementation status of the execution plan activity. Valid values:
        # 
        # *   InProcess
        # *   Completed
        # *   Failed
        self.status = status

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_activity_id is not None:
            result['ActionPlanActivityId'] = self.action_plan_activity_id

        if self.created_capacity is not None:
            result['CreatedCapacity'] = self.created_capacity

        if self.destroy_capacity is not None:
            result['DestroyCapacity'] = self.destroy_capacity

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanActivityId') is not None:
            self.action_plan_activity_id = m.get('ActionPlanActivityId')

        if m.get('CreatedCapacity') is not None:
            self.created_capacity = m.get('CreatedCapacity')

        if m.get('DestroyCapacity') is not None:
            self.destroy_capacity = m.get('DestroyCapacity')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListActionPlanActivitiesResponseBodyActionPlanActivitiesJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListActionPlanActivitiesResponseBodyActionPlanActivitiesJobs(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        job_operation_type: str = None,
        region_id: str = None,
    ):
        # The ID of the job.
        self.job_id = job_id
        # The operation type of the execution plan activity on the job. Possible values are as follows:
        # 
        # *   Create
        # *   Delete
        self.job_operation_type = job_operation_type
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_operation_type is not None:
            result['JobOperationType'] = self.job_operation_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobOperationType') is not None:
            self.job_operation_type = m.get('JobOperationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

