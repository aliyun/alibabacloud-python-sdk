# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEccInfoRequest(DaraModel):
    def __init__(
        self,
        ecc_id: str = None,
    ):
        # The ID of the ECC.
        # 
        # This parameter is required.
        self.ecc_id = ecc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        return self

