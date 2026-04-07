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
        # The permissions that you want to revoke. Separate multiple permissions with commas (,). You can revoke only the SELECT, DESCRIBE, and DOWNLOAD permissions on MaxCompute tables.
        # 
        # This parameter is required.
        self.actions = actions
        # The name of the MaxCompute project to which the table belongs. You can log on to the DataWorks console and go to the SettingCenter page to obtain the name of the MaxCompute project that you associate with the workspace.
        # 
        # This parameter is required.
        self.max_compute_project_name = max_compute_project_name
        # The ID of the Alibaba Cloud account from which you want to revoke permissions. You can log on to the DataWorks console and go to the Security Settings page to obtain the ID. You must specify either this parameter or the RevokeUserName parameter. If you specify both this parameter and the RevokeUserName parameter and the parameter values are different, the value of this parameter prevails.
        self.revoke_user_id = revoke_user_id
        # The Alibaba Cloud account from which you want to revoke permissions. Specify this parameter in the format that is the same as the format of the account used to access the MaxCompute project.
        # 
        # *   If the account is an Alibaba Cloud account, the value is in the ALIYUN$+Account name format.
        # *   If the account is a RAM user, the value is in the RAM$+Account name format.
        # 
        # You must specify either this parameter or the RevokeUserId parameter. If you specify both this parameter and the RevokeUserId parameter and the parameter values are different, the value of the RevokeUserId parameter prevails.
        self.revoke_user_name = revoke_user_name
        # The name of the MaxCompute table. You can call the [SearchMetaTables](https://help.aliyun.com/document_detail/173919.html) operation to query the name of the MaxCompute table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the DataWorks workspace with which the MaxCompute project is associated. You can log on to the DataWorks console and go to the Workspace page to obtain the ID.
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

