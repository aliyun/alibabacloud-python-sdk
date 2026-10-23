# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAppResourcePermissionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListAppResourcePermissionRecordsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The authorization records on the current page.
        self.items = items
        # The error message. This parameter is empty if the request is successful.
        self.message = message
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAppResourcePermissionRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAppResourcePermissionRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        expire_at: str = None,
        granted_by: str = None,
        grantee_id: str = None,
        grantee_name: str = None,
        grantee_tenant_id: str = None,
        grantee_type: str = None,
        permission: str = None,
        permission_id: int = None,
        resource_key: str = None,
        resource_type: str = None,
        updated_at: str = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The expiration time.
        self.expire_at = expire_at
        # The platform user ID of the grantor.
        self.granted_by = granted_by
        # The grantee ID.
        self.grantee_id = grantee_id
        # The grantee name.
        self.grantee_name = grantee_name
        # The ID of the tenant to which the cross-tenant user belongs.
        self.grantee_tenant_id = grantee_tenant_id
        # The grantee type.
        self.grantee_type = grantee_type
        # The permission.
        self.permission = permission
        # The ID of the permission record.
        self.permission_id = permission_id
        # The resource key.
        self.resource_key = resource_key
        # The resource type.
        self.resource_type = resource_type
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.granted_by is not None:
            result['grantedBy'] = self.granted_by

        if self.grantee_id is not None:
            result['granteeId'] = self.grantee_id

        if self.grantee_name is not None:
            result['granteeName'] = self.grantee_name

        if self.grantee_tenant_id is not None:
            result['granteeTenantId'] = self.grantee_tenant_id

        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.permission is not None:
            result['permission'] = self.permission

        if self.permission_id is not None:
            result['permissionId'] = self.permission_id

        if self.resource_key is not None:
            result['resourceKey'] = self.resource_key

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('grantedBy') is not None:
            self.granted_by = m.get('grantedBy')

        if m.get('granteeId') is not None:
            self.grantee_id = m.get('granteeId')

        if m.get('granteeName') is not None:
            self.grantee_name = m.get('granteeName')

        if m.get('granteeTenantId') is not None:
            self.grantee_tenant_id = m.get('granteeTenantId')

        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('permissionId') is not None:
            self.permission_id = m.get('permissionId')

        if m.get('resourceKey') is not None:
            self.resource_key = m.get('resourceKey')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

