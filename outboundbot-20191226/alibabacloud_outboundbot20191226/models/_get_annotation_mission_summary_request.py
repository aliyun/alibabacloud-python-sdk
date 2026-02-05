# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAnnotationMissionSummaryRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
    ):
        self.annotation_mission_id = annotation_mission_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        return self

