# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDataSourceConfigRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateDataSourceConfigRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateDataSourceConfigRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDataSourceConfigRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        config_item_list: List[main_models.UpdateDataSourceConfigRequestUpdateCommandConfigItemList] = None,
        id: int = None,
    ):
        # This parameter is required.
        self.config_item_list = config_item_list
        # This parameter is required.
        self.id = id

    def validate(self):
        if self.config_item_list:
            for v1 in self.config_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k1 in self.config_item_list:
                result['ConfigItemList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k1 in m.get('ConfigItemList'):
                temp_model = main_models.UpdateDataSourceConfigRequestUpdateCommandConfigItemList()
                self.config_item_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpdateDataSourceConfigRequestUpdateCommandConfigItemList(DaraModel):
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

