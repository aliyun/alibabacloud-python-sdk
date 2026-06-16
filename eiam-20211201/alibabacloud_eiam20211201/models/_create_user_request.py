# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        custom_fields: List[main_models.CreateUserRequestCustomFields] = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        instance_id: str = None,
        organizational_unit_ids: List[str] = None,
        password: str = None,
        password_initialization_config: main_models.CreateUserRequestPasswordInitializationConfig = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        primary_organizational_unit_id: str = None,
        user_external_id: str = None,
        username: str = None,
    ):
        # A client-provided token to ensure the idempotence of the request. This value must be unique for each request. The token can contain only ASCII characters and must be no more than 64 characters long. For more information, see [How to ensure idempotence](~~~/doc-en/6a938a5b-2402-4c9d-b235-3733a1f813c9.dita).
        self.client_token = client_token
        # The list of custom fields.
        self.custom_fields = custom_fields
        # The description. The maximum length is 256 characters.
        self.description = description
        # The display name. The maximum length is 128 characters.
        self.display_name = display_name
        # The email address. The local part of the address can contain uppercase letters, lowercase letters, digits, periods (.), underscores (_), or hyphens (-). The maximum length is 128 characters.
        self.email = email
        # Indicates whether the email address is verified. A verified address is considered trusted. This parameter is required if you specify the `Email` parameter. For typical use, set this to `true`.
        self.email_verified = email_verified
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A list of subordinate organizational unit IDs. A user can belong to multiple organizational units.
        self.organizational_unit_ids = organizational_unit_ids
        # The password. The format must comply with the password policy.
        self.password = password
        # The settings for the password initialization policy.
        self.password_initialization_config = password_initialization_config
        # The phone number. It must be 6 to 15 digits long.
        self.phone_number = phone_number
        # Indicates whether the phone number is verified. A verified number is considered trusted. This parameter is required if you specify the `PhoneNumber` parameter. For typical use, set this to `true`.
        self.phone_number_verified = phone_number_verified
        # The country code. It must contain 1 to 6 digits and must not include the plus sign (+).
        self.phone_region = phone_region
        # The ID of the primary organizational unit.
        # 
        # This parameter is required.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The external ID for associating the user with an external system. The maximum length is 128 characters. If this parameter is not specified, its value defaults to the system-generated user ID.
        self.user_external_id = user_external_id
        # The username. It can contain letters, digits, and the following special characters: underscores (_), periods (.), at signs (@), and hyphens (-). The maximum length is 256 characters.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        if self.password is not None:
            result['Password'] = self.password

        if self.password_initialization_config is not None:
            result['PasswordInitializationConfig'] = self.password_initialization_config.to_map()

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region

        if self.primary_organizational_unit_id is not None:
            result['PrimaryOrganizationalUnitId'] = self.primary_organizational_unit_id

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.CreateUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInitializationConfig') is not None:
            temp_model = main_models.CreateUserRequestPasswordInitializationConfig()
            self.password_initialization_config = temp_model.from_map(m.get('PasswordInitializationConfig'))

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')

        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')

        if m.get('PrimaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('PrimaryOrganizationalUnitId')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class CreateUserRequestPasswordInitializationConfig(DaraModel):
    def __init__(
        self,
        password_forced_update_status: str = None,
        password_initialization_policy_priority: str = None,
        password_initialization_type: str = None,
        user_notification_channels: List[str] = None,
    ):
        # The status of forced password update. This setting is disabled by default. Valid values:
        # 
        # - `enabled`: Enables forced password updates.
        # 
        # - `disabled`: Disables forced password updates.
        self.password_forced_update_status = password_forced_update_status
        # The priority of the password initialization policy. This setting is disabled by default. Valid values:
        # 
        # - `global`: The service uses the instance-level password initialization policy and ignores the policy specified in this request. For more information, see the password initialization policy settings.
        # 
        # - `custom`: The service uses the password initialization policy defined in this request. This includes the forced password update setting, the password initialization method, and the notification channels.
        self.password_initialization_policy_priority = password_initialization_policy_priority
        # The password initialization type. Valid values:
        # 
        # - `random`: The system generates a random password.
        self.password_initialization_type = password_initialization_type
        # The list of password notification channels.
        self.user_notification_channels = user_notification_channels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status

        if self.password_initialization_policy_priority is not None:
            result['PasswordInitializationPolicyPriority'] = self.password_initialization_policy_priority

        if self.password_initialization_type is not None:
            result['PasswordInitializationType'] = self.password_initialization_type

        if self.user_notification_channels is not None:
            result['UserNotificationChannels'] = self.user_notification_channels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')

        if m.get('PasswordInitializationPolicyPriority') is not None:
            self.password_initialization_policy_priority = m.get('PasswordInitializationPolicyPriority')

        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')

        if m.get('UserNotificationChannels') is not None:
            self.user_notification_channels = m.get('UserNotificationChannels')

        return self

class CreateUserRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # The identifier of the custom field. You must create this field in the console before you can use it in a request. For more information, see the Custom Fields module in the console.
        self.field_name = field_name
        # The value of the custom field. This value must comply with the constraints defined for the corresponding custom field.
        self.field_value = field_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        return self

