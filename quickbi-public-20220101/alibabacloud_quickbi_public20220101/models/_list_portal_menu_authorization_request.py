# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPortalMenuAuthorizationRequest(DaraModel):
    def __init__(
        self,
        data_portal_id: str = None,
    ):
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')

        return self

