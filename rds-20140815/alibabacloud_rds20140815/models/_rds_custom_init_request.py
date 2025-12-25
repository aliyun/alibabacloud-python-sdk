# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RdsCustomInitRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        service_linked_role: str = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.service_linked_role = service_linked_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')

        return self

