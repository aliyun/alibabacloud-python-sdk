# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OperateInstanceRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        operate_command: main_models.OperateInstanceRequestOperateCommand = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.operate_command = operate_command

    def validate(self):
        if self.operate_command:
            self.operate_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.operate_command is not None:
            result['OperateCommand'] = self.operate_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OperateCommand') is not None:
            temp_model = main_models.OperateInstanceRequestOperateCommand()
            self.operate_command = temp_model.from_map(m.get('OperateCommand'))

        return self

class OperateInstanceRequestOperateCommand(DaraModel):
    def __init__(
        self,
        instance_id_list: List[main_models.OperateInstanceRequestOperateCommandInstanceIdList] = None,
        operation: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # This parameter is required.
        self.operation = operation
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.instance_id_list:
            for v1 in self.instance_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceIdList'] = []
        if self.instance_id_list is not None:
            for k1 in self.instance_id_list:
                result['InstanceIdList'].append(k1.to_map() if k1 else None)

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_id_list = []
        if m.get('InstanceIdList') is not None:
            for k1 in m.get('InstanceIdList'):
                temp_model = main_models.OperateInstanceRequestOperateCommandInstanceIdList()
                self.instance_id_list.append(temp_model.from_map(k1))

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class OperateInstanceRequestOperateCommandInstanceIdList(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

