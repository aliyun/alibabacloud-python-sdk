# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoSourceCodeRepoRequest(DaraModel):
    def __init__(
        self,
        auto_build: bool = None,
        code_repo_name: str = None,
        code_repo_namespace_name: str = None,
        code_repo_type: str = None,
        disable_cache_build: bool = None,
        instance_id: str = None,
        oversea_build: bool = None,
        repo_id: str = None,
    ):
        # Specifies whether to trigger image building when source code is committed. Valid values:
        # 
        # *   `true`: triggers image building when source code is committed.
        # *   `false`: does not trigger image building when source code is committed.
        self.auto_build = auto_build
        # The name of the source code repository.
        # 
        # This parameter is required.
        self.code_repo_name = code_repo_name
        # The namespace to which the source code repository belongs.
        # 
        # This parameter is required.
        self.code_repo_namespace_name = code_repo_namespace_name
        # The type of the source code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        # 
        # This parameter is required.
        self.code_repo_type = code_repo_type
        # Specifies whether to disable building caches. Valid values:
        # 
        # *   `true`: disables building caches.
        # *   `false`: enables building caches.
        self.disable_cache_build = disable_cache_build
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable Build With Servers Deployed Outside Chinese Mainland. Valid values:
        # 
        # *   `true`: enables Build With Servers Deployed Outside Chinese Mainland.
        # *   `false`: does not enable Build With Servers Deployed Outside Chinese Mainland.
        self.oversea_build = oversea_build
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build

        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name

        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name

        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type

        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')

        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')

        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')

        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')

        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

