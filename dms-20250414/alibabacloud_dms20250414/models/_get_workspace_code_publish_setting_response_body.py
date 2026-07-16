# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceCodePublishSettingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetWorkspaceCodePublishSettingResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code that indicates the result of the request. A value of `200` indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetWorkspaceCodePublishSettingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetWorkspaceCodePublishSettingResponseBodyData(DaraModel):
    def __init__(
        self,
        exclude: List[str] = None,
        lock_repo_branch: bool = None,
        repos: List[main_models.GetWorkspaceCodePublishSettingResponseBodyDataRepos] = None,
    ):
        # The files and directories to exclude from the deployment.
        self.exclude = exclude
        # Indicates whether the deployment branch is locked. If `true`, configurations submitted via the `workspaceCodePublish` API are ignored. If `false`, configurations submitted via the `workspaceCodePublish` API update the settings.
        self.lock_repo_branch = lock_repo_branch
        # The Git repositories in the workspace.
        self.repos = repos

    def validate(self):
        if self.repos:
            for v1 in self.repos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.lock_repo_branch is not None:
            result['LockRepoBranch'] = self.lock_repo_branch

        result['Repos'] = []
        if self.repos is not None:
            for k1 in self.repos:
                result['Repos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('LockRepoBranch') is not None:
            self.lock_repo_branch = m.get('LockRepoBranch')

        self.repos = []
        if m.get('Repos') is not None:
            for k1 in m.get('Repos'):
                temp_model = main_models.GetWorkspaceCodePublishSettingResponseBodyDataRepos()
                self.repos.append(temp_model.from_map(k1))

        return self

class GetWorkspaceCodePublishSettingResponseBodyDataRepos(DaraModel):
    def __init__(
        self,
        branch: str = None,
        path: str = None,
        repo: str = None,
    ):
        # The name of the branch.
        self.branch = branch
        # The path to the notebook file.
        self.path = path
        # The name of the repository.
        self.repo = repo

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch

        if self.path is not None:
            result['Path'] = self.path

        if self.repo is not None:
            result['Repo'] = self.repo

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Repo') is not None:
            self.repo = m.get('Repo')

        return self

