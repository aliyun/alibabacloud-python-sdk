# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        repositories: List[main_models.ListRepositoryResponseBodyRepositories] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The information about the repositories.
        self.repositories = repositories
        # The request ID.
        self.request_id = request_id
        # The total number of the queried image repositories.
        self.total_count = total_count

    def validate(self):
        if self.repositories:
            for v1 in self.repositories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Repositories'] = []
        if self.repositories is not None:
            for k1 in self.repositories:
                result['Repositories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.repositories = []
        if m.get('Repositories') is not None:
            for k1 in m.get('Repositories'):
                temp_model = main_models.ListRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepositoryResponseBodyRepositories(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        modified_time: int = None,
        repo_build_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        resource_group_id: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        # The time when the repository was created.
        self.create_time = create_time
        # The ID of the Container Registry instance to which the repository belongs.
        self.instance_id = instance_id
        # The time when the repository was last modified.
        self.modified_time = modified_time
        # The type of the repository building. Valid values:
        # 
        # *   `AUTO`: The repository is automatically built.
        # *   `MANUAL`: The repository is manually built.
        self.repo_build_type = repo_build_type
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the repository.
        self.repo_status = repo_status
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`
        # *   `PRIVATE`
        self.repo_type = repo_type
        # The ID of the resource group to which the repository belongs.
        self.resource_group_id = resource_group_id
        # The summary of the repository.
        self.summary = summary
        # Indicates whether the feature of image tag immutability is enabled for the repository.
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')

        return self

