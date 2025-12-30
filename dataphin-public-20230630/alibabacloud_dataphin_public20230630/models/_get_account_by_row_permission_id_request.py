# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAccountByRowPermissionIdRequest(DaraModel):
    def __init__(
        self,
        get_account_by_row_permission_id_query: main_models.GetAccountByRowPermissionIdRequestGetAccountByRowPermissionIdQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.get_account_by_row_permission_id_query = get_account_by_row_permission_id_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.get_account_by_row_permission_id_query:
            self.get_account_by_row_permission_id_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_account_by_row_permission_id_query is not None:
            result['GetAccountByRowPermissionIdQuery'] = self.get_account_by_row_permission_id_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetAccountByRowPermissionIdQuery') is not None:
            temp_model = main_models.GetAccountByRowPermissionIdRequestGetAccountByRowPermissionIdQuery()
            self.get_account_by_row_permission_id_query = temp_model.from_map(m.get('GetAccountByRowPermissionIdQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetAccountByRowPermissionIdRequestGetAccountByRowPermissionIdQuery(DaraModel):
    def __init__(
        self,
        row_permission_id: int = None,
        rule_ids: List[int] = None,
    ):
        # This parameter is required.
        self.row_permission_id = row_permission_id
        # This parameter is required.
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row_permission_id is not None:
            result['RowPermissionId'] = self.row_permission_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RowPermissionId') is not None:
            self.row_permission_id = m.get('RowPermissionId')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        return self

