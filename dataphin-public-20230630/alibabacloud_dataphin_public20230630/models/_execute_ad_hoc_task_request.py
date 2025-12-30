# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecuteAdHocTaskRequest(DaraModel):
    def __init__(
        self,
        execute_command: main_models.ExecuteAdHocTaskRequestExecuteCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.execute_command = execute_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.execute_command:
            self.execute_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execute_command is not None:
            result['ExecuteCommand'] = self.execute_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteCommand') is not None:
            temp_model = main_models.ExecuteAdHocTaskRequestExecuteCommand()
            self.execute_command = temp_model.from_map(m.get('ExecuteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ExecuteAdHocTaskRequestExecuteCommand(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_source_catalog: str = None,
        data_source_id: int = None,
        data_source_schema: str = None,
        operator_type: str = None,
        param_list: List[main_models.ExecuteAdHocTaskRequestExecuteCommandParamList] = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.code = code
        self.data_source_catalog = data_source_catalog
        self.data_source_id = data_source_id
        self.data_source_schema = data_source_schema
        # This parameter is required.
        self.operator_type = operator_type
        self.param_list = param_list
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.ExecuteAdHocTaskRequestExecuteCommandParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ExecuteAdHocTaskRequestExecuteCommandParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

