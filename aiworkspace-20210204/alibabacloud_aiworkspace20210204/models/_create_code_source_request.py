# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCodeSourceRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        description: str = None,
        display_name: str = None,
        mount_path: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the code build. Valid values:
        # 
        # *   PUBLIC: The code build is visible to all members in the workspace.
        # *   PRIVATE: The code build is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The code branch.
        self.code_branch = code_branch
        self.code_commit = code_commit
        # The URL of the code repository.
        self.code_repo = code_repo
        # The token used to access the code repository.
        self.code_repo_access_token = code_repo_access_token
        # The username of the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The description of the code build, which helps you distinguish between code builds.
        self.description = description
        # The name of the code build.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The local mount path of the code. By default, the code is mounted to the /root/code/ path.
        self.mount_path = mount_path
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

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

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

