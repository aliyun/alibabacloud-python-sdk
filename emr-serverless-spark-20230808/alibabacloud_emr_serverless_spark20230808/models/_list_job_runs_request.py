# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListJobRunsRequest(DaraModel):
    def __init__(
        self,
        application_configs: str = None,
        creator: str = None,
        end_time: main_models.ListJobRunsRequestEndTime = None,
        is_workflow: str = None,
        job_run_deployment_id: str = None,
        job_run_id: str = None,
        max_results: int = None,
        min_duration: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_queue_id: str = None,
        runtime_configs: str = None,
        start_time: main_models.ListJobRunsRequestStartTime = None,
        states: List[str] = None,
        tags: List[main_models.ListJobRunsRequestTags] = None,
    ):
        self.application_configs = application_configs
        # The ID of the user who created the job.
        self.creator = creator
        # The range of end time.
        self.end_time = end_time
        self.is_workflow = is_workflow
        # The job run ID.
        self.job_run_deployment_id = job_run_deployment_id
        # The job ID.
        self.job_run_id = job_run_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The minimum running duration of the job. Unit: ms.
        self.min_duration = min_duration
        # The job name.
        self.name = name
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The name of the resource queue on which the Spark jobs run.
        self.resource_queue_id = resource_queue_id
        self.runtime_configs = runtime_configs
        # The range of start time.
        self.start_time = start_time
        # The job states.
        self.states = states
        # The tags of the job.
        self.tags = tags

    def validate(self):
        if self.end_time:
            self.end_time.validate()
        if self.start_time:
            self.start_time.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_configs is not None:
            result['applicationConfigs'] = self.application_configs

        if self.creator is not None:
            result['creator'] = self.creator

        if self.end_time is not None:
            result['endTime'] = self.end_time.to_map()

        if self.is_workflow is not None:
            result['isWorkflow'] = self.is_workflow

        if self.job_run_deployment_id is not None:
            result['jobRunDeploymentId'] = self.job_run_deployment_id

        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.min_duration is not None:
            result['minDuration'] = self.min_duration

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        if self.runtime_configs is not None:
            result['runtimeConfigs'] = self.runtime_configs

        if self.start_time is not None:
            result['startTime'] = self.start_time.to_map()

        if self.states is not None:
            result['states'] = self.states

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfigs') is not None:
            self.application_configs = m.get('applicationConfigs')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('endTime') is not None:
            temp_model = main_models.ListJobRunsRequestEndTime()
            self.end_time = temp_model.from_map(m.get('endTime'))

        if m.get('isWorkflow') is not None:
            self.is_workflow = m.get('isWorkflow')

        if m.get('jobRunDeploymentId') is not None:
            self.job_run_deployment_id = m.get('jobRunDeploymentId')

        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        if m.get('runtimeConfigs') is not None:
            self.runtime_configs = m.get('runtimeConfigs')

        if m.get('startTime') is not None:
            temp_model = main_models.ListJobRunsRequestStartTime()
            self.start_time = temp_model.from_map(m.get('startTime'))

        if m.get('states') is not None:
            self.states = m.get('states')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListJobRunsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListJobRunsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListJobRunsRequestStartTime(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the start time range.
        self.end_time = end_time
        # The beginning of the start time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class ListJobRunsRequestEndTime(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the end time range.
        self.end_time = end_time
        # The beginning of the end time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

