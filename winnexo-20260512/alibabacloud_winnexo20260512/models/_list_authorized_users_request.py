# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedUsersRequest(DaraModel):
    def __init__(
        self,
        grantee_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        permission: str = None,
        tenant_id: str = None,
    ):
        # 筛选类型：USER / USER_GROUP / 不传则返回全部
        self.grantee_type = grantee_type
        # 搜索关键词，按用户名或组名模糊匹配
        self.keyword = keyword
        # 数字员工名称
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 权限类型过滤：USE=使用权限 / MANAGE=管理权限
        self.permission = permission
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.permission is not None:
            result['permission'] = self.permission

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

