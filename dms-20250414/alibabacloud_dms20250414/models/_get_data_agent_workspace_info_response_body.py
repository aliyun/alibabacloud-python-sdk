# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetDataAgentWorkspaceInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataAgentWorkspaceInfoResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataAgentWorkspaceInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataAgentWorkspaceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        modify_time: str = None,
        role_name: str = None,
        total_member: str = None,
        workspace_desc: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.modify_time = modify_time
        self.role_name = role_name
        self.total_member = total_member
        self.workspace_desc = workspace_desc
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name
        self.workspace_status = workspace_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.total_member is not None:
            result['TotalMember'] = self.total_member

        if self.workspace_desc is not None:
            result['WorkspaceDesc'] = self.workspace_desc

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.workspace_status is not None:
            result['WorkspaceStatus'] = self.workspace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('TotalMember') is not None:
            self.total_member = m.get('TotalMember')

        if m.get('WorkspaceDesc') is not None:
            self.workspace_desc = m.get('WorkspaceDesc')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('WorkspaceStatus') is not None:
            self.workspace_status = m.get('WorkspaceStatus')

        return self

