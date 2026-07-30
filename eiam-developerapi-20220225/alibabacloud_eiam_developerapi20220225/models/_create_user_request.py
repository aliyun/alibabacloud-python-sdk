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
        # A list of custom fields for the account.
        self.custom_fields = custom_fields
        # The account description. The maximum length is 256 characters.
        self.description = description
        # The display name. The maximum length is 128 characters.
        self.display_name = display_name
        # The email address. The local-part of the address can contain uppercase and lowercase letters, digits, periods (`.`), underscores (`_`), and hyphens (`-`). The maximum length is 128 characters.
        self.email = email
        # Specifies whether the email is verified. This parameter is required if `email` is set. Typically, set this to `true`.
        self.email_verified = email_verified
        # The account password. For password complexity rules, see the password policy in the IDaaS console.
        self.password = password
        # The password initialization configuration.
        self.password_initialization_config = password_initialization_config
        # The account phone number. It must be 6 to 15 digits long.
        self.phone_number = phone_number
        # Specifies whether the phone number is verified. This parameter is required if `phoneNumber` is set. Typically, set this to `true`.
        self.phone_number_verified = phone_number_verified
        # The phone region code. For example, the code for the Chinese mainland is `86`. Do not include a `00` prefix or a plus sign (`+`). This parameter is required if `phoneNumber` is set.
        self.phone_region = phone_region
        # The ID of the primary organizational unit.
        # 
        # This parameter is required.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The external user ID, used to associate the account with an external system. The maximum length is 128 characters. If unspecified, it defaults to the account ID.
        self.user_external_id = user_external_id
        # The username. It can contain letters, digits, and the following special characters: underscore (`_`), period (`.`), at sign (`@`), and hyphen (`-`). The maximum length is 256 characters.
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
        # The password forced update status. By default, this feature is disabled. Valid values:
        # 
        # - `enabled`: Enables the feature.
        # 
        # - `disabled`: Disables the feature.
        self.password_forced_update_status = password_forced_update_status
        # The priority of the password initialization policy. Valid values:
        # 
        # - `global`: Uses the instance-level password initialization policy and ignores the custom settings in this request. For more information, see the password initialization policy configuration in the IDaaS console.
        # 
        # - `custom`: Uses the custom password initialization policy defined in this request. This includes settings for forced password updates, the initialization type, and notification channels.
        self.password_initialization_policy_priority = password_initialization_policy_priority
        # The password initialization type. Valid values:
        # 
        # - `random`: A randomly generated password.
        self.password_initialization_type = password_initialization_type
        # The user notification channels. Valid values:
        # 
        # - `email`: Email
        # 
        # - `sms`: SMS
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
        # The name of the custom field. You can view the field\\"s data type and value range in the IDaaS console.
        self.field_name = field_name
        # The value of the custom field.
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

