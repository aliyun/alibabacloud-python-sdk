# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAppInstanceTicketRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        token: str = None,
        uuid: str = None,
    ):
        self.biz_id = biz_id
        self.token = token
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.token is not None:
            result['Token'] = self.token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

