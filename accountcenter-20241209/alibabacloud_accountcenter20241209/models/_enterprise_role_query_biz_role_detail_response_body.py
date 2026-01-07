# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseRoleQueryBizRoleDetailResponseBody(DaraModel):
    def __init__(
        self,
        biz_role_detail: main_models.EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_role_detail = biz_role_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.biz_role_detail:
            self.biz_role_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_role_detail is not None:
            result['BizRoleDetail'] = self.biz_role_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleDetail') is not None:
            temp_model = main_models.EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail()
            self.biz_role_detail = temp_model.from_map(m.get('BizRoleDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail(DaraModel):
    def __init__(
        self,
        biz_permissions: List[main_models.EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions] = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        resource_type: str = None,
        src_type: str = None,
    ):
        self.biz_permissions = biz_permissions
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.resource_type = resource_type
        self.src_type = src_type

    def validate(self):
        if self.biz_permissions:
            for v1 in self.biz_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizPermissions'] = []
        if self.biz_permissions is not None:
            for k1 in self.biz_permissions:
                result['BizPermissions'].append(k1.to_map() if k1 else None)

        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc

        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_permissions = []
        if m.get('BizPermissions') is not None:
            for k1 in m.get('BizPermissions'):
                temp_model = main_models.EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions()
                self.biz_permissions.append(temp_model.from_map(k1))

        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')

        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

class EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions(DaraModel):
    def __init__(
        self,
        biz_permission_code: str = None,
        biz_permission_desc: str = None,
        biz_permission_name: str = None,
    ):
        self.biz_permission_code = biz_permission_code
        self.biz_permission_desc = biz_permission_desc
        self.biz_permission_name = biz_permission_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_permission_code is not None:
            result['BizPermissionCode'] = self.biz_permission_code

        if self.biz_permission_desc is not None:
            result['BizPermissionDesc'] = self.biz_permission_desc

        if self.biz_permission_name is not None:
            result['BizPermissionName'] = self.biz_permission_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCode') is not None:
            self.biz_permission_code = m.get('BizPermissionCode')

        if m.get('BizPermissionDesc') is not None:
            self.biz_permission_desc = m.get('BizPermissionDesc')

        if m.get('BizPermissionName') is not None:
            self.biz_permission_name = m.get('BizPermissionName')

        return self

