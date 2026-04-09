# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class CreateDataPermissionsRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        data_type: str = None,
        permission_user_infos: List[main_models.CreateDataPermissionsRequestPermissionUserInfos] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.data_id = data_id
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.permission_user_infos = permission_user_infos
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.permission_user_infos:
            for v1 in self.permission_user_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        result['PermissionUserInfos'] = []
        if self.permission_user_infos is not None:
            for k1 in self.permission_user_infos:
                result['PermissionUserInfos'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        self.permission_user_infos = []
        if m.get('PermissionUserInfos') is not None:
            for k1 in m.get('PermissionUserInfos'):
                temp_model = main_models.CreateDataPermissionsRequestPermissionUserInfos()
                self.permission_user_infos.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateDataPermissionsRequestPermissionUserInfos(DaraModel):
    def __init__(
        self,
        permission_user_id: str = None,
        permission_username: str = None,
    ):
        # This parameter is required.
        self.permission_user_id = permission_user_id
        self.permission_username = permission_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_user_id is not None:
            result['PermissionUserId'] = self.permission_user_id

        if self.permission_username is not None:
            result['PermissionUsername'] = self.permission_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionUserId') is not None:
            self.permission_user_id = m.get('PermissionUserId')

        if m.get('PermissionUsername') is not None:
            self.permission_username = m.get('PermissionUsername')

        return self

