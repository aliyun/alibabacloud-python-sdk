# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCustomFieldResponseBody(DaraModel):
    def __init__(
        self,
        custom_field: main_models.GetCustomFieldResponseBodyCustomField = None,
        request_id: str = None,
    ):
        self.custom_field = custom_field
        self.request_id = request_id

    def validate(self):
        if self.custom_field:
            self.custom_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_field is not None:
            result['CustomField'] = self.custom_field.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomField') is not None:
            temp_model = main_models.GetCustomFieldResponseBodyCustomField()
            self.custom_field = temp_model.from_map(m.get('CustomField'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCustomFieldResponseBodyCustomField(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        default_value: str = None,
        description: str = None,
        encrypted: bool = None,
        entity_type: str = None,
        field_data_config: main_models.GetCustomFieldResponseBodyCustomFieldFieldDataConfig = None,
        field_data_type: str = None,
        field_display_name: str = None,
        field_display_type: str = None,
        field_id: str = None,
        field_name: str = None,
        instance_id: str = None,
        required: bool = None,
        status: str = None,
        unique: bool = None,
        update_time: int = None,
        user_permission: str = None,
    ):
        # 扩展字段创建时间，Unix时间戳格式，单位为毫秒
        self.create_time = create_time
        # 字段默认值
        self.default_value = default_value
        # 扩展字段描述
        self.description = description
        # 是否加密，默认false
        self.encrypted = encrypted
        # 字段所属实体类型
        self.entity_type = entity_type
        # 字段值配置项
        self.field_data_config = field_data_config
        # 数据类型，枚举值：string、number、boolean
        self.field_data_type = field_data_type
        # 字段展示名
        self.field_display_name = field_display_name
        # 字段展示类型，枚举值，select、checkbox、input、number
        self.field_display_type = field_display_type
        # 字段ID
        self.field_id = field_id
        # 字段标识
        self.field_name = field_name
        # 实例ID
        self.instance_id = instance_id
        # 是否必填，默认false
        self.required = required
        # 扩展字段状态, 枚举类型：enabled，disabled
        self.status = status
        # 是否唯一，默认false
        self.unique = unique
        # 扩展字段最近一次更新时间, Unix时间戳格式，单位为毫秒
        self.update_time = update_time
        # 用户端(portal侧)权限，hide、read_only、read_write，默认read_only
        self.user_permission = user_permission

    def validate(self):
        if self.field_data_config:
            self.field_data_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.field_data_config is not None:
            result['FieldDataConfig'] = self.field_data_config.to_map()

        if self.field_data_type is not None:
            result['FieldDataType'] = self.field_data_type

        if self.field_display_name is not None:
            result['FieldDisplayName'] = self.field_display_name

        if self.field_display_type is not None:
            result['FieldDisplayType'] = self.field_display_type

        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.required is not None:
            result['Required'] = self.required

        if self.status is not None:
            result['Status'] = self.status

        if self.unique is not None:
            result['Unique'] = self.unique

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_permission is not None:
            result['UserPermission'] = self.user_permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('FieldDataConfig') is not None:
            temp_model = main_models.GetCustomFieldResponseBodyCustomFieldFieldDataConfig()
            self.field_data_config = temp_model.from_map(m.get('FieldDataConfig'))

        if m.get('FieldDataType') is not None:
            self.field_data_type = m.get('FieldDataType')

        if m.get('FieldDisplayName') is not None:
            self.field_display_name = m.get('FieldDisplayName')

        if m.get('FieldDisplayType') is not None:
            self.field_display_type = m.get('FieldDisplayType')

        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Unique') is not None:
            self.unique = m.get('Unique')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserPermission') is not None:
            self.user_permission = m.get('UserPermission')

        return self

class GetCustomFieldResponseBodyCustomFieldFieldDataConfig(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetCustomFieldResponseBodyCustomFieldFieldDataConfigItems] = None,
    ):
        # 字段配置项列表，displayName、value、status
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetCustomFieldResponseBodyCustomFieldFieldDataConfigItems()
                self.items.append(temp_model.from_map(k1))

        return self

class GetCustomFieldResponseBodyCustomFieldFieldDataConfigItems(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        status: str = None,
        value: str = None,
    ):
        # 配置项展示名
        self.display_name = display_name
        # 配置项状态, 枚举值，enabled、disabled
        self.status = status
        # 配置项值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

