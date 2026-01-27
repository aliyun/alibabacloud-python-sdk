# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IsKeepAliveResponseBody(DaraModel):
    def __init__(
        self,
        is_keep_alive: bool = None,
        office_site_id: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        # Identifies whether the user should remain logged on to the client.
        self.is_keep_alive = is_keep_alive
        # The office network ID.
        self.office_site_id = office_site_id
        # The request ID.
        self.request_id = request_id
        # The unique ID (UID) of the Alibaba Cloud account.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_keep_alive is not None:
            result['IsKeepAlive'] = self.is_keep_alive

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsKeepAlive') is not None:
            self.is_keep_alive = m.get('IsKeepAlive')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

