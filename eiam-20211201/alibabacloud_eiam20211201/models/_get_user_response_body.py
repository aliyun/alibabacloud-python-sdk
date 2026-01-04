# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserResponseBodyUser = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The data object of the account.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.GetUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        account_expire_time: int = None,
        create_time: int = None,
        custom_fields: List[main_models.GetUserResponseBodyUserCustomFields] = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        groups: List[main_models.GetUserResponseBodyUserGroups] = None,
        instance_id: str = None,
        lock_expire_time: int = None,
        organizational_units: List[main_models.GetUserResponseBodyUserOrganizationalUnits] = None,
        password_expire_time: int = None,
        password_set: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        preferred_language: str = None,
        primary_organizational_unit_id: str = None,
        register_time: int = None,
        status: str = None,
        update_time: int = None,
        user_external_id: str = None,
        user_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
        username: str = None,
    ):
        # The time when the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.account_expire_time = account_expire_time
        # The time when the account was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The list of custom fields that describe the account.
        self.custom_fields = custom_fields
        # The description of the account.
        self.description = description
        # The display name of the account.
        self.display_name = display_name
        # The email address of the user who owns the account.
        self.email = email
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified
        # The organizational units to which the account belongs.
        self.groups = groups
        # The ID of the instance
        self.instance_id = instance_id
        # The time when the account lock expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.lock_expire_time = lock_expire_time
        # The organizational units to which the account belongs.
        self.organizational_units = organizational_units
        # The time when the password of the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   If the value -1 is returned, the password does not expire.
        # *   If no value is returned, the password does not expire.
        # *   If a UNIX timestamp is returned, the password expires at the indicated point of time.
        self.password_expire_time = password_expire_time
        # Indicates whether a password is set.
        self.password_set = password_set
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region
        # Preferred language
        self.preferred_language = preferred_language
        # The ID of the primary organizational unit to which the account belongs.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The time when the account was registered. This value is a UNIX timestamp. Unit: milliseconds.
        self.register_time = register_time
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status
        # The time when the account was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM. By default, the external ID is the account ID.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id
        # The ID of the account.
        self.user_id = user_id
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type
        # The username of the account.
        self.username = username

    def validate(self):
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.organizational_units:
            for v1 in self.organizational_units:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_expire_time is not None:
            result['AccountExpireTime'] = self.account_expire_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lock_expire_time is not None:
            result['LockExpireTime'] = self.lock_expire_time

        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k1 in self.organizational_units:
                result['OrganizationalUnits'].append(k1.to_map() if k1 else None)

        if self.password_expire_time is not None:
            result['PasswordExpireTime'] = self.password_expire_time

        if self.password_set is not None:
            result['PasswordSet'] = self.password_set

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region

        if self.preferred_language is not None:
            result['PreferredLanguage'] = self.preferred_language

        if self.primary_organizational_unit_id is not None:
            result['PrimaryOrganizationalUnitId'] = self.primary_organizational_unit_id

        if self.register_time is not None:
            result['RegisterTime'] = self.register_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountExpireTime') is not None:
            self.account_expire_time = m.get('AccountExpireTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.GetUserResponseBodyUserCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.GetUserResponseBodyUserGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LockExpireTime') is not None:
            self.lock_expire_time = m.get('LockExpireTime')

        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k1 in m.get('OrganizationalUnits'):
                temp_model = main_models.GetUserResponseBodyUserOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k1))

        if m.get('PasswordExpireTime') is not None:
            self.password_expire_time = m.get('PasswordExpireTime')

        if m.get('PasswordSet') is not None:
            self.password_set = m.get('PasswordSet')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')

        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')

        if m.get('PreferredLanguage') is not None:
            self.preferred_language = m.get('PreferredLanguage')

        if m.get('PrimaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('PrimaryOrganizationalUnitId')

        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')

        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetUserResponseBodyUserOrganizationalUnits(DaraModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        primary: bool = None,
    ):
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name
        # Indicates whether the organization is the primary organization.
        self.primary = primary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name

        if self.primary is not None:
            result['Primary'] = self.primary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        return self

class GetUserResponseBodyUserGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The description of the organizational unit.
        self.description = description
        # The ID of the organizational unit.
        self.group_id = group_id
        # The name of the organizational unit.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class GetUserResponseBodyUserCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # The identifier of the custom field.
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

