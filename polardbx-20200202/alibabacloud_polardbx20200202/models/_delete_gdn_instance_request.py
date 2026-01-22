# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGdnInstanceRequest(DaraModel):
    def __init__(
        self,
        gdn_instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.gdn_instance_name = gdn_instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gdn_instance_name is not None:
            result['GdnInstanceName'] = self.gdn_instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GdnInstanceName') is not None:
            self.gdn_instance_name = m.get('GdnInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

