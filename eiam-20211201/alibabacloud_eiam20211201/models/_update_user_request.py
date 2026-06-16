# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        custom_fields: List[main_models.UpdateUserRequestCustomFields] = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        instance_id: str = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        user_id: str = None,
        username: str = None,
    ):
        # A list of custom field objects.
        self.custom_fields = custom_fields
        # The display name. It can be a maximum of 256 characters.
        self.display_name = display_name
        # The email address. The local-part can contain uppercase letters, lowercase letters, digits, dots (.), underscores (_), and hyphens (-).
        self.email = email
        # Indicates whether the email address is verified. This parameter is required when specifying an email address. In most cases, set this to `true`.
        self.email_verified = email_verified
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mobile phone number. It must be between 6 and 15 digits long.
        self.phone_number = phone_number
        # Indicates whether the mobile phone number is verified. This parameter is required when specifying a mobile phone number. In most cases, set this to `true`.
        self.phone_number_verified = phone_number_verified
        # The country code for the mobile phone number. Example: 86 for Chinese mainland. Do not include `00` or `+`. This parameter is required if you specify a mobile phone number.
        self.phone_region = phone_region
        # The account ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username. It must be no more than 256 characters and can contain letters, digits, and the special characters: _, ., @, and -.
        self.username = username

    def validate(self):
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.UpdateUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')

        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class UpdateUserRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        operation: str = None,
    ):
        # The custom field name. You must create the custom field in the console before using it. For more information, see the custom fields module in the console.
        self.field_name = field_name
        # The custom field value. The value must comply with the constraints of the custom field.
        self.field_value = field_value
        # The operation type for the custom field. Valid values:
        # 
        # - `add`: Adds a value to the custom field.
        # 
        # - `replace`: Replaces the existing value of the custom field. If the field has no existing value, this operation adds the value instead.
        # 
        # - `remove`: Removes a value from the custom field.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

