# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeTablePermissionRequest(DaraModel):
    def __init__(
        self,
        actions: str = None,
        max_compute_project_name: str = None,
        revoke_user_id: str = None,
        revoke_user_name: str = None,
        table_name: str = None,
        workspace_id: int = None,
    ):
        # The operation permissions on the table that you want to revoke. Separate multiple operation permissions with commas (,).
        # 
        # Currently, only the Select, Describe, and Download operation permissions on MaxCompute tables can be revoked.
        # 
        # This parameter is required.
        self.actions = actions
        # The name of the MaxCompute project that contains the table from which you want to revoke permissions. You can log on to the DataWorks console and go to the Workspace Settings page to obtain the name of the MaxCompute project associated with the DataWorks workspace.
        # 
        # This parameter is required.
        self.max_compute_project_name = max_compute_project_name
        # The Alibaba Cloud account ID from which you want to revoke table permissions. You can logon to the DataWorks console and go to the Security Settings page to obtain the account ID.
        # 
        # You only need to specify either this parameter or the RevokeUserName parameter. If both this parameter and the RevokeUserName parameter are specified in the parameter settings but have different values, the value of the RevokeUserId parameter takes precedence.
        self.revoke_user_id = revoke_user_id
        # The name of the Alibaba Cloud account from which you want to revoke table permissions. The account format is the same as the account format used in MaxCompute.
        # - An Alibaba Cloud account is in the format of ALIYUN$+account name.
        # - A RAM user is in the format of RAM$+account name.
        # 
        # You only need to specify either this parameter or the RevokeUserId parameter. If both this parameter and the RevokeUserId parameter are specified in the parameter settings but have different values, the value of the RevokeUserId parameter takes precedence.
        self.revoke_user_name = revoke_user_name
        # The name of the MaxCompute table from which you want to revoke permissions. You can call the [SearchMetaTables](https://help.aliyun.com/document_detail/173919.html) operation to obtain the MaxCompute table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the DataWorks workspace to which the MaxCompute table belongs. You can log on to the DataWorks console and go to the Workspace Settings page to obtain the workspace ID.
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
        if self.actions is not None:
            result['Actions'] = self.actions

        if self.max_compute_project_name is not None:
            result['MaxComputeProjectName'] = self.max_compute_project_name

        if self.revoke_user_id is not None:
            result['RevokeUserId'] = self.revoke_user_id

        if self.revoke_user_name is not None:
            result['RevokeUserName'] = self.revoke_user_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')

        if m.get('MaxComputeProjectName') is not None:
            self.max_compute_project_name = m.get('MaxComputeProjectName')

        if m.get('RevokeUserId') is not None:
            self.revoke_user_id = m.get('RevokeUserId')

        if m.get('RevokeUserName') is not None:
            self.revoke_user_name = m.get('RevokeUserName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

