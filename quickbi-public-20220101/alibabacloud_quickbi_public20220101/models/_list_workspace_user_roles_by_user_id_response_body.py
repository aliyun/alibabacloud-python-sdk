# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListWorkspaceUserRolesByUserIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListWorkspaceUserRolesByUserIdResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListWorkspaceUserRolesByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWorkspaceUserRolesByUserIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        role_model: main_models.ListWorkspaceUserRolesByUserIdResponseBodyResultRoleModel = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.role_model = role_model
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.role_model:
            self.role_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_model is not None:
            result['RoleModel'] = self.role_model.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleModel') is not None:
            temp_model = main_models.ListWorkspaceUserRolesByUserIdResponseBodyResultRoleModel()
            self.role_model = temp_model.from_map(m.get('RoleModel'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class ListWorkspaceUserRolesByUserIdResponseBodyResultRoleModel(DaraModel):
    def __init__(
        self,
        role_code: str = None,
        role_id: str = None,
        role_name: str = None,
    ):
        self.role_code = role_code
        self.role_id = role_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

