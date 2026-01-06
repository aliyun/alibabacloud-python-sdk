# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCodeSourceRequest(DaraModel):
    def __init__(
        self,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        description: str = None,
        display_name: str = None,
        mount_path: str = None,
    ):
        # The name of the code branch.
        self.code_branch = code_branch
        # The code commit ID.
        self.code_commit = code_commit
        # The address of the code repository.
        self.code_repo = code_repo
        # The access token corresponding to the username.
        self.code_repo_access_token = code_repo_access_token
        # The username used to access the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The description of the code build.
        self.description = description
        # The name of the code build.
        self.display_name = display_name
        # The default mount path.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch

        if self.code_commit is not None:
            result['CodeCommit'] = self.code_commit

        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo

        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token

        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')

        if m.get('CodeCommit') is not None:
            self.code_commit = m.get('CodeCommit')

        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')

        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')

        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

