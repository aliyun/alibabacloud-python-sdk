# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChartRepositoryRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        return self

