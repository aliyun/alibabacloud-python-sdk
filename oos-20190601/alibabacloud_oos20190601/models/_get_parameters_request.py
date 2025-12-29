# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParametersRequest(DaraModel):
    def __init__(
        self,
        names: str = None,
        region_id: str = None,
    ):
        # The names of the common parameters.
        # 
        # This parameter is required.
        self.names = names
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.names is not None:
            result['Names'] = self.names

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

