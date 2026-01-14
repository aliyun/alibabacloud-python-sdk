# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataSourceConnectionInfoRequest(DaraModel):
    def __init__(
        self,
        ds_id: str = None,
    ):
        # Data source ID.
        # 
        # This parameter is required.
        self.ds_id = ds_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        return self

