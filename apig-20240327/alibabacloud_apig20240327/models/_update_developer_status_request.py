# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDeveloperStatusRequest(DaraModel):
    def __init__(
        self,
        portal_id: str = None,
        status: str = None,
    ):
        # The ID of the portal to which the developer belongs, which is the primary ID of the portal resource. You can obtain this ID from the portalId field in the CreatePortal response or from the portalId field of an item in the ListPortals response.
        self.portal_id = portal_id
        # The target status of the developer. Valid values: PENDING, APPROVED, and REJECTED.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

