# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class StatisticsListByTypeReportRequest(DaraModel):
    def __init__(
        self,
        offset: int = None,
        report_id: str = None,
        size: int = None,
        tenant_context: main_models.StatisticsListByTypeReportRequestTenantContext = None,
        type: int = None,
    ):
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.report_id = report_id
        # This parameter is required.
        self.size = size
        self.tenant_context = tenant_context
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.size is not None:
            result['Size'] = self.size

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TenantContext') is not None:
            temp_model = main_models.StatisticsListByTypeReportRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class StatisticsListByTypeReportRequestTenantContext(DaraModel):
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

