# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OpenServiceGroupForServiceCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        lane_id: int = None,
        service_ids: List[int] = None,
    ):
        self.company_id = company_id
        # This parameter is required.
        self.lane_id = lane_id
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.lane_id is not None:
            result['laneId'] = self.lane_id

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('laneId') is not None:
            self.lane_id = m.get('laneId')

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        return self

