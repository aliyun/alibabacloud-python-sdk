# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInspirationBalanceForPartnerRequest(DaraModel):
    def __init__(
        self,
        belong_id: str = None,
        belong_id_type: str = None,
    ):
        # The owner ID, which can be a website ID or an Alibaba Cloud account ID.
        self.belong_id = belong_id
        # The type of the owner ID. Valid values: siteId and uid.
        self.belong_id_type = belong_id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.belong_id_type is not None:
            result['BelongIdType'] = self.belong_id_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('BelongIdType') is not None:
            self.belong_id_type = m.get('BelongIdType')

        return self

