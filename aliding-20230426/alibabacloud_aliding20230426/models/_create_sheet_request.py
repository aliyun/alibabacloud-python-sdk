# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateSheetRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        tenant_context: main_models.CreateSheetRequestTenantContext = None,
        workbook_id: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.tenant_context = tenant_context
        # This parameter is required.
        self.workbook_id = workbook_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.workbook_id is not None:
            result['WorkbookId'] = self.workbook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateSheetRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WorkbookId') is not None:
            self.workbook_id = m.get('WorkbookId')

        return self

class CreateSheetRequestTenantContext(DaraModel):
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

