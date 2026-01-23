# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetArtifactSubscriptionTaskResponseBody(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        code: str = None,
        end_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        message: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        request_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        source_repo_type: str = None,
        start_time: int = None,
        tag_subscription_count: int = None,
        tag_total_count: int = None,
        task_id: str = None,
        task_result: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The return value.
        self.code = code
        # The end time of the artifact subscription task.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The return message.
        self.message = message
        # The name of the Container Registry namespace.
        self.namespace_name = namespace_name
        # The name of the Container Registry repository.
        self.repo_name = repo_name
        # The request ID.
        self.request_id = request_id
        # The name of the source namespace.
        self.source_namespace_name = source_namespace_name
        # The artifact source.
        self.source_provider = source_provider
        # The name of the source repository.
        self.source_repo_name = source_repo_name
        # The type of the source repository.
        self.source_repo_type = source_repo_type
        # The start time of the artifact subscription task.
        self.start_time = start_time
        # The total subscribed tags.
        self.tag_subscription_count = tag_subscription_count
        # The total number of tags.
        self.tag_total_count = tag_total_count
        # The task ID.
        self.task_id = task_id
        # The task results.
        self.task_result = task_result
        # The status of the task.
        self.task_status = task_status
        # The type of the task. Valid values:
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name

        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider

        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name

        if self.source_repo_type is not None:
            result['SourceRepoType'] = self.source_repo_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag_subscription_count is not None:
            result['TagSubscriptionCount'] = self.tag_subscription_count

        if self.tag_total_count is not None:
            result['TagTotalCount'] = self.tag_total_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')

        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')

        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')

        if m.get('SourceRepoType') is not None:
            self.source_repo_type = m.get('SourceRepoType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagSubscriptionCount') is not None:
            self.tag_subscription_count = m.get('TagSubscriptionCount')

        if m.get('TagTotalCount') is not None:
            self.tag_total_count = m.get('TagTotalCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

