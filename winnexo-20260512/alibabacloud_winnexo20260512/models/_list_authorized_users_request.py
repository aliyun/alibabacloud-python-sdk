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
        # The filter type. Valid values: USER, USER_GROUP. If not specified, all types are returned.
        self.grantee_type = grantee_type
        # The search keyword.
        self.keyword = keyword
        # The name of the digital employee.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # Permission
        self.permission = permission
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
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

