# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OfflineAnnouncementRequest(DaraModel):
    def __init__(
        self,
        announcement_id: int = None,
        tenant_id: str = None,
    ):
        # The business ID of the announcement.
        # 
        # This parameter is required.
        self.announcement_id = announcement_id
        # The tenant ID. This is a common parameter. Pass it explicitly in winnexo-cli by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.announcement_id is not None:
            result['announcementId'] = self.announcement_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('announcementId') is not None:
            self.announcement_id = m.get('announcementId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

