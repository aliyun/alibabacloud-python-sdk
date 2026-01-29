# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCostUnitRequest(DaraModel):
    def __init__(
        self,
        owner_uid: int = None,
        unit_id: int = None,
    ):
        # The user ID of the cost center owner.
        # 
        # This parameter is required.
        self.owner_uid = owner_uid
        # The ID of the cost center. A value of -1 indicates the root cost center.
        # 
        # This parameter is required.
        self.unit_id = unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        return self

