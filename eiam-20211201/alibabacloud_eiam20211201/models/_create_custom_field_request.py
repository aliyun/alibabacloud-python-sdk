# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateCustomFieldRequest(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        encrypted: bool = None,
        entity_type: str = None,
        field_data_config: main_models.CreateCustomFieldRequestFieldDataConfig = None,
        field_data_type: str = None,
        field_display_name: str = None,
        field_display_type: str = None,
        field_name: str = None,
        instance_id: str = None,
        required: bool = None,
        unique: bool = None,
        user_permission: str = None,
    ):
        # The default value of the field. If the field has configuration items, the default value must be one of the enabled configuration items. The default value can be up to 1024 characters in length.
        self.default_value = default_value
        # The description of the field. The description can be up to 512 characters in length.
        self.description = description
        # Indicates whether to encrypt the field value. If you set this parameter to true, the system encrypts the data value before storing it.
        self.encrypted = encrypted
        # The entity to which the field belongs. Valid value:
        # 
        # - user: an account.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The configuration items of the field value.
        self.field_data_config = field_data_config
        # The data type of the field. Valid values:
        # 
        # - string: a string.
        # 
        # - number: a number. The number can be up to 32 digits in length and can be a positive integer or a decimal.
        # 
        # - boolean: a Boolean value.
        # 
        # This parameter is required.
        self.field_data_type = field_data_type
        # The display name of the field. The display name can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.field_display_name = field_display_name
        # The display type of the field. Valid values:
        # 
        # - input: a text box. This display type supports the string and number data types.
        # 
        # - select: a drop-down list. This display type supports the string and Boolean data types.
        # 
        # - checkbox: a check box. This display type supports the string data type.
        # 
        # This parameter is required.
        self.field_display_type = field_display_type
        # The name of the field. The name can be up to 40 characters in length and can contain lowercase letters and underscores (_). It cannot start with an underscore (_).
        # 
        # This parameter is required.
        self.field_name = field_name
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Indicates whether the field is required.
        self.required = required
        # Indicates whether the field value is unique. If you set this parameter to true, the value of this field must be unique for the specified entity type.
        self.unique = unique
        # The permission on the field in the portal. Valid values:
        # 
        # - hide: The field is not visible in the portal.
        # 
        # - read_only: The field is visible but cannot be modified in the portal.
        # 
        # - read_write: The field is visible and can be modified in the portal.
        self.user_permission = user_permission

    def validate(self):
        if self.field_data_config:
            self.field_data_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.required is not None:
            result['Required'] = self.required

        if self.unique is not None:
            result['Unique'] = self.unique

        if self.user_permission is not None:
            result['UserPermission'] = self.user_permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('FieldDataConfig') is not None:
            temp_model = main_models.CreateCustomFieldRequestFieldDataConfig()
            self.field_data_config = temp_model.from_map(m.get('FieldDataConfig'))

        if m.get('FieldDataType') is not None:
            self.field_data_type = m.get('FieldDataType')

        if m.get('FieldDisplayName') is not None:
            self.field_display_name = m.get('FieldDisplayName')

        if m.get('FieldDisplayType') is not None:
            self.field_display_type = m.get('FieldDisplayType')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Unique') is not None:
            self.unique = m.get('Unique')

        if m.get('UserPermission') is not None:
            self.user_permission = m.get('UserPermission')

        return self

class CreateCustomFieldRequestFieldDataConfig(DaraModel):
    def __init__(
        self,
        items: List[main_models.CreateCustomFieldRequestFieldDataConfigItems] = None,
    ):
        # A list of field configuration items. The list can contain up to 100 items.
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
                temp_model = main_models.CreateCustomFieldRequestFieldDataConfigItems()
                self.items.append(temp_model.from_map(k1))

        return self

class CreateCustomFieldRequestFieldDataConfigItems(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        status: str = None,
        value: str = None,
    ):
        # The display name of the configuration item. The display name can be up to 128 characters in length.
        self.display_name = display_name
        # The status of the configuration item. Valid values:
        # 
        # - enabled: The configuration item is enabled.
        # 
        # - disabled: The configuration item is disabled.
        # 
        # If a configuration item is disabled, it is unavailable when you create or update the field value for an entity.
        self.status = status
        # The value of the configuration item. The value can be up to 64 characters in length.
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

