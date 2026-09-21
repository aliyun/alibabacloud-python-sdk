# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeScheduledTaskExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        executions: List[main_models.DescribeScheduledTaskExecutionsResponseBodyExecutions] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The status code of the operation.
        self.code = code
        # The list of task execution records.
        self.executions = executions
        # The maximum number of results returned in this request.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of results returned.
        self.total_count = total_count

    def validate(self):
        if self.executions:
            for v1 in self.executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Executions'] = []
        if self.executions is not None:
            for k1 in self.executions:
                result['Executions'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.executions = []
        if m.get('Executions') is not None:
            for k1 in m.get('Executions'):
                temp_model = main_models.DescribeScheduledTaskExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScheduledTaskExecutionsResponseBodyExecutions(DaraModel):
    def __init__(
        self,
        artifact_count: int = None,
        artifacts: List[main_models.DescribeScheduledTaskExecutionsResponseBodyExecutionsArtifacts] = None,
        completed_at: str = None,
        config_snapshot: str = None,
        duration_ms: int = None,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
        output: str = None,
        scheduled_id: str = None,
        started_at: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The number of task artifacts.
        self.artifact_count = artifact_count
        # The list of uploaded task artifacts.
        self.artifacts = artifacts
        # The end time.
        self.completed_at = completed_at
        # The configuration snapshot in JSON format.
        self.config_snapshot = config_snapshot
        # The execution duration in milliseconds.
        self.duration_ms = duration_ms
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The instance ID.
        self.instance_id = instance_id
        # The execution output in JSON format.
        self.output = output
        # The ID of the scheduled task.
        self.scheduled_id = scheduled_id
        # The start time.
        self.started_at = started_at
        # The execution status.
        self.status = status
        # The ID of the scheduled task execution record.
        self.task_id = task_id

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_count is not None:
            result['ArtifactCount'] = self.artifact_count

        result['Artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['Artifacts'].append(k1.to_map() if k1 else None)

        if self.completed_at is not None:
            result['CompletedAt'] = self.completed_at

        if self.config_snapshot is not None:
            result['ConfigSnapshot'] = self.config_snapshot

        if self.duration_ms is not None:
            result['DurationMs'] = self.duration_ms

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.output is not None:
            result['Output'] = self.output

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.started_at is not None:
            result['StartedAt'] = self.started_at

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactCount') is not None:
            self.artifact_count = m.get('ArtifactCount')

        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k1 in m.get('Artifacts'):
                temp_model = main_models.DescribeScheduledTaskExecutionsResponseBodyExecutionsArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('CompletedAt') is not None:
            self.completed_at = m.get('CompletedAt')

        if m.get('ConfigSnapshot') is not None:
            self.config_snapshot = m.get('ConfigSnapshot')

        if m.get('DurationMs') is not None:
            self.duration_ms = m.get('DurationMs')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeScheduledTaskExecutionsResponseBodyExecutionsArtifacts(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        download_url: str = None,
        name: str = None,
        size: int = None,
        updated_time: str = None,
    ):
        # The MIME type.
        self.content_type = content_type
        # The OSS pre-signed download URL.
        self.download_url = download_url
        # The file name.
        self.name = name
        # The file size in bytes.
        self.size = size
        # The upload time in ISO 8601 format.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

