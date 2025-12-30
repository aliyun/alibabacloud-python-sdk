# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionZoneRemarkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        remark: str = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.remark = remark
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

