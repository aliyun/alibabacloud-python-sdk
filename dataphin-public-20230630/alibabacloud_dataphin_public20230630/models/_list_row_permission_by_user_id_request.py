# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListRowPermissionByUserIdRequest(DaraModel):
    def __init__(
        self,
        list_row_permission_by_user_id_query: main_models.ListRowPermissionByUserIdRequestListRowPermissionByUserIdQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_row_permission_by_user_id_query = list_row_permission_by_user_id_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_row_permission_by_user_id_query:
            self.list_row_permission_by_user_id_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_row_permission_by_user_id_query is not None:
            result['ListRowPermissionByUserIdQuery'] = self.list_row_permission_by_user_id_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListRowPermissionByUserIdQuery') is not None:
            temp_model = main_models.ListRowPermissionByUserIdRequestListRowPermissionByUserIdQuery()
            self.list_row_permission_by_user_id_query = temp_model.from_map(m.get('ListRowPermissionByUserIdQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListRowPermissionByUserIdRequestListRowPermissionByUserIdQuery(DaraModel):
    def __init__(
        self,
        operator: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['Operator'] = self.operator

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

