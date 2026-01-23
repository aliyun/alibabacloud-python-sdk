# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRepositoryRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
    ):
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value larger than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')

        return self

