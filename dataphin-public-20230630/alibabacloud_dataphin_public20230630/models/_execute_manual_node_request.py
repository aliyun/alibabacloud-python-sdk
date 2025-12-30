# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecuteManualNodeRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        execute_command: main_models.ExecuteManualNodeRequestExecuteCommand = None,
        op_tenant_id: int = None,
    ):
        self.env = env
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
        if self.env is not None:
            result['Env'] = self.env

        if self.execute_command is not None:
            result['ExecuteCommand'] = self.execute_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExecuteCommand') is not None:
            temp_model = main_models.ExecuteManualNodeRequestExecuteCommand()
            self.execute_command = temp_model.from_map(m.get('ExecuteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ExecuteManualNodeRequestExecuteCommand(DaraModel):
    def __init__(
        self,
        end_biz_date: str = None,
        flow_name: str = None,
        node_id: str = None,
        param_list: List[main_models.ExecuteManualNodeRequestExecuteCommandParamList] = None,
        project_id: int = None,
        start_biz_date: str = None,
    ):
        # This parameter is required.
        self.end_biz_date = end_biz_date
        self.flow_name = flow_name
        # This parameter is required.
        self.node_id = node_id
        self.param_list = param_list
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.start_biz_date = start_biz_date

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
        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.ExecuteManualNodeRequestExecuteCommandParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')

        return self

class ExecuteManualNodeRequestExecuteCommandParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

