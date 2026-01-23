# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoSourceCodeRepoResponseBody(DaraModel):
    def __init__(
        self,
        auto_build: str = None,
        code: str = None,
        code_repo_domain: str = None,
        code_repo_name: str = None,
        code_repo_namespace_name: str = None,
        code_repo_type: str = None,
        disable_cache_build: str = None,
        is_success: bool = None,
        oversea_build: str = None,
        repo_id: str = None,
        request_id: str = None,
    ):
        # Indicates whether image building is automatically triggered when source code is committed. Valid values:
        # 
        # *   `true`: Image building is automatically triggered when source code is committed.
        # *   `false`: Image building is not triggered when source code is committed.
        self.auto_build = auto_build
        # The response code.
        self.code = code
        # The address of the source code repository.
        self.code_repo_domain = code_repo_domain
        # The name of the source code repository.
        self.code_repo_name = code_repo_name
        # The namespace to which the source code repository belongs.
        self.code_repo_namespace_name = code_repo_namespace_name
        # The type of the code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        self.code_repo_type = code_repo_type
        # Indicates whether build cache is disabled. Valid values:
        # 
        # *   `true`: Build cache is disabled.
        # *   `false`: Build cache is enabled.
        self.disable_cache_build = disable_cache_build
        # Indicates whether the API call is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # Indicates whether image building is accelerated for servers outside the Chinese mainland. Valid values:
        # 
        # *   `true`: Image building is accelerated for servers outside the Chinese mainland.
        # *   `false`: Image building is not accelerated for servers outside the Chinese mainland.
        self.oversea_build = oversea_build
        # The ID of the repository.
        self.repo_id = repo_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build

        if self.code is not None:
            result['Code'] = self.code

        if self.code_repo_domain is not None:
            result['CodeRepoDomain'] = self.code_repo_domain

        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name

        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name

        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type

        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeRepoDomain') is not None:
            self.code_repo_domain = m.get('CodeRepoDomain')

        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')

        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')

        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')

        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

