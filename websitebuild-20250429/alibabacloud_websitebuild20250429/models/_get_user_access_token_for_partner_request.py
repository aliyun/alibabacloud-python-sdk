# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserAccessTokenForPartnerRequest(DaraModel):
    def __init__(
        self,
        site_host: str = None,
        ticket: str = None,
    ):
        self.site_host = site_host
        # This parameter is required.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

