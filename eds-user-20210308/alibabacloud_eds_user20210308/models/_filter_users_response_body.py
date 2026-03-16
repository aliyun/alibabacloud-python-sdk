# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class FilterUsersResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[main_models.FilterUsersResponseBodyUsers] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the convenience accounts.
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
                temp_model = main_models.FilterUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class FilterUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        desktop_count: int = None,
        desktop_group_count: int = None,
        email: str = None,
        enable_admin_access: bool = None,
        end_user_id: str = None,
        external_info: main_models.FilterUsersResponseBodyUsersExternalInfo = None,
        groups: List[main_models.FilterUsersResponseBodyUsersGroups] = None,
        id: int = None,
        is_tenant_manager: bool = None,
        org_list: List[main_models.FilterUsersResponseBodyUsersOrgList] = None,
        owner_type: str = None,
        password_expire_days: int = None,
        password_expire_rest_days: int = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
        status: int = None,
        support_login_idps: List[main_models.FilterUsersResponseBodyUsersSupportLoginIdps] = None,
        user_set_properties_models: List[main_models.FilterUsersResponseBodyUsersUserSetPropertiesModels] = None,
    ):
        # The date when a convenience account is automatically locked.
        self.auto_lock_time = auto_lock_time
        # The number of cloud desktops that are assigned to the convenience user.
        self.desktop_count = desktop_count
        # The number of cloud desktop pools that are assigned to the convenience user. This value is returned if you set `IncludeDesktopGroupCount` to `true`.
        self.desktop_group_count = desktop_group_count
        # The email address of the convenience user.
        self.email = email
        # Indicates whether the convenience user is a local administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_admin_access = enable_admin_access
        # The username of the convenience user.
        self.end_user_id = end_user_id
        # The additional information about the convenience user.
        self.external_info = external_info
        self.groups = groups
        # The ID of the convenience user.
        self.id = id
        # Indicates whether the convenience user is a tenant administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.is_tenant_manager = is_tenant_manager
        # The organizations to which the user belongs.
        self.org_list = org_list
        # The type of the account ownership.
        # 
        # Valid values:
        # 
        # *   CreateFromManager: administrator-activated
        # *   Normal: user-activated
        self.owner_type = owner_type
        # By default, user account passwords do not expire. However, you can set a validity period between 30 and 365 days. Once the period expires, end users must change their password before they can log on to terminals.
        # 
        # >  The feature is in invitational preview. If you want to use this feature, submit a ticket.
        self.password_expire_days = password_expire_days
        # The number of days remaining until the account password expires.
        self.password_expire_rest_days = password_expire_rest_days
        # The mobile number of the convenience user.
        self.phone = phone
        # The nickname of the convenience user.
        self.real_nick_name = real_nick_name
        # The remarks on the convenience user.
        self.remark = remark
        # The remarks on the convenience account.
        # 
        # Valid values:
        # 
        # *   0: The convenience account is normal.
        # *   9: The convenience account is locked.
        self.status = status
        # The supported identity provider logon methods.
        self.support_login_idps = support_login_idps
        # The information about the properties.
        self.user_set_properties_models = user_set_properties_models

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.org_list:
            for v1 in self.org_list:
                 if v1:
                    v1.validate()
        if self.support_login_idps:
            for v1 in self.support_login_idps:
                 if v1:
                    v1.validate()
        if self.user_set_properties_models:
            for v1 in self.user_set_properties_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time

        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count

        if self.email is not None:
            result['Email'] = self.email

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager

        result['OrgList'] = []
        if self.org_list is not None:
            for k1 in self.org_list:
                result['OrgList'].append(k1.to_map() if k1 else None)

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.password_expire_days is not None:
            result['PasswordExpireDays'] = self.password_expire_days

        if self.password_expire_rest_days is not None:
            result['PasswordExpireRestDays'] = self.password_expire_rest_days

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        result['SupportLoginIdps'] = []
        if self.support_login_idps is not None:
            for k1 in self.support_login_idps:
                result['SupportLoginIdps'].append(k1.to_map() if k1 else None)

        result['UserSetPropertiesModels'] = []
        if self.user_set_properties_models is not None:
            for k1 in self.user_set_properties_models:
                result['UserSetPropertiesModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')

        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExternalInfo') is not None:
            temp_model = main_models.FilterUsersResponseBodyUsersExternalInfo()
            self.external_info = temp_model.from_map(m.get('ExternalInfo'))

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.FilterUsersResponseBodyUsersGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')

        self.org_list = []
        if m.get('OrgList') is not None:
            for k1 in m.get('OrgList'):
                temp_model = main_models.FilterUsersResponseBodyUsersOrgList()
                self.org_list.append(temp_model.from_map(k1))

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('PasswordExpireDays') is not None:
            self.password_expire_days = m.get('PasswordExpireDays')

        if m.get('PasswordExpireRestDays') is not None:
            self.password_expire_rest_days = m.get('PasswordExpireRestDays')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.support_login_idps = []
        if m.get('SupportLoginIdps') is not None:
            for k1 in m.get('SupportLoginIdps'):
                temp_model = main_models.FilterUsersResponseBodyUsersSupportLoginIdps()
                self.support_login_idps.append(temp_model.from_map(k1))

        self.user_set_properties_models = []
        if m.get('UserSetPropertiesModels') is not None:
            for k1 in m.get('UserSetPropertiesModels'):
                temp_model = main_models.FilterUsersResponseBodyUsersUserSetPropertiesModels()
                self.user_set_properties_models.append(temp_model.from_map(k1))

        return self

class FilterUsersResponseBodyUsersUserSetPropertiesModels(DaraModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_type: int = None,
        property_values: List[main_models.FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The property ID.
        self.property_id = property_id
        # The property name.
        self.property_key = property_key
        # The property type.
        self.property_type = property_type
        # The property values.
        self.property_values = property_values
        # The ID of the convenience user that is bound to the property.
        self.user_id = user_id
        # The username of the convenience user that is bound to the property.
        self.user_name = user_name

    def validate(self):
        if self.property_values:
            for v1 in self.property_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        if self.property_key is not None:
            result['PropertyKey'] = self.property_key

        if self.property_type is not None:
            result['PropertyType'] = self.property_type

        result['PropertyValues'] = []
        if self.property_values is not None:
            for k1 in self.property_values:
                result['PropertyValues'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')

        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k1 in m.get('PropertyValues'):
                temp_model = main_models.FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues()
                self.property_values.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues(DaraModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The property value.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        return self

class FilterUsersResponseBodyUsersSupportLoginIdps(DaraModel):
    def __init__(
        self,
        idp_id: str = None,
        idp_name: str = None,
    ):
        # The enterprise identity provider ID.
        self.idp_id = idp_id
        # The enterprise identity provider name.
        self.idp_name = idp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.idp_name is not None:
            result['IdpName'] = self.idp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')

        return self

class FilterUsersResponseBodyUsersOrgList(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        org_name_path: str = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The organization name.
        self.org_name = org_name
        # The organization name path.
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

class FilterUsersResponseBodyUsersGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
    ):
        self.group_id = group_id
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

class FilterUsersResponseBodyUsersExternalInfo(DaraModel):
    def __init__(
        self,
        external_name: str = None,
        job_number: str = None,
    ):
        # The account that is associated with the convenience user.
        self.external_name = external_name
        # The account, student ID, or employee ID that is associated with the convenience user.
        self.job_number = job_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_name is not None:
            result['ExternalName'] = self.external_name

        if self.job_number is not None:
            result['JobNumber'] = self.job_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')

        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')

        return self

