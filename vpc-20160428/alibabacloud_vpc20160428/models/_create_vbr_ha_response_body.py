# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVbrHaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vbr_ha_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the VBR failover group.
        self.vbr_ha_id = vbr_ha_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vbr_ha_id is not None:
            result['VbrHaId'] = self.vbr_ha_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VbrHaId') is not None:
            self.vbr_ha_id = m.get('VbrHaId')

        return self

