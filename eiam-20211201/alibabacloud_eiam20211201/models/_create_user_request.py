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
        # The password initialization method. Set the value to random,
        # 
        # *   which indicates that the password is randomly generated.
        self.client_token = client_token
        # The custom extended fields.
        self.custom_fields = custom_fields
        # The description of the organization. The value can be up to 256 characters in length.
        self.description = description
        # The display name of the account. The display name can be up to 64 characters in length.
        self.display_name = display_name
        # The name of the account. The name can be up to 64 characters in length and can contain letters, digits, underscores (_), periods (.), at signs (@), and hyphens (-).
        self.email = email
        # The description of the account. The description can be up to 256 characters in length.
        self.email_verified = email_verified
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the mobile phone number is a trusted mobile phone number. This parameter is required if the PhoneNumber parameter is specified. If you have no special business requirements, set this parameter to true.
        self.organizational_unit_ids = organizational_unit_ids
        # The password of the account. For more information,view the password policyof the instanceinthe IDaaS console.
        self.password = password
        # The configurations for password initialization.
        self.password_initialization_config = password_initialization_config
        # The ID of the account.
        self.phone_number = phone_number
        # The email address of the user who owns the account. The email address prefix can contain letters, digits, underscores (_), periods (.), and hyphens (-).
        self.phone_number_verified = phone_number_verified
        # The IDs of organizational units to which the account belongs. An account can belong to multiple organizational units.
        self.phone_region = phone_region
        # 主组织ID。
        # 
        # This parameter is required.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The display name of the account. The display name can be up to 64 characters in length.
        self.user_external_id = user_external_id
        # The name of the extended field. You must create the extended field in advance. To create an extended field, log on to the IDaaS console. In the left-side navigation pane, choose Accounts > Extended Fields, and then click Create Field on the Extended Fields page.
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
        # Specifies whether to forcibly change the password status. Default value: disabled. Valid values:
        # *   enabled:forcibly changes the password status.
        # * disabled: does not forcibly change the password status.
        self.password_forced_update_status = password_forced_update_status
        # The priority of the password initialization policy. By default, this parameter does not take effect. Valid values:
        # *   global:The password initialization policy globally takes effect.
        # *   custom: The password initialization policy takes effect based on custom settings.
        self.password_initialization_policy_priority = password_initialization_policy_priority
        # The password initialization method. Set the value to random,
        # *   whichindicates that the password is randomly generated.
        self.password_initialization_type = password_initialization_type
        # The value of the extended field. The value follows the limits on the properties of the extended field.
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
        # The name of the extended field. You must create the extended field in advance. To create an extended field, log on to the IDaaS console. In the left-side navigation pane, choose Accounts > Extended Fields, and then click Create Field on the Extended Fields page.
        self.field_name = field_name
        # The value of the extended field. The value follows the limits on the properties of the extended field.
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

