# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateComputeInstanceRequest(DaraModel):
    def __init__(
        self,
        paid_type: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.paid_type = paid_type
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

