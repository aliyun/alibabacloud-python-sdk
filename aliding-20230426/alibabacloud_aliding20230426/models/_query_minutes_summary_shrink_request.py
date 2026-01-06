# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMinutesSummaryShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        conference_id: str = None,
        summary_type_list_shrink: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.conference_id = conference_id
        self.summary_type_list_shrink = summary_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.summary_type_list_shrink is not None:
            result['summaryTypeList'] = self.summary_type_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('summaryTypeList') is not None:
            self.summary_type_list_shrink = m.get('summaryTypeList')

        return self

