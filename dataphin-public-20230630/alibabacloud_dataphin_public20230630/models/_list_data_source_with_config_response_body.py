# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceWithConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataSourceWithConfigResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataSourceWithConfigResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data_source_list: List[main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceList] = None,
        total_count: int = None,
    ):
        self.data_source_list = data_source_list
        self.total_count = total_count

    def validate(self):
        if self.data_source_list:
            for v1 in self.data_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSourceList'] = []
        if self.data_source_list is not None:
            for k1 in self.data_source_list:
                result['DataSourceList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_list = []
        if m.get('DataSourceList') is not None:
            for k1 in m.get('DataSourceList'):
                temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceList()
                self.data_source_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataSourceWithConfigResponseBodyPageResultDataSourceList(DaraModel):
    def __init__(
        self,
        dev_data_source_info: main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo = None,
        prod_data_source_info: main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo = None,
    ):
        # 开发环境数据源信息
        self.dev_data_source_info = dev_data_source_info
        # 生产环境数据源
        self.prod_data_source_info = prod_data_source_info

    def validate(self):
        if self.dev_data_source_info:
            self.dev_data_source_info.validate()
        if self.prod_data_source_info:
            self.prod_data_source_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_data_source_info is not None:
            result['DevDataSourceInfo'] = self.dev_data_source_info.to_map()

        if self.prod_data_source_info is not None:
            result['ProdDataSourceInfo'] = self.prod_data_source_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceInfo') is not None:
            temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo()
            self.dev_data_source_info = temp_model.from_map(m.get('DevDataSourceInfo'))

        if m.get('ProdDataSourceInfo') is not None:
            temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo()
            self.prod_data_source_info = temp_model.from_map(m.get('ProdDataSourceInfo'))

        return self

class ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo(DaraModel):
    def __init__(
        self,
        config_item_list: List[main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList] = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.config_item_list = config_item_list
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.scope = scope
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
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k1 in self.config_item_list:
                result['ConfigItemList'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k1 in m.get('ConfigItemList'):
                temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList()
                self.config_item_list.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList(DaraModel):
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

class ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo(DaraModel):
    def __init__(
        self,
        config_item_list: List[main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList] = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.config_item_list = config_item_list
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.scope = scope
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
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k1 in self.config_item_list:
                result['ConfigItemList'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.env is not None:
            result['Env'] = self.env

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k1 in m.get('ConfigItemList'):
                temp_model = main_models.ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList()
                self.config_item_list.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList(DaraModel):
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

