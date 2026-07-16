# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeUsersResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[main_models.DescribeUsersResponseBodyUsers] = None,
    ):
        # The token to start the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The details of the convenience accounts.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.DescribeUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class DescribeUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        address: str = None,
        avatar: str = None,
        email: str = None,
        enable_admin_access: bool = None,
        end_user_id: str = None,
        external_name: str = None,
        extras: main_models.DescribeUsersResponseBodyUsersExtras = None,
        groups: List[main_models.DescribeUsersResponseBodyUsersGroups] = None,
        id: int = None,
        is_tenant_manager: bool = None,
        job_number: str = None,
        nick_name: str = None,
        org_id: str = None,
        orgs: List[main_models.DescribeUsersResponseBodyUsersOrgs] = None,
        owner_type: str = None,
        password_expire_days: int = None,
        password_expire_rest_days: int = None,
        phone: str = None,
        properties: List[main_models.DescribeUsersResponseBodyUsersProperties] = None,
        real_nick_name: str = None,
        remark: str = None,
        status: int = None,
        wy_id: str = None,
    ):
        # The work address of the user.
        self.address = address
        # The URL of the user\\"s avatar.
        self.avatar = avatar
        # The email address.
        self.email = email
        # Indicates whether administrator access is enabled.
        self.enable_admin_access = enable_admin_access
        # The end user ID.
        self.end_user_id = end_user_id
        # The name of the user imported from an external system.
        # 
        # > This parameter is for internal use only.
        self.external_name = external_name
        # The extended properties of the user.
        self.extras = extras
        # The user groups to which the convenience account belongs.
        self.groups = groups
        # The ID of the convenience account.
        self.id = id
        # Indicates whether the user is a tenant manager. When you create a convenience account of the `CreateFromManager` type, you must specify a tenant manager. Notifications, such as password resets initiated by an end user from a client, are sent to the tenant manager\\"s email or mobile phone. For more information, see [Create a convenience account](https://help.aliyun.com/document_detail/214472.html).
        self.is_tenant_manager = is_tenant_manager
        # The employee ID.
        self.job_number = job_number
        # The nickname of the user.<br>
        # The value is determined from the following parameters, in order of priority:<br>
        # 
        # - `RealNickName`
        # 
        # - `Remark`
        # 
        # - `EndUserId`
        self.nick_name = nick_name
        # The ID of the organization to which the convenience account belongs.
        # 
        # > This parameter is deprecated and may be removed in a future release.
        self.org_id = org_id
        # The organizations to which the convenience account belongs.
        self.orgs = orgs
        # The type of the convenience account. The account can be activated in one of the following ways:
        # 
        # - Tenant manager-activated: The tenant manager sets the username and password. Notifications such as password resets are sent to the tenant manager\\"s email address or mobile phone.
        # 
        # - End user-activated: The tenant manager sets the username and the end user\\"s email address or mobile phone. Notifications for the end user, such as the initial password for the cloud desktop, are sent to the end user\\"s email address or mobile phone.
        self.owner_type = owner_type
        self.password_expire_days = password_expire_days
        self.password_expire_rest_days = password_expire_rest_days
        # The phone number. This parameter is returned only if a phone number is set.
        self.phone = phone
        # A list of custom properties for the user.
        self.properties = properties
        # The display name of the user.
        self.real_nick_name = real_nick_name
        # The note about the convenience account.
        self.remark = remark
        # The status of the convenience account.
        self.status = status
        # The globally unique ID of the convenience account.
        self.wy_id = wy_id

    def validate(self):
        if self.extras:
            self.extras.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.orgs:
            for v1 in self.orgs:
                 if v1:
                    v1.validate()
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.email is not None:
            result['Email'] = self.email

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.external_name is not None:
            result['ExternalName'] = self.external_name

        if self.extras is not None:
            result['Extras'] = self.extras.to_map()

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager

        if self.job_number is not None:
            result['JobNumber'] = self.job_number

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        result['Orgs'] = []
        if self.orgs is not None:
            for k1 in self.orgs:
                result['Orgs'].append(k1.to_map() if k1 else None)

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.password_expire_days is not None:
            result['PasswordExpireDays'] = self.password_expire_days

        if self.password_expire_rest_days is not None:
            result['PasswordExpireRestDays'] = self.password_expire_rest_days

        if self.phone is not None:
            result['Phone'] = self.phone

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')

        if m.get('Extras') is not None:
            temp_model = main_models.DescribeUsersResponseBodyUsersExtras()
            self.extras = temp_model.from_map(m.get('Extras'))

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeUsersResponseBodyUsersGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')

        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        self.orgs = []
        if m.get('Orgs') is not None:
            for k1 in m.get('Orgs'):
                temp_model = main_models.DescribeUsersResponseBodyUsersOrgs()
                self.orgs.append(temp_model.from_map(k1))

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('PasswordExpireDays') is not None:
            self.password_expire_days = m.get('PasswordExpireDays')

        if m.get('PasswordExpireRestDays') is not None:
            self.password_expire_rest_days = m.get('PasswordExpireRestDays')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.DescribeUsersResponseBodyUsersProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class DescribeUsersResponseBodyUsersProperties(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The property key.
        self.key = key
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeUsersResponseBodyUsersOrgs(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
    ):
        # The ID of the organization.
        self.org_id = org_id
        # The name of the organization.
        self.org_name = org_name
        self.org_name_path = org_name_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        if self.org_name_path is not None:
            result['OrgNamePath'] = self.org_name_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('OrgNamePath') is not None:
            self.org_name_path = m.get('OrgNamePath')

        return self

class DescribeUsersResponseBodyUsersGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
    ):
        # The ID of the user group.
        self.group_id = group_id
        # The name of the user group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class DescribeUsersResponseBodyUsersExtras(DaraModel):
    def __init__(
        self,
        assigned_resource_count: Dict[str, Any] = None,
        resource_policy_list: List[main_models.DescribeUsersResponseBodyUsersExtrasResourcePolicyList] = None,
    ):
        # The number of assigned cloud resources.
        self.assigned_resource_count = assigned_resource_count
        self.resource_policy_list = resource_policy_list

    def validate(self):
        if self.resource_policy_list:
            for v1 in self.resource_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_resource_count is not None:
            result['AssignedResourceCount'] = self.assigned_resource_count

        result['ResourcePolicyList'] = []
        if self.resource_policy_list is not None:
            for k1 in self.resource_policy_list:
                result['ResourcePolicyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedResourceCount') is not None:
            self.assigned_resource_count = m.get('AssignedResourceCount')

        self.resource_policy_list = []
        if m.get('ResourcePolicyList') is not None:
            for k1 in m.get('ResourcePolicyList'):
                temp_model = main_models.DescribeUsersResponseBodyUsersExtrasResourcePolicyList()
                self.resource_policy_list.append(temp_model.from_map(k1))

        return self

class DescribeUsersResponseBodyUsersExtrasResourcePolicyList(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
        policy_name: str = None,
    ):
        self.policy_id = policy_id
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

