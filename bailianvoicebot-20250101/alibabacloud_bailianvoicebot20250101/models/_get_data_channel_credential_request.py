# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataChannelCredentialRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.business_unit_id = business_unit_id
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        return self

