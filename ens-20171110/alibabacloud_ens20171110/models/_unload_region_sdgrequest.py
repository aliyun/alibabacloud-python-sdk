# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnloadRegionSDGRequest(DaraModel):
    def __init__(
        self,
        destination_region_ids: List[str] = None,
        namespaces: List[str] = None,
        sdgid: str = None,
    ):
        # The destination nodes.
        # 
        # This parameter is required.
        self.destination_region_ids = destination_region_ids
        # An array that consists of queried namespaces.
        self.namespaces = namespaces
        # Deletes the shared data group (SDG) ID of the preloaded data.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

