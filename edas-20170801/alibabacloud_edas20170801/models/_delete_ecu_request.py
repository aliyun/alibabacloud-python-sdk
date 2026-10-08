# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEcuRequest(DaraModel):
    def __init__(
        self,
        ecu_id: str = None,
    ):
        # The unique ID of the ECU to be deleted.
        # 
        # This parameter is required.
        self.ecu_id = ecu_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        return self

