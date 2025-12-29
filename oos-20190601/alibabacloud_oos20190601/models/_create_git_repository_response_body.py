# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateGitRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        git_repo: main_models.CreateGitRepositoryResponseBodyGitRepo = None,
        request_id: str = None,
    ):
        self.git_repo = git_repo
        self.request_id = request_id

    def validate(self):
        if self.git_repo:
            self.git_repo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.git_repo is not None:
            result['GitRepo'] = self.git_repo.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GitRepo') is not None:
            temp_model = main_models.CreateGitRepositoryResponseBodyGitRepo()
            self.git_repo = temp_model.from_map(m.get('GitRepo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateGitRepositoryResponseBodyGitRepo(DaraModel):
    def __init__(
        self,
        description: str = None,
        full_name: str = None,
        html_url: str = None,
        is_private: str = None,
    ):
        self.description = description
        self.full_name = full_name
        self.html_url = html_url
        self.is_private = is_private

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

        return self

