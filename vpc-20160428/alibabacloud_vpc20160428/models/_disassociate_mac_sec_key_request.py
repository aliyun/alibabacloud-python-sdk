# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisassociateMacSecKeyRequest(DaraModel):
    def __init__(
        self,
        ckn: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ckn = ckn
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ckn is not None:
            result['Ckn'] = self.ckn

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ckn') is not None:
            self.ckn = m.get('Ckn')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

