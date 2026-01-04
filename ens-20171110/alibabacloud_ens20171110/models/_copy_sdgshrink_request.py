# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopySDGShrinkRequest(DaraModel):
    def __init__(
        self,
        destination_region_ids_shrink: str = None,
        sdgid: str = None,
    ):
        # The destination nodes.
        # 
        # This parameter is required.
        self.destination_region_ids_shrink = destination_region_ids_shrink
        # The ID of the SDG that you want to copy.
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
        if self.destination_region_ids_shrink is not None:
            result['DestinationRegionIds'] = self.destination_region_ids_shrink

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids_shrink = m.get('DestinationRegionIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

