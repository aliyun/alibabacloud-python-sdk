# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SyncDepartmentUserRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        sync_department_user_command: main_models.SyncDepartmentUserRequestSyncDepartmentUserCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.sync_department_user_command = sync_department_user_command

    def validate(self):
        if self.sync_department_user_command:
            self.sync_department_user_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.sync_department_user_command is not None:
            result['SyncDepartmentUserCommand'] = self.sync_department_user_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SyncDepartmentUserCommand') is not None:
            temp_model = main_models.SyncDepartmentUserRequestSyncDepartmentUserCommand()
            self.sync_department_user_command = temp_model.from_map(m.get('SyncDepartmentUserCommand'))

        return self

class SyncDepartmentUserRequestSyncDepartmentUserCommand(DaraModel):
    def __init__(
        self,
        dept_user_mapping: List[main_models.SyncDepartmentUserRequestSyncDepartmentUserCommandDeptUserMapping] = None,
    ):
        # This parameter is required.
        self.dept_user_mapping = dept_user_mapping

    def validate(self):
        if self.dept_user_mapping:
            for v1 in self.dept_user_mapping:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeptUserMapping'] = []
        if self.dept_user_mapping is not None:
            for k1 in self.dept_user_mapping:
                result['DeptUserMapping'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dept_user_mapping = []
        if m.get('DeptUserMapping') is not None:
            for k1 in m.get('DeptUserMapping'):
                temp_model = main_models.SyncDepartmentUserRequestSyncDepartmentUserCommandDeptUserMapping()
                self.dept_user_mapping.append(temp_model.from_map(k1))

        return self

class SyncDepartmentUserRequestSyncDepartmentUserCommandDeptUserMapping(DaraModel):
    def __init__(
        self,
        department_id_list: List[str] = None,
        source_user_id: str = None,
    ):
        self.department_id_list = department_id_list
        # This parameter is required.
        self.source_user_id = source_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id_list is not None:
            result['DepartmentIdList'] = self.department_id_list

        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentIdList') is not None:
            self.department_id_list = m.get('DepartmentIdList')

        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')

        return self

