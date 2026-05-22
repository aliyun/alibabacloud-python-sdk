# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListAcrImageRepositoriesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        repositories: List[main_models.ListAcrImageRepositoriesResponseBodyRepositories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The images.
        self.repositories = repositories
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.repositories = []
        if m.get('Repositories') is not None:
            for k1 in m.get('Repositories'):
                temp_model = main_models.ListAcrImageRepositoriesResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAcrImageRepositoriesResponseBodyRepositories(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modified_time: str = None,
        namespace: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_type: str = None,
    ):
        # The time when the image was created.
        self.create_time = create_time
        # The time when the image was modified.
        self.modified_time = modified_time
        # The namespace of the repository
        self.namespace = namespace
        # The image repo ID.
        self.repo_id = repo_id
        # The image repo name.
        self.repo_name = repo_name
        # The type of the repository. Valid values:
        # 
        # *   `Private`: a private repository
        # *   `Public`: a public repository
        self.repo_type = repo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        return self

