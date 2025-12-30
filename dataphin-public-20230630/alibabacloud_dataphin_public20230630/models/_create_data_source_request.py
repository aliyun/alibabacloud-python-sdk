# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateDataSourceRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateDataSourceRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateDataSourceRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateDataSourceRequestCreateCommand(DaraModel):
    def __init__(
        self,
        dev_data_source_create: main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreate = None,
        prod_data_source_create: main_models.CreateDataSourceRequestCreateCommandProdDataSourceCreate = None,
    ):
        self.dev_data_source_create = dev_data_source_create
        # 数据源创建结构体
        self.prod_data_source_create = prod_data_source_create

    def validate(self):
        if self.dev_data_source_create:
            self.dev_data_source_create.validate()
        if self.prod_data_source_create:
            self.prod_data_source_create.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_data_source_create is not None:
            result['DevDataSourceCreate'] = self.dev_data_source_create.to_map()

        if self.prod_data_source_create is not None:
            result['ProdDataSourceCreate'] = self.prod_data_source_create.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceCreate') is not None:
            temp_model = main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreate()
            self.dev_data_source_create = temp_model.from_map(m.get('DevDataSourceCreate'))

        if m.get('ProdDataSourceCreate') is not None:
            temp_model = main_models.CreateDataSourceRequestCreateCommandProdDataSourceCreate()
            self.prod_data_source_create = temp_model.from_map(m.get('ProdDataSourceCreate'))

        return self

class CreateDataSourceRequestCreateCommandProdDataSourceCreate(DaraModel):
    def __init__(
        self,
        check_activity: bool = None,
        config_item_list: List[main_models.CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList] = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_activity = check_activity
        # This parameter is required.
        self.config_item_list = config_item_list
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

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
        if self.check_activity is not None:
            result['CheckActivity'] = self.check_activity

        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k1 in self.config_item_list:
                result['ConfigItemList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckActivity') is not None:
            self.check_activity = m.get('CheckActivity')

        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k1 in m.get('ConfigItemList'):
                temp_model = main_models.CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList()
                self.config_item_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList(DaraModel):
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

class CreateDataSourceRequestCreateCommandDevDataSourceCreate(DaraModel):
    def __init__(
        self,
        data_source_create: main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate = None,
        prod_data_source_id: int = None,
    ):
        # 数据源创建结构体
        self.data_source_create = data_source_create
        self.prod_data_source_id = prod_data_source_id

    def validate(self):
        if self.data_source_create:
            self.data_source_create.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_create is not None:
            result['DataSourceCreate'] = self.data_source_create.to_map()

        if self.prod_data_source_id is not None:
            result['ProdDataSourceId'] = self.prod_data_source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceCreate') is not None:
            temp_model = main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate()
            self.data_source_create = temp_model.from_map(m.get('DataSourceCreate'))

        if m.get('ProdDataSourceId') is not None:
            self.prod_data_source_id = m.get('ProdDataSourceId')

        return self

class CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate(DaraModel):
    def __init__(
        self,
        check_activity: bool = None,
        config_item_list: List[main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList] = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_activity = check_activity
        # This parameter is required.
        self.config_item_list = config_item_list
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

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
        if self.check_activity is not None:
            result['CheckActivity'] = self.check_activity

        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k1 in self.config_item_list:
                result['ConfigItemList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckActivity') is not None:
            self.check_activity = m.get('CheckActivity')

        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k1 in m.get('ConfigItemList'):
                temp_model = main_models.CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList()
                self.config_item_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList(DaraModel):
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

