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
        # The return code.
        self.code = code
        # The creation time, represented as a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The detailed information.
        self.detail = detail
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the request was successful.
        self.is_success = is_success
        # The last modification time, represented as a UNIX timestamp in milliseconds.
        self.modified_time = modified_time
        # The repository build type. Valid values:
        # 
        # - `MANUAL`: manually triggered build.
        # 
        # - `AUTO`: automatically triggered build.
        self.repo_build_type = repo_build_type
        # The repository ID.
        self.repo_id = repo_id
        # The repository name.
        self.repo_name = repo_name
        # The namespace name.
        self.repo_namespace_name = repo_namespace_name
        # The repository status.
        self.repo_status = repo_status
        # The repository type. Valid values:
        # 
        # - `PUBLIC`: public repository.
        # 
        # - `PRIVATE`: private repository.
        self.repo_type = repo_type
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The summary information.
        self.summary = summary
        # The image tag immutability setting. Valid values:
        # 
        # - `true`: Enabled.
        # 
        # - `false`: Disabled.
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

