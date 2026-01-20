# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        custom_fields: List[main_models.CreateUserRequestCustomFields] = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        password: str = None,
        password_initialization_config: main_models.CreateUserRequestPasswordInitializationConfig = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        primary_organizational_unit_id: str = None,
        user_external_id: str = None,
        username: str = None,
    ):
        # Custom fields
        self.custom_fields = custom_fields
        # The description of the account. The description can be up to 256 characters in length.
        self.description = description
        # The display name of the account. The display name can be up to 64 characters in length.
        self.display_name = display_name
        # The email address of the user who owns the account.
        self.email = email
        # Indicates whether the email address is verified. This field is required if an email address is specified. If you have no special requirement, set this parameter to true.
        self.email_verified = email_verified
        # The password of the account. For information about the password rules, go to the Create User panel in the Identity as a Service (IDaaS) console.
        self.password = password
        # Configure the initial password
        self.password_initialization_config = password_initialization_config
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # Indicates whether the mobile number is verified. This field is required if a mobile number is specified. If you have no special requirement, set this parameter to true.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +. This parameter is required if a mobile number is specified.
        self.phone_region = phone_region
        # The ID of the primary organizational unit.
        # 
        # This parameter is required.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The external ID of the account. The external ID can be used to map external data to the data of the account in EIAM of Identity as a Service (IDaaS). By default, the external ID is the account ID.
        self.user_external_id = user_external_id
        # The username of the account.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()
        if self.password_initialization_config:
            self.password_initialization_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['customFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['customFields'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified

        if self.password is not None:
            result['password'] = self.password

        if self.password_initialization_config is not None:
            result['passwordInitializationConfig'] = self.password_initialization_config.to_map()

        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region

        if self.primary_organizational_unit_id is not None:
            result['primaryOrganizationalUnitId'] = self.primary_organizational_unit_id

        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_fields = []
        if m.get('customFields') is not None:
            for k1 in m.get('customFields'):
                temp_model = main_models.CreateUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('passwordInitializationConfig') is not None:
            temp_model = main_models.CreateUserRequestPasswordInitializationConfig()
            self.password_initialization_config = temp_model.from_map(m.get('passwordInitializationConfig'))

        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')

        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')

        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')

        if m.get('primaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('primaryOrganizationalUnitId')

        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class CreateUserRequestPasswordInitializationConfig(DaraModel):
    def __init__(
        self,
        password_forced_update_status: str = None,
        password_initialization_policy_priority: str = None,
        password_initialization_type: str = None,
        user_notification_channels: List[str] = None,
    ):
        # Password  forced update
        self.password_forced_update_status = password_forced_update_status
        # Password policy
        self.password_initialization_policy_priority = password_initialization_policy_priority
        # Password Initialization Type
        self.password_initialization_type = password_initialization_type
        # User Notification Channels
        self.user_notification_channels = user_notification_channels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_forced_update_status is not None:
            result['passwordForcedUpdateStatus'] = self.password_forced_update_status

        if self.password_initialization_policy_priority is not None:
            result['passwordInitializationPolicyPriority'] = self.password_initialization_policy_priority

        if self.password_initialization_type is not None:
            result['passwordInitializationType'] = self.password_initialization_type

        if self.user_notification_channels is not None:
            result['userNotificationChannels'] = self.user_notification_channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passwordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('passwordForcedUpdateStatus')

        if m.get('passwordInitializationPolicyPriority') is not None:
            self.password_initialization_policy_priority = m.get('passwordInitializationPolicyPriority')

        if m.get('passwordInitializationType') is not None:
            self.password_initialization_type = m.get('passwordInitializationType')

        if m.get('userNotificationChannels') is not None:
            self.user_notification_channels = m.get('userNotificationChannels')

        return self



class CreateUserRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # Field name
        self.field_name = field_name
        # Filed value
        self.field_value = field_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        return self

