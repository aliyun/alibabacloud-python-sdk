# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeUsersInGroupResponseBody(DaraModel):
    def __init__(
        self,
        end_users: List[main_models.DescribeUsersInGroupResponseBodyEndUsers] = None,
        next_token: str = None,
        online_users_count: int = None,
        request_id: str = None,
        user_group_name: str = None,
        user_ou_path: str = None,
        users_count: int = None,
    ):
        # The authorized users.
        self.end_users = end_users
        # The token that is used to start the next query.
        self.next_token = next_token
        # The total number of authorized users that are connected to cloud computers of the cloud computer share.
        self.online_users_count = online_users_count
        # The ID of the request.
        self.request_id = request_id
        self.user_group_name = user_group_name
        self.user_ou_path = user_ou_path
        # The total number of authorized users of the cloud computer share.
        self.users_count = users_count

    def validate(self):
        if self.end_users:
            for v1 in self.end_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EndUsers'] = []
        if self.end_users is not None:
            for k1 in self.end_users:
                result['EndUsers'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.online_users_count is not None:
            result['OnlineUsersCount'] = self.online_users_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        if self.user_ou_path is not None:
            result['UserOuPath'] = self.user_ou_path

        if self.users_count is not None:
            result['UsersCount'] = self.users_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.end_users = []
        if m.get('EndUsers') is not None:
            for k1 in m.get('EndUsers'):
                temp_model = main_models.DescribeUsersInGroupResponseBodyEndUsers()
                self.end_users.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OnlineUsersCount') is not None:
            self.online_users_count = m.get('OnlineUsersCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        if m.get('UserOuPath') is not None:
            self.user_ou_path = m.get('UserOuPath')

        if m.get('UsersCount') is not None:
            self.users_count = m.get('UsersCount')

        return self

class DescribeUsersInGroupResponseBodyEndUsers(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        display_name: str = None,
        display_name_new: str = None,
        end_user_email: str = None,
        end_user_id: str = None,
        end_user_name: str = None,
        end_user_phone: str = None,
        end_user_remark: str = None,
        end_user_type: str = None,
        external_info: main_models.DescribeUsersInGroupResponseBodyEndUsersExternalInfo = None,
        user_desktop_id: str = None,
        user_principal_name: str = None,
        user_set_properties_models: List[main_models.DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels] = None,
    ):
        # The connection status.
        # 
        # Valid values:
        # 
        # *   0: disconnected
        # *   1: connecting
        self.connection_status = connection_status
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The display name of the enterprise AD account.
        self.display_name = display_name
        self.display_name_new = display_name_new
        # The email address of the authorized user.
        self.end_user_email = end_user_email
        # The ID of the authorized user.
        self.end_user_id = end_user_id
        # The username of the authorized user.
        self.end_user_name = end_user_name
        # The mobile number of the authorized user.
        self.end_user_phone = end_user_phone
        # The remarks.
        self.end_user_remark = end_user_remark
        # The user account type.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience account
        # *   AD_CONNECTOR: enterprise Active Directory (AD) account
        self.end_user_type = end_user_type
        # The appended information.
        self.external_info = external_info
        # The ID of the cloud computer that is used by the user.
        self.user_desktop_id = user_desktop_id
        self.user_principal_name = user_principal_name
        # Details about the seats of users.
        self.user_set_properties_models = user_set_properties_models

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.user_set_properties_models:
            for v1 in self.user_set_properties_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_new is not None:
            result['DisplayNameNew'] = self.display_name_new

        if self.end_user_email is not None:
            result['EndUserEmail'] = self.end_user_email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name

        if self.end_user_phone is not None:
            result['EndUserPhone'] = self.end_user_phone

        if self.end_user_remark is not None:
            result['EndUserRemark'] = self.end_user_remark

        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type

        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()

        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        result['UserSetPropertiesModels'] = []
        if self.user_set_properties_models is not None:
            for k1 in self.user_set_properties_models:
                result['UserSetPropertiesModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameNew') is not None:
            self.display_name_new = m.get('DisplayNameNew')

        if m.get('EndUserEmail') is not None:
            self.end_user_email = m.get('EndUserEmail')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')

        if m.get('EndUserPhone') is not None:
            self.end_user_phone = m.get('EndUserPhone')

        if m.get('EndUserRemark') is not None:
            self.end_user_remark = m.get('EndUserRemark')

        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')

        if m.get('ExternalInfo') is not None:
            temp_model = main_models.DescribeUsersInGroupResponseBodyEndUsersExternalInfo()
            self.external_info = temp_model.from_map(m.get('ExternalInfo'))

        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        self.user_set_properties_models = []
        if m.get('UserSetPropertiesModels') is not None:
            for k1 in m.get('UserSetPropertiesModels'):
                temp_model = main_models.DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels()
                self.user_set_properties_models.append(temp_model.from_map(k1))

        return self

class DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels(DaraModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_type: int = None,
        property_values: List[main_models.DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The property ID.
        self.property_id = property_id
        # The property name.
        self.property_key = property_key
        # The property type.
        # 
        # Valid values:
        # 
        # *   1: system property
        # *   2: custom property
        self.property_type = property_type
        # Details about property values.
        self.property_values = property_values
        # The user ID.
        self.user_id = user_id
        # The username.
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
                temp_model = main_models.DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues()
                self.property_values.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues(DaraModel):
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

class DescribeUsersInGroupResponseBodyEndUsersExternalInfo(DaraModel):
    def __init__(
        self,
        external_name: str = None,
        job_number: str = None,
    ):
        # The external name.
        self.external_name = external_name
        # The employee ID.
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

