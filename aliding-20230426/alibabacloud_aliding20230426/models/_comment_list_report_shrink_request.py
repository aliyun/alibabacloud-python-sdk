# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CommentListReportShrinkRequest(DaraModel):
    def __init__(
        self,
        offset: int = None,
        report_id: str = None,
        size: int = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.report_id = report_id
        # This parameter is required.
        self.size = size
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

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

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

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
            self.tenant_context_shrink = m.get('TenantContext')

        return self

