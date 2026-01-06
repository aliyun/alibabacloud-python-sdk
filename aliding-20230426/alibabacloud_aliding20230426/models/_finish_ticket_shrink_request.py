# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FinishTicketShrinkRequest(DaraModel):
    def __init__(
        self,
        notify_shrink: str = None,
        open_team_id: str = None,
        open_ticket_id: str = None,
        tenant_context_shrink: str = None,
        ticket_memo_shrink: str = None,
    ):
        self.notify_shrink = notify_shrink
        # This parameter is required.
        self.open_team_id = open_team_id
        # This parameter is required.
        self.open_ticket_id = open_ticket_id
        self.tenant_context_shrink = tenant_context_shrink
        self.ticket_memo_shrink = ticket_memo_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_shrink is not None:
            result['Notify'] = self.notify_shrink

        if self.open_team_id is not None:
            result['OpenTeamId'] = self.open_team_id

        if self.open_ticket_id is not None:
            result['OpenTicketId'] = self.open_ticket_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.ticket_memo_shrink is not None:
            result['TicketMemo'] = self.ticket_memo_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Notify') is not None:
            self.notify_shrink = m.get('Notify')

        if m.get('OpenTeamId') is not None:
            self.open_team_id = m.get('OpenTeamId')

        if m.get('OpenTicketId') is not None:
            self.open_ticket_id = m.get('OpenTicketId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('TicketMemo') is not None:
            self.ticket_memo_shrink = m.get('TicketMemo')

        return self

