# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkMeetingInfoRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.GetDingtalkMeetingInfoRequestTenantContext = None,
        conference_id: str = None,
        org_id: str = None,
    ):
        self.tenant_context = tenant_context
        # This parameter is required.
        self.conference_id = conference_id
        self.org_id = org_id

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

        if self.org_id is not None:
            result['orgId'] = self.org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.GetDingtalkMeetingInfoRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        return self

class GetDingtalkMeetingInfoRequestTenantContext(DaraModel):
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

