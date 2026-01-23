# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChartRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        summary: str = None,
    ):
        # The return value.
        self.code = code
        # The time when the chart repository was created.
        self.create_time = create_time
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the chart repository was last modified.
        self.modified_time = modified_time
        # The ID of the chart repository.
        self.repo_id = repo_id
        # The name of the chart repository.
        self.repo_name = repo_name
        # The name of the namespace to which the chart repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the chart repository. Valid values:
        # 
        # *   `NORMAL`: The repository is normal.
        # *   `DELETING`: The repository is being deleted.
        self.repo_status = repo_status
        # The type of the chart repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.repo_type = repo_type
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The summary about the chart repository.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

