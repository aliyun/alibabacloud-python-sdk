# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppInstanceTicketRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        client_id: str = None,
        role: str = None,
    ):
        # The customer business ID.
        self.biz_id = biz_id
        # The Client ID of the device for which you want to revoke the access credential.
        self.client_id = client_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

