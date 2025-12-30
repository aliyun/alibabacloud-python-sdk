# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceAuthorizedAppsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServiceAuthorizedAppsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

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

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDataServiceAuthorizedAppsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceAuthorizedAppsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        authorized_app_list: List[main_models.ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppList] = None,
        total_count: int = None,
    ):
        self.authorized_app_list = authorized_app_list
        self.total_count = total_count

    def validate(self):
        if self.authorized_app_list:
            for v1 in self.authorized_app_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizedAppList'] = []
        if self.authorized_app_list is not None:
            for k1 in self.authorized_app_list:
                result['AuthorizedAppList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_app_list = []
        if m.get('AuthorizedAppList') is not None:
            for k1 in m.get('AuthorizedAppList'):
                temp_model = main_models.ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppList()
                self.authorized_app_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppList(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        apply_user_id: str = None,
        apply_user_name: str = None,
        expire_date: str = None,
        id: int = None,
        is_project_manager: bool = None,
        owner: str = None,
        owner_user_name: str = None,
        privilege_account: int = None,
        privilege_type: int = None,
        project_id: int = None,
        project_name: str = None,
        real_has_owner_privilege: bool = None,
        real_has_privilege: bool = None,
        remark_for_debug_list: List[main_models.ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppListRemarkForDebugList] = None,
        revocable: bool = None,
        revocable_detail: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.apply_user_id = apply_user_id
        self.apply_user_name = apply_user_name
        self.expire_date = expire_date
        self.id = id
        self.is_project_manager = is_project_manager
        self.owner = owner
        self.owner_user_name = owner_user_name
        self.privilege_account = privilege_account
        self.privilege_type = privilege_type
        self.project_id = project_id
        self.project_name = project_name
        self.real_has_owner_privilege = real_has_owner_privilege
        self.real_has_privilege = real_has_privilege
        self.remark_for_debug_list = remark_for_debug_list
        self.revocable = revocable
        self.revocable_detail = revocable_detail

    def validate(self):
        if self.remark_for_debug_list:
            for v1 in self.remark_for_debug_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.apply_user_id is not None:
            result['ApplyUserId'] = self.apply_user_id

        if self.apply_user_name is not None:
            result['ApplyUserName'] = self.apply_user_name

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.id is not None:
            result['Id'] = self.id

        if self.is_project_manager is not None:
            result['IsProjectManager'] = self.is_project_manager

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_user_name is not None:
            result['OwnerUserName'] = self.owner_user_name

        if self.privilege_account is not None:
            result['PrivilegeAccount'] = self.privilege_account

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.real_has_owner_privilege is not None:
            result['RealHasOwnerPrivilege'] = self.real_has_owner_privilege

        if self.real_has_privilege is not None:
            result['RealHasPrivilege'] = self.real_has_privilege

        result['RemarkForDebugList'] = []
        if self.remark_for_debug_list is not None:
            for k1 in self.remark_for_debug_list:
                result['RemarkForDebugList'].append(k1.to_map() if k1 else None)

        if self.revocable is not None:
            result['Revocable'] = self.revocable

        if self.revocable_detail is not None:
            result['RevocableDetail'] = self.revocable_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ApplyUserId') is not None:
            self.apply_user_id = m.get('ApplyUserId')

        if m.get('ApplyUserName') is not None:
            self.apply_user_name = m.get('ApplyUserName')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsProjectManager') is not None:
            self.is_project_manager = m.get('IsProjectManager')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerUserName') is not None:
            self.owner_user_name = m.get('OwnerUserName')

        if m.get('PrivilegeAccount') is not None:
            self.privilege_account = m.get('PrivilegeAccount')

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RealHasOwnerPrivilege') is not None:
            self.real_has_owner_privilege = m.get('RealHasOwnerPrivilege')

        if m.get('RealHasPrivilege') is not None:
            self.real_has_privilege = m.get('RealHasPrivilege')

        self.remark_for_debug_list = []
        if m.get('RemarkForDebugList') is not None:
            for k1 in m.get('RemarkForDebugList'):
                temp_model = main_models.ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppListRemarkForDebugList()
                self.remark_for_debug_list.append(temp_model.from_map(k1))

        if m.get('Revocable') is not None:
            self.revocable = m.get('Revocable')

        if m.get('RevocableDetail') is not None:
            self.revocable_detail = m.get('RevocableDetail')

        return self

class ListDataServiceAuthorizedAppsResponseBodyPageResultAuthorizedAppListRemarkForDebugList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

