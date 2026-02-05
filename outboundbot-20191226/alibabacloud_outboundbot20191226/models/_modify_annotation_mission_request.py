# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAnnotationMissionRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
        annotation_mission_name: str = None,
        annotation_status: int = None,
        delete: bool = None,
    ):
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_name = annotation_mission_name
        self.annotation_status = annotation_status
        self.delete = delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_name is not None:
            result['AnnotationMissionName'] = self.annotation_mission_name

        if self.annotation_status is not None:
            result['AnnotationStatus'] = self.annotation_status

        if self.delete is not None:
            result['Delete'] = self.delete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionName') is not None:
            self.annotation_mission_name = m.get('AnnotationMissionName')

        if m.get('AnnotationStatus') is not None:
            self.annotation_status = m.get('AnnotationStatus')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        return self

