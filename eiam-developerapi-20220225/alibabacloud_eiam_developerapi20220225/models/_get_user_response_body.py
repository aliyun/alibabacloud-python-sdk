# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        account_expire_time: int = None,
        create_time: int = None,
        custom_fields: List[main_models.GetUserResponseBodyCustomFields] = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        groups: List[main_models.GetUserResponseBodyGroups] = None,
        instance_id: str = None,
        lock_expire_time: int = None,
        organizational_units: List[main_models.GetUserResponseBodyOrganizationalUnits] = None,
        password_set: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
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
        # The time when the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.account_expire_time = account_expire_time
        # The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The extended fields of the account.
        self.custom_fields = custom_fields
        # The description of the account.
        self.description = description
        # The display name of the account.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified
        # The groups to which the account belongs.
        self.groups = groups
        # The instance ID.
        self.instance_id = instance_id
        # The time when the account lock expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.lock_expire_time = lock_expire_time
        # The organizational units to which the account belongs.
        self.organizational_units = organizational_units
        # Indicates whether the password is set.
        self.password_set = password_set
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region
        # The ID of the primary organizational unit of the account.
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # The time when the account was registered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.register_time = register_time
        # The status of the account. Valid values: enabled disabled
        self.status = status
        # The time when the account was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The external ID of the account. The external ID can be used to map external data to the data of the account in EIAM of Identity as a Service (IDaaS). By default, the external ID is the account ID.
        # 
        # Note: For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id
        # The account ID.
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
            result['accountExpireTime'] = self.account_expire_time

        if self.create_time is not None:
            result['createTime'] = self.create_time

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

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lock_expire_time is not None:
            result['lockExpireTime'] = self.lock_expire_time

        result['organizationalUnits'] = []
        if self.organizational_units is not None:
            for k1 in self.organizational_units:
                result['organizationalUnits'].append(k1.to_map() if k1 else None)

        if self.password_set is not None:
            result['passwordSet'] = self.password_set

        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number

        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified

        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region

        if self.primary_organizational_unit_id is not None:
            result['primaryOrganizationalUnitId'] = self.primary_organizational_unit_id

        if self.register_time is not None:
            result['registerTime'] = self.register_time

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountExpireTime') is not None:
            self.account_expire_time = m.get('accountExpireTime')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        self.custom_fields = []
        if m.get('customFields') is not None:
            for k1 in m.get('customFields'):
                temp_model = main_models.GetUserResponseBodyCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.GetUserResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lockExpireTime') is not None:
            self.lock_expire_time = m.get('lockExpireTime')

        self.organizational_units = []
        if m.get('organizationalUnits') is not None:
            for k1 in m.get('organizationalUnits'):
                temp_model = main_models.GetUserResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k1))

        if m.get('passwordSet') is not None:
            self.password_set = m.get('passwordSet')

        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')

        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')

        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')

        if m.get('primaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('primaryOrganizationalUnitId')

        if m.get('registerTime') is not None:
            self.register_time = m.get('registerTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')

        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class GetUserResponseBodyOrganizationalUnits(DaraModel):
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
        # Indicates whether the organizational unit is the primary organizational unit.
        self.primary = primary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id

        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name

        if self.primary is not None:
            result['primary'] = self.primary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')

        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')

        if m.get('primary') is not None:
            self.primary = m.get('primary')

        return self

class GetUserResponseBodyGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The group description.
        self.description = description
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        return self

class GetUserResponseBodyCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # The name of the extended field.
        self.field_name = field_name
        # The value of the extended field. Field values are returned as strings regardless of the data types of the fields. For example, true or false is returned for a Boolean field.
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

