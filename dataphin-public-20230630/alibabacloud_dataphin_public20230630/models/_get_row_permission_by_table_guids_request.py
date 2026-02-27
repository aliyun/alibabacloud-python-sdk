# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetRowPermissionByTableGuidsRequest(DaraModel):
    def __init__(
        self,
        get_row_permission_by_table_guids_query: main_models.GetRowPermissionByTableGuidsRequestGetRowPermissionByTableGuidsQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.get_row_permission_by_table_guids_query = get_row_permission_by_table_guids_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.get_row_permission_by_table_guids_query:
            self.get_row_permission_by_table_guids_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_row_permission_by_table_guids_query is not None:
            result['GetRowPermissionByTableGuidsQuery'] = self.get_row_permission_by_table_guids_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetRowPermissionByTableGuidsQuery') is not None:
            temp_model = main_models.GetRowPermissionByTableGuidsRequestGetRowPermissionByTableGuidsQuery()
            self.get_row_permission_by_table_guids_query = temp_model.from_map(m.get('GetRowPermissionByTableGuidsQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetRowPermissionByTableGuidsRequestGetRowPermissionByTableGuidsQuery(DaraModel):
    def __init__(
        self,
        table_guids: List[str] = None,
    ):
        # This parameter is required.
        self.table_guids = table_guids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_guids is not None:
            result['TableGuids'] = self.table_guids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuids') is not None:
            self.table_guids = m.get('TableGuids')

        return self

