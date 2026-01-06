# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCodeSourceResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        code_source_id: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        mount_path: str = None,
        request_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the code source. Valid values:
        # 
        # *   PRIVATE: Visible only to you and the administrator of the workspace.
        # *   PUBLIC: Visible to all members in the workspace.
        self.accessibility = accessibility
        # The code repository branch.
        self.code_branch = code_branch
        # The code commit ID.
        self.code_commit = code_commit
        # The address of the code repository.
        self.code_repo = code_repo
        # The token used to access the code repository.
        self.code_repo_access_token = code_repo_access_token
        # The username of the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The ID of the code source.
        self.code_source_id = code_source_id
        # The description of the code source.
        self.description = description
        # The name of the code source.
        self.display_name = display_name
        # The time when the code source was created, in the ISO8601 format.
        self.gmt_create_time = gmt_create_time
        # The time when the code source was modified, in the ISO8601 format.
        self.gmt_modify_time = gmt_modify_time
        # The local mount path of the code.
        self.mount_path = mount_path
        # The request ID.
        self.request_id = request_id
        # The ID of the creator.
        self.user_id = user_id
        # The workspace ID.
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

        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

