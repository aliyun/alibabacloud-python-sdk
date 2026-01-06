# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListReportShrinkRequest(DaraModel):
    def __init__(
        self,
        cursor: int = None,
        end_time: int = None,
        modified_end_time: int = None,
        modified_start_time: int = None,
        size: int = None,
        start_time: int = None,
        template_name: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.cursor = cursor
        # This parameter is required.
        self.end_time = end_time
        self.modified_end_time = modified_end_time
        self.modified_start_time = modified_start_time
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.start_time = start_time
        self.template_name = template_name
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.modified_end_time is not None:
            result['ModifiedEndTime'] = self.modified_end_time

        if self.modified_start_time is not None:
            result['ModifiedStartTime'] = self.modified_start_time

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ModifiedEndTime') is not None:
            self.modified_end_time = m.get('ModifiedEndTime')

        if m.get('ModifiedStartTime') is not None:
            self.modified_start_time = m.get('ModifiedStartTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

