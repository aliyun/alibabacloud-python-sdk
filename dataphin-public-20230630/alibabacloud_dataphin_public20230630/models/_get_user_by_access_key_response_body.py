# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetUserByAccessKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_info: main_models.GetUserByAccessKeyResponseBodyUserInfo = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message returned for the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The user information.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetUserByAccessKeyResponseBodyUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class GetUserByAccessKeyResponseBodyUserInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        mail: str = None,
        nick_name: str = None,
        source_type: str = None,
        source_user_id: str = None,
        status: str = None,
        tenant_roles: List[main_models.GetUserByAccessKeyResponseBodyUserInfoTenantRoles] = None,
        user_name: str = None,
    ):
        # The display name of the user.
        self.display_name = display_name
        # The Dataphin user ID.
        self.id = id
        # The email address of the user.
        self.mail = mail
        # The nickname of the user.
        self.nick_name = nick_name
        # The account source type, such as ALIYUN_OAUTH2, PUBLICCLOUD_OAUTH2, BUC, or APSARA.
        self.source_type = source_type
        # The source account ID of the user during SSO integration.
        self.source_user_id = source_user_id
        # The tenant member status. Valid values:
        # - NORMAL: Normal.
        # - DEACTIVATE: Deactivated.
        # - DELETE: Deleted.
        self.status = status
        # The list of tenant-level roles assigned to the AK/SK owner in the current tenant.
        self.tenant_roles = tenant_roles
        # The username of the account.
        self.user_name = user_name

    def validate(self):
        if self.tenant_roles:
            for v1 in self.tenant_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id

        if self.status is not None:
            result['Status'] = self.status

        result['TenantRoles'] = []
        if self.tenant_roles is not None:
            for k1 in self.tenant_roles:
                result['TenantRoles'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tenant_roles = []
        if m.get('TenantRoles') is not None:
            for k1 in m.get('TenantRoles'):
                temp_model = main_models.GetUserByAccessKeyResponseBodyUserInfoTenantRoles()
                self.tenant_roles.append(temp_model.from_map(k1))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetUserByAccessKeyResponseBodyUserInfoTenantRoles(DaraModel):
    def __init__(
        self,
        role_key: str = None,
        role_name: str = None,
    ):
        # The role identifier, such as SUPER_ADMIN or COMMON_USER.
        self.role_key = role_key
        # The role name.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_key is not None:
            result['RoleKey'] = self.role_key

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleKey') is not None:
            self.role_key = m.get('RoleKey')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

