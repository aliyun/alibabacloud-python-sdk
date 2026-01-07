# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseRoleQueryBizRoleByPageResponseBody(DaraModel):
    def __init__(
        self,
        biz_roles: List[main_models.EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles] = None,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.biz_roles = biz_roles
        self.code = code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.biz_roles:
            for v1 in self.biz_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizRoles'] = []
        if self.biz_roles is not None:
            for k1 in self.biz_roles:
                result['BizRoles'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_roles = []
        if m.get('BizRoles') is not None:
            for k1 in m.get('BizRoles'):
                temp_model = main_models.EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles()
                self.biz_roles.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles(DaraModel):
    def __init__(
        self,
        biz_permission_count: int = None,
        biz_permission_name_list: List[str] = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        granted_pk_count: int = None,
        resource_type: str = None,
        src_type: str = None,
    ):
        self.biz_permission_count = biz_permission_count
        self.biz_permission_name_list = biz_permission_name_list
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.granted_pk_count = granted_pk_count
        self.resource_type = resource_type
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_permission_count is not None:
            result['BizPermissionCount'] = self.biz_permission_count

        if self.biz_permission_name_list is not None:
            result['BizPermissionNameList'] = self.biz_permission_name_list

        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc

        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name

        if self.granted_pk_count is not None:
            result['GrantedPkCount'] = self.granted_pk_count

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCount') is not None:
            self.biz_permission_count = m.get('BizPermissionCount')

        if m.get('BizPermissionNameList') is not None:
            self.biz_permission_name_list = m.get('BizPermissionNameList')

        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')

        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')

        if m.get('GrantedPkCount') is not None:
            self.granted_pk_count = m.get('GrantedPkCount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

