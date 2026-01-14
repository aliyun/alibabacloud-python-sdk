# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachAssessmentPointRequest(DaraModel):
    def __init__(
        self,
        point_id: str = None,
    ):
        self.point_id = point_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.point_id is not None:
            result['pointId'] = self.point_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')

        return self

