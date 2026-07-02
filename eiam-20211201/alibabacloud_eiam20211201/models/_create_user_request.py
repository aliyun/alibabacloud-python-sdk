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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate a parameter value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see References: How to ensure idempotence.
        self.client_token = client_token
        # The list of custom fields.
        self.custom_fields = custom_fields
        # The description. The description can be up to 256 characters in length.
        self.description = description
        # The display name of the account. The display name can be up to 128 characters in length.
        self.display_name = display_name
        # The email address. The email prefix can contain uppercase letters, lowercase letters, digits, periods (.), underscores (_), and hyphens (-). The email address can be up to 128 characters in length.
        self.email = email
        # Specifies whether the email address is verified as a trusted email address. This parameter is required if Email is specified. If no special business requirement exists, set this parameter to true.
        self.email_verified = email_verified
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of organizational unit IDs to which the account belongs. An account can belong to multiple organizational units.
        self.organizational_unit_ids = organizational_unit_ids
        # The password. The password must meet the requirements of the password policy.
        self.password = password
        # The password initialization configuration.
        self.password_initialization_config = password_initialization_config
        # The phone number. The value is a 6 to 15-digit number.
        self.phone_number = phone_number
        # Specifies whether the phone number is verified as a trusted phone number. This parameter is required if PhoneNumber is specified. If no special business requirement exists, set this parameter to true.
        self.phone_number_verified = phone_number_verified
        # The phone region code. The value is a 1 to 6-digit number and does not include a plus sign (+).
        self.phone_region = phone_region
        # The ID of the primary organizational unit.
        # 
        # This parameter is required.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The external ID of the account. This parameter is used to associate the account with an external system. The value can be up to 128 characters in length. If this parameter is not specified, the account ID is used by default.
        self.user_external_id = user_external_id
        # The username. The username can contain letters, digits, underscores (_), periods (.), at signs (@), and hyphens (-). The username can be up to 256 characters in length.
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
        # The forced password change status. By default, this feature is not enabled. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.password_forced_update_status = password_forced_update_status
        # The priority of the password initialization policy. By default, this parameter does not take effect. Valid values:
        # - global: The global policy policy priority. The instance-level password initialization policy is used, and the password initialization policy specified in this request does not take effect. For more information, refer to the password initialization policy in password-related policies.
        # - custom: The custom policy policy priority. The password initialization policy defined in this request is used, including whether to enable forced password change, the password initialization method, and the notification channel.
        self.password_initialization_policy_priority = password_initialization_policy_priority
        # The password initialization method. Valid values:
        # - random: random.
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
        # The identifier of the custom field. Create the custom field in advance. For more information, refer to the custom fields module in the console.
        self.field_name = field_name
        # The value of the custom field. The value must comply with the attribute constraints of the corresponding custom field.
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

