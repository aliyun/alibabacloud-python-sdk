# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class InsertMultiDimTableRecordRequest(DaraModel):
    def __init__(
        self,
        base_id: str = None,
        records: List[main_models.InsertMultiDimTableRecordRequestRecords] = None,
        sheet_id_or_name: str = None,
        tenant_context: main_models.InsertMultiDimTableRecordRequestTenantContext = None,
    ):
        # This parameter is required.
        self.base_id = base_id
        # This parameter is required.
        self.records = records
        # This parameter is required.
        self.sheet_id_or_name = sheet_id_or_name
        self.tenant_context = tenant_context

    def validate(self):
        if self.records:
            for v1 in self.records:
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

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.sheet_id_or_name is not None:
            result['SheetIdOrName'] = self.sheet_id_or_name

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseId') is not None:
            self.base_id = m.get('BaseId')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.InsertMultiDimTableRecordRequestRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('SheetIdOrName') is not None:
            self.sheet_id_or_name = m.get('SheetIdOrName')

        if m.get('TenantContext') is not None:
            temp_model = main_models.InsertMultiDimTableRecordRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class InsertMultiDimTableRecordRequestTenantContext(DaraModel):
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

class InsertMultiDimTableRecordRequestRecords(DaraModel):
    def __init__(
        self,
        fields: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        return self

