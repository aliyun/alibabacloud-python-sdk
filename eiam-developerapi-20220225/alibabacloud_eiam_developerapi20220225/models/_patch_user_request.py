# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class PatchUserRequest(DaraModel):
    def __init__(
        self,
        custom_fields: List[main_models.PatchUserRequestCustomFields] = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        username: str = None,
    ):
        # The extended fields of the account.
        self.custom_fields = custom_fields
        # The display name of the account.
        self.display_name = display_name
        # The email address.
        self.email = email
        # Specifies whether the email address is verified. This field is required if an email address is specified. If you have no special requirement, set this parameter to true.
        self.email_verified = email_verified
        # The mobile number.
        self.phone_number = phone_number
        # Specifies whether the mobile number is verified. This field is required if a mobile number is specified. If you have no special requirement, set this parameter to true.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +. This parameter is required if a mobile number is specified.
        self.phone_region = phone_region
        # The name of the account.
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
        result['customFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['customFields'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified

        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_fields = []
        if m.get('customFields') is not None:
            for k1 in m.get('customFields'):
                temp_model = main_models.PatchUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')

        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')

        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')

        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class PatchUserRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        operation: str = None,
        operator: str = None,
    ):
        # The name of the extended field. For more information about the type and valid values of the extended field, see the detailed description of the extended field in the IDaaS console.
        self.field_name = field_name
        # The value of the extended field.
        self.field_value = field_value
        # The operation to be performed on the field. Valid values:
        # 
        # *   add
        # *   replace If you leave the value of the extended field empty, the replace operation is converted to an add operation.
        # *   remove
        self.operation = operation
        # The type of the operation. This parameter is deprecated. Replace it with operation.
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        if self.operation is not None:
            result['operation'] = self.operation

        if self.operator is not None:
            result['operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        return self

