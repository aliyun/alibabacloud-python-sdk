# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetMyTenantsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant_list: List[main_models.GetMyTenantsResponseBodyTenantList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tenant_list = tenant_list

    def validate(self):
        if self.tenant_list:
            for v1 in self.tenant_list:
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

        if self.success is not None:
            result['Success'] = self.success

        result['TenantList'] = []
        if self.tenant_list is not None:
            for k1 in self.tenant_list:
                result['TenantList'].append(k1.to_map() if k1 else None)

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

        self.tenant_list = []
        if m.get('TenantList') is not None:
            for k1 in m.get('TenantList'):
                temp_model = main_models.GetMyTenantsResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k1))

        return self

class GetMyTenantsResponseBodyTenantList(DaraModel):
    def __init__(
        self,
        delete_time: int = None,
        deleted: bool = None,
        description: str = None,
        id: int = None,
        name: str = None,
        ops_tenant: bool = None,
        owner_id: str = None,
        resource_limited: bool = None,
        tenant_type_list: List[str] = None,
        title_type: str = None,
        visible: bool = None,
    ):
        self.delete_time = delete_time
        self.deleted = deleted
        self.description = description
        self.id = id
        self.name = name
        self.ops_tenant = ops_tenant
        self.owner_id = owner_id
        self.resource_limited = resource_limited
        self.tenant_type_list = tenant_type_list
        self.title_type = title_type
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.ops_tenant is not None:
            result['OpsTenant'] = self.ops_tenant

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_limited is not None:
            result['ResourceLimited'] = self.resource_limited

        if self.tenant_type_list is not None:
            result['TenantTypeList'] = self.tenant_type_list

        if self.title_type is not None:
            result['TitleType'] = self.title_type

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpsTenant') is not None:
            self.ops_tenant = m.get('OpsTenant')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceLimited') is not None:
            self.resource_limited = m.get('ResourceLimited')

        if m.get('TenantTypeList') is not None:
            self.tenant_type_list = m.get('TenantTypeList')

        if m.get('TitleType') is not None:
            self.title_type = m.get('TitleType')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

