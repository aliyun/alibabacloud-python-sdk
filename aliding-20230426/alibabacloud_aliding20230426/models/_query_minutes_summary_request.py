# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryMinutesSummaryRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.QueryMinutesSummaryRequestTenantContext = None,
        conference_id: str = None,
        summary_type_list: List[str] = None,
    ):
        self.tenant_context = tenant_context
        # This parameter is required.
        self.conference_id = conference_id
        self.summary_type_list = summary_type_list

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.summary_type_list is not None:
            result['summaryTypeList'] = self.summary_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.QueryMinutesSummaryRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('summaryTypeList') is not None:
            self.summary_type_list = m.get('summaryTypeList')

        return self

class QueryMinutesSummaryRequestTenantContext(DaraModel):
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

