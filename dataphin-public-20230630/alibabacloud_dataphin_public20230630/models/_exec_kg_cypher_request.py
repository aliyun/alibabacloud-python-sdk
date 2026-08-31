# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecKgCypherRequest(DaraModel):
    def __init__(
        self,
        exec_command: main_models.ExecKgCypherRequestExecCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        workspace_id: str = None,
    ):
        # The custom Cypher query instruction.
        # 
        # This parameter is required.
        self.exec_command = exec_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The model ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.exec_command:
            self.exec_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_command is not None:
            result['ExecCommand'] = self.exec_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecCommand') is not None:
            temp_model = main_models.ExecKgCypherRequestExecCommand()
            self.exec_command = temp_model.from_map(m.get('ExecCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ExecKgCypherRequestExecCommand(DaraModel):
    def __init__(
        self,
        limit: int = None,
        params: List[main_models.ExecKgCypherRequestExecCommandParams] = None,
        query: str = None,
    ):
        # The maximum number of records to return.
        self.limit = limit
        # The input parameters of the query statement.
        self.params = params
        # The custom Cypher query statement.
        self.query = query

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.ExecKgCypherRequestExecCommandParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class ExecKgCypherRequestExecCommandParams(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        key: str = None,
        value: str = None,
    ):
        # The data type of paramValue.
        self.data_type = data_type
        # paramKey
        self.key = key
        # paramValue
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

