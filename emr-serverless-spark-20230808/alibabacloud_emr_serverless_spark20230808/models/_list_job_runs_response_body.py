# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListJobRunsResponseBody(DaraModel):
    def __init__(
        self,
        job_runs: List[main_models.ListJobRunsResponseBodyJobRuns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The Spark jobs.
        self.job_runs = job_runs
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_runs:
            for v1 in self.job_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobRuns'] = []
        if self.job_runs is not None:
            for k1 in self.job_runs:
                result['jobRuns'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_runs = []
        if m.get('jobRuns') is not None:
            for k1 in m.get('jobRuns'):
                temp_model = main_models.ListJobRunsResponseBodyJobRuns()
                self.job_runs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListJobRunsResponseBodyJobRuns(DaraModel):
    def __init__(
        self,
        code_type: str = None,
        configuration_overrides: main_models.ListJobRunsResponseBodyJobRunsConfigurationOverrides = None,
        creator: str = None,
        cu_hours: float = None,
        display_release_version: str = None,
        end_time: int = None,
        execution_timeout_seconds: int = None,
        fusion: bool = None,
        job_driver: main_models.JobDriver = None,
        job_run_id: str = None,
        log: main_models.RunLog = None,
        mb_seconds: int = None,
        name: str = None,
        release_version: str = None,
        resource_queue_id: str = None,
        state: str = None,
        state_change_reason: main_models.ListJobRunsResponseBodyJobRunsStateChangeReason = None,
        submit_time: int = None,
        tags: List[main_models.Tag] = None,
        vcore_seconds: int = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The code type of the job. Valid values:
        # 
        # SQL
        # 
        # JAR
        # 
        # PYTHON
        self.code_type = code_type
        # The advanced configurations of Spark.
        self.configuration_overrides = configuration_overrides
        # The ID of the user who created the job.
        self.creator = creator
        # The number of CUs consumed during a specified cycle of a task. The value is an estimated value. Refer to your Alibaba Cloud bill for the actual number of consumed CUs.
        self.cu_hours = cu_hours
        # The version of Spark on which the jobs run.
        self.display_release_version = display_release_version
        # The end time of the job.
        self.end_time = end_time
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_run_id = job_run_id
        # The path where the operational logs are stored.
        self.log = log
        # The total amount of memory allocated to the job multiplied by the running duration (seconds).
        self.mb_seconds = mb_seconds
        # The job name.
        self.name = name
        # The version of Spark on which the jobs run.
        self.release_version = release_version
        self.resource_queue_id = resource_queue_id
        # The job state.
        self.state = state
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The tags of the job.
        self.tags = tags
        # The total number of CPU cores allocated to the job multiplied by the running duration (seconds).
        self.vcore_seconds = vcore_seconds
        # The web UI of the job.
        self.web_ui = web_ui
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.log:
            self.log.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_type is not None:
            result['codeType'] = self.code_type

        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()

        if self.creator is not None:
            result['creator'] = self.creator

        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()

        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id

        if self.log is not None:
            result['log'] = self.log.to_map()

        if self.mb_seconds is not None:
            result['mbSeconds'] = self.mb_seconds

        if self.name is not None:
            result['name'] = self.name

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        if self.state is not None:
            result['state'] = self.state

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.vcore_seconds is not None:
            result['vcoreSeconds'] = self.vcore_seconds

        if self.web_ui is not None:
            result['webUI'] = self.web_ui

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')

        if m.get('configurationOverrides') is not None:
            temp_model = main_models.ListJobRunsResponseBodyJobRunsConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m.get('configurationOverrides'))

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('jobDriver') is not None:
            temp_model = main_models.JobDriver()
            self.job_driver = temp_model.from_map(m.get('jobDriver'))

        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')

        if m.get('log') is not None:
            temp_model = main_models.RunLog()
            self.log = temp_model.from_map(m.get('log'))

        if m.get('mbSeconds') is not None:
            self.mb_seconds = m.get('mbSeconds')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.ListJobRunsResponseBodyJobRunsStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('vcoreSeconds') is not None:
            self.vcore_seconds = m.get('vcoreSeconds')

        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListJobRunsResponseBodyJobRunsStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListJobRunsResponseBodyJobRunsConfigurationOverrides(DaraModel):
    def __init__(
        self,
        configurations: List[main_models.Configuration] = None,
    ):
        # The SparkConf objects.
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for v1 in self.configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configurations'] = []
        if self.configurations is not None:
            for k1 in self.configurations:
                result['configurations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k1 in m.get('configurations'):
                temp_model = main_models.Configuration()
                self.configurations.append(temp_model.from_map(k1))

        return self

