# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class QueryRbacUserRolesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.QueryRbacUserRolesResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.QueryRbacUserRolesResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class QueryRbacUserRolesResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryRbacUserRolesResponseBodyModuleData] = None,
        next: main_models.QueryRbacUserRolesResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next = next
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryRbacUserRolesResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.QueryRbacUserRolesResponseBodyModuleNext()
            self.next = temp_model.from_map(m.get('Next'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryRbacUserRolesResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        org_id: str = None,
        role_id: str = None,
        user_id: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.org_id = org_id
        self.role_id = role_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.id is not None:
            result['Id'] = self.id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryRbacUserRolesResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        org_id: str = None,
        role_id: str = None,
        user_id: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.org_id = org_id
        self.role_id = role_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.id is not None:
            result['Id'] = self.id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

