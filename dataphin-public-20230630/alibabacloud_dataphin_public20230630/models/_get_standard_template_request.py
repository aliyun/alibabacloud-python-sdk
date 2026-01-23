# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardTemplateRequest(DaraModel):
    def __init__(
        self,
        filter_query: main_models.GetStandardTemplateRequestFilterQuery = None,
        id: int = None,
        nullable: bool = None,
        op_tenant_id: int = None,
    ):
        self.filter_query = filter_query
        # This parameter is required.
        self.id = id
        self.nullable = nullable
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.filter_query:
            self.filter_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_query is not None:
            result['FilterQuery'] = self.filter_query.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterQuery') is not None:
            temp_model = main_models.GetStandardTemplateRequestFilterQuery()
            self.filter_query = temp_model.from_map(m.get('FilterQuery'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetStandardTemplateRequestFilterQuery(DaraModel):
    def __init__(
        self,
        version: int = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

