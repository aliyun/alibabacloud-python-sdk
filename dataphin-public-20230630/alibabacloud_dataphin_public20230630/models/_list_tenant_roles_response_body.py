# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListTenantRolesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        role_list: List[main_models.ListTenantRolesResponseBodyRoleList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.role_list = role_list
        self.success = success

    def validate(self):
        if self.role_list:
            for v1 in self.role_list:
                 if v1:
                    v1.validate()

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

        result['RoleList'] = []
        if self.role_list is not None:
            for k1 in self.role_list:
                result['RoleList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

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

        self.role_list = []
        if m.get('RoleList') is not None:
            for k1 in m.get('RoleList'):
                temp_model = main_models.ListTenantRolesResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTenantRolesResponseBodyRoleList(DaraModel):
    def __init__(
        self,
        auth_json: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        role_desc: str = None,
        role_key: str = None,
        role_name: str = None,
        role_type: str = None,
        status: str = None,
        tenant_id: int = None,
        tenant_type: str = None,
    ):
        self.auth_json = auth_json
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.role_desc = role_desc
        self.role_key = role_key
        self.role_name = role_name
        self.role_type = role_type
        self.status = status
        self.tenant_id = tenant_id
        self.tenant_type = tenant_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_json is not None:
            result['AuthJson'] = self.auth_json

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.role_desc is not None:
            result['RoleDesc'] = self.role_desc

        if self.role_key is not None:
            result['RoleKey'] = self.role_key

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthJson') is not None:
            self.auth_json = m.get('AuthJson')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('RoleDesc') is not None:
            self.role_desc = m.get('RoleDesc')

        if m.get('RoleKey') is not None:
            self.role_key = m.get('RoleKey')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')

        return self

