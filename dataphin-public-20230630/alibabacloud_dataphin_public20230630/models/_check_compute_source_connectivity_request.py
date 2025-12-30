# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CheckComputeSourceConnectivityRequest(DaraModel):
    def __init__(
        self,
        check_command: main_models.CheckComputeSourceConnectivityRequestCheckCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command = check_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.check_command:
            self.check_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_command is not None:
            result['CheckCommand'] = self.check_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            temp_model = main_models.CheckComputeSourceConnectivityRequestCheckCommand()
            self.check_command = temp_model.from_map(m.get('CheckCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CheckComputeSourceConnectivityRequestCheckCommand(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.CheckComputeSourceConnectivityRequestCheckCommandConfigList] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.config_list = config_list
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.CheckComputeSourceConnectivityRequestCheckCommandConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CheckComputeSourceConnectivityRequestCheckCommandConfigList(DaraModel):
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

