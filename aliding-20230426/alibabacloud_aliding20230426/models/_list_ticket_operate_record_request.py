# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListTicketOperateRecordRequest(DaraModel):
    def __init__(
        self,
        open_team_id: str = None,
        open_ticket_id: str = None,
        tenant_context: main_models.ListTicketOperateRecordRequestTenantContext = None,
    ):
        # This parameter is required.
        self.open_team_id = open_team_id
        # This parameter is required.
        self.open_ticket_id = open_ticket_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_team_id is not None:
            result['OpenTeamId'] = self.open_team_id

        if self.open_ticket_id is not None:
            result['OpenTicketId'] = self.open_ticket_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenTeamId') is not None:
            self.open_team_id = m.get('OpenTeamId')

        if m.get('OpenTicketId') is not None:
            self.open_ticket_id = m.get('OpenTicketId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.ListTicketOperateRecordRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class ListTicketOperateRecordRequestTenantContext(DaraModel):
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

