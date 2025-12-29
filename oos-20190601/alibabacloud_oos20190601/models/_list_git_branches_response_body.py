# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListGitBranchesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        git_branches: List[main_models.ListGitBranchesResponseBodyGitBranches] = None,
        request_id: str = None,
    ):
        self.count = count
        self.git_branches = git_branches
        self.request_id = request_id

    def validate(self):
        if self.git_branches:
            for v1 in self.git_branches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GitBranches'] = []
        if self.git_branches is not None:
            for k1 in self.git_branches:
                result['GitBranches'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.git_branches = []
        if m.get('GitBranches') is not None:
            for k1 in m.get('GitBranches'):
                temp_model = main_models.ListGitBranchesResponseBodyGitBranches()
                self.git_branches.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGitBranchesResponseBodyGitBranches(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

