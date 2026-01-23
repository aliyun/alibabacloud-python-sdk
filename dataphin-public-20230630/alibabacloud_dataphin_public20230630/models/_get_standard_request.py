# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        standard_get_query: main_models.GetStandardRequestStandardGetQuery = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.standard_get_query = standard_get_query

    def validate(self):
        if self.standard_get_query:
            self.standard_get_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.standard_get_query is not None:
            result['StandardGetQuery'] = self.standard_get_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('StandardGetQuery') is not None:
            temp_model = main_models.GetStandardRequestStandardGetQuery()
            self.standard_get_query = temp_model.from_map(m.get('StandardGetQuery'))

        return self

class GetStandardRequestStandardGetQuery(DaraModel):
    def __init__(
        self,
        need_relation: bool = None,
        nullable: bool = None,
        standard_id: int = None,
        standard_stage: str = None,
        version: int = None,
    ):
        self.need_relation = need_relation
        self.nullable = nullable
        # This parameter is required.
        self.standard_id = standard_id
        self.standard_stage = standard_stage
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_relation is not None:
            result['NeedRelation'] = self.need_relation

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.standard_stage is not None:
            result['StandardStage'] = self.standard_stage

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedRelation') is not None:
            self.need_relation = m.get('NeedRelation')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('StandardStage') is not None:
            self.standard_stage = m.get('StandardStage')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

