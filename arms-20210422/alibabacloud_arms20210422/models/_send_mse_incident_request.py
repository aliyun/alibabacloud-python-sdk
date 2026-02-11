# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMseIncidentRequest(DaraModel):
    def __init__(
        self,
        incidents: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.incidents = incidents
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incidents is not None:
            result['Incidents'] = self.incidents

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incidents') is not None:
            self.incidents = m.get('Incidents')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

