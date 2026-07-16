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
        # The list of custom field objects.
        self.custom_fields = custom_fields
        # The display name of the account. The name can be up to 256 characters in length.
        self.display_name = display_name
        # The email address. The prefix of the email address can contain uppercase letters, lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        self.email = email
        # Specifies whether the email address is verified. This parameter is required if an email address is specified. If no special business requirements exist, set this parameter to true.
        self.email_verified = email_verified
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The phone number. The value must be 6 to 15 digits in length.
        self.phone_number = phone_number
        # Specifies whether the phone number is verified as a trusted phone number. This parameter is required if a phone number is specified. If no special business requirements exist, set this parameter to true.
        self.phone_number_verified = phone_number_verified
        # The phone region code. Example: 86 for the Chinese mainland, without the 00 or + prefix. This parameter is required if a phone number is specified.
        self.phone_region = phone_region
        # The account ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The account name. The name can contain letters, digits, underscores (_), periods (.), at signs (@), and hyphens (-). The name can be up to 256 characters in length.
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
        # The identifier of the custom field. Create the custom field in advance. For more information, refer to the custom fields module in the console.
        self.field_name = field_name
        # The value of the custom field. The value must comply with the property constraints of the corresponding custom field.
        self.field_value = field_value
        # The operation type for the custom field. Valid values:
        # - add: adds a custom field value to the account.
        # - replace: replaces an existing custom field value of the account. If the custom field value does not exist, the operation is converted to an add operation.
        # - remove: removes the custom field value from the account.
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

