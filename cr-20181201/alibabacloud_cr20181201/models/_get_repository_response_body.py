# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        detail: str = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        repo_build_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        # The return value.
        self.code = code
        # The time when the repository was created.
        self.create_time = create_time
        # The details of the repository.
        self.detail = detail
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The time when the repository was last modified.
        self.modified_time = modified_time
        # Indicates how the repository was created. Valid values:
        # 
        # *   `MANUAL`: The repository was manually created.
        # *   `AUTO`: The repository was automatically created.
        self.repo_build_type = repo_build_type
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name
        # The status of the repository.
        self.repo_status = repo_status
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: public repository.
        # *   `PRIVATE`: private repository.
        self.repo_type = repo_type
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The summary of the repository.
        self.summary = summary
        # Indicates whether the feature of image tag immutability is enabled. Valid values:
        # 
        # *   `true`: The feature of image tag immutability is enabled.
        # *   `false`: The feature of image tag immutability is disabled.
        self.tag_immutability = tag_immutability

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

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type

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

        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')

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

        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')

        return self

