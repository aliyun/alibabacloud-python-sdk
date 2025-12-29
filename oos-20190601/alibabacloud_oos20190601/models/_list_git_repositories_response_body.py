# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListGitRepositoriesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        git_repos: List[main_models.ListGitRepositoriesResponseBodyGitRepos] = None,
        request_id: str = None,
    ):
        self.count = count
        self.git_repos = git_repos
        self.request_id = request_id

    def validate(self):
        if self.git_repos:
            for v1 in self.git_repos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GitRepos'] = []
        if self.git_repos is not None:
            for k1 in self.git_repos:
                result['GitRepos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.git_repos = []
        if m.get('GitRepos') is not None:
            for k1 in m.get('GitRepos'):
                temp_model = main_models.ListGitRepositoriesResponseBodyGitRepos()
                self.git_repos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGitRepositoriesResponseBodyGitRepos(DaraModel):
    def __init__(
        self,
        description: str = None,
        full_name: str = None,
        html_url: str = None,
        is_private: bool = None,
        repo_id: int = None,
    ):
        self.description = description
        self.full_name = full_name
        self.html_url = html_url
        self.is_private = is_private
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.html_url is not None:
            result['HtmlUrl'] = self.html_url

        if self.is_private is not None:
            result['IsPrivate'] = self.is_private

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('HtmlUrl') is not None:
            self.html_url = m.get('HtmlUrl')

        if m.get('IsPrivate') is not None:
            self.is_private = m.get('IsPrivate')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

