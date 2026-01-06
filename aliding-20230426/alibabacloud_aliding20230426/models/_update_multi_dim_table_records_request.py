# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateMultiDimTableRecordsRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        record_ids: List[main_models.UpdateMultiDimTableRecordsRequestRecordIds] = None,
        sheet_id_or_name: str = None,
        tenant_context: main_models.UpdateMultiDimTableRecordsRequestTenantContext = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        # This parameter is required.
        self.record_ids = record_ids
        # This parameter is required.
        self.sheet_id_or_name = sheet_id_or_name
        self.tenant_context = tenant_context

    def validate(self):
        if self.record_ids:
            for v1 in self.record_ids:
                 if v1:
                    v1.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_id is not None:
            result['BaseId'] = self.base_id

        result['RecordIds'] = []
        if self.record_ids is not None:
            for k1 in self.record_ids:
                result['RecordIds'].append(k1.to_map() if k1 else None)

        if self.sheet_id_or_name is not None:
            result['SheetIdOrName'] = self.sheet_id_or_name

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        self.record_ids = []
        if m.get('RecordIds') is not None:
            for k1 in m.get('RecordIds'):
                temp_model = main_models.UpdateMultiDimTableRecordsRequestRecordIds()
                self.record_ids.append(temp_model.from_map(k1))

        if m.get('SheetIdOrName') is not None:
            self.sheet_id_or_name = m.get('SheetIdOrName')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateMultiDimTableRecordsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class UpdateMultiDimTableRecordsRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class UpdateMultiDimTableRecordsRequestRecordIds(DaraModel):
    def __init__(
        self,
        fields: Dict[str, Any] = None,
        id: str = None,
    ):
        # This parameter is required.
        self.fields = fields
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

