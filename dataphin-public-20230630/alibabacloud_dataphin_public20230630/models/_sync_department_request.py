# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SyncDepartmentRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        sync_department_command: main_models.SyncDepartmentRequestSyncDepartmentCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.sync_department_command = sync_department_command

    def validate(self):
        if self.sync_department_command:
            self.sync_department_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.sync_department_command is not None:
            result['SyncDepartmentCommand'] = self.sync_department_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SyncDepartmentCommand') is not None:
            temp_model = main_models.SyncDepartmentRequestSyncDepartmentCommand()
            self.sync_department_command = temp_model.from_map(m.get('SyncDepartmentCommand'))

        return self

class SyncDepartmentRequestSyncDepartmentCommand(DaraModel):
    def __init__(
        self,
        department_list: List[main_models.SyncDepartmentRequestSyncDepartmentCommandDepartmentList] = None,
    ):
        # This parameter is required.
        self.department_list = department_list

    def validate(self):
        if self.department_list:
            for v1 in self.department_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DepartmentList'] = []
        if self.department_list is not None:
            for k1 in self.department_list:
                result['DepartmentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.department_list = []
        if m.get('DepartmentList') is not None:
            for k1 in m.get('DepartmentList'):
                temp_model = main_models.SyncDepartmentRequestSyncDepartmentCommandDepartmentList()
                self.department_list.append(temp_model.from_map(k1))

        return self

class SyncDepartmentRequestSyncDepartmentCommandDepartmentList(DaraModel):
    def __init__(
        self,
        department_id: str = None,
        department_name: str = None,
        parent_department_id: str = None,
    ):
        # This parameter is required.
        self.department_id = department_id
        # This parameter is required.
        self.department_name = department_name
        self.parent_department_id = parent_department_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        if self.parent_department_id is not None:
            result['ParentDepartmentId'] = self.parent_department_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        if m.get('ParentDepartmentId') is not None:
            self.parent_department_id = m.get('ParentDepartmentId')

        return self

