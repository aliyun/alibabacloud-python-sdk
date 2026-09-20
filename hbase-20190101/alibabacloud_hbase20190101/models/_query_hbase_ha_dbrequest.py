# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHBaseHaDBRequest(DaraModel):
    def __init__(
        self,
        bds_id: str = None,
    ):
        # The ID of the BDS cluster.
        # 
        # This parameter is required.
        self.bds_id = bds_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')

        return self

