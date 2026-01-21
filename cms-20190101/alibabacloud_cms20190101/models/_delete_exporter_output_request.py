# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteExporterOutputRequest(DaraModel):
    def __init__(
        self,
        dest_name: str = None,
        region_id: str = None,
    ):
        # The name of the configuration set.
        # 
        # This parameter is required.
        self.dest_name = dest_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_name is not None:
            result['DestName'] = self.dest_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestName') is not None:
            self.dest_name = m.get('DestName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

