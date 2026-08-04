# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindFinanceTaxDetailRequest(DaraModel):
    def __init__(
        self,
        kp_id: int = None,
    ):
        # This parameter is required.
        self.kp_id = kp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kp_id is not None:
            result['KpId'] = self.kp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KpId') is not None:
            self.kp_id = m.get('KpId')

        return self

