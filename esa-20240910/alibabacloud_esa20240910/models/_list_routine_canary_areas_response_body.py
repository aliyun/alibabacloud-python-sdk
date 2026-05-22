# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListRoutineCanaryAreasResponseBody(DaraModel):
    def __init__(
        self,
        canary_areas: List[str] = None,
        request_id: str = None,
    ):
        # The regions for canary release.
        self.canary_areas = canary_areas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.canary_areas is not None:
            result['CanaryAreas'] = self.canary_areas

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryAreas') is not None:
            self.canary_areas = m.get('CanaryAreas')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

