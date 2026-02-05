# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAnnotationMissionSessionRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        environment: int = None,
        include_status_list_json_string: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        self.environment = environment
        self.include_status_list_json_string = include_status_list_json_string
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.include_status_list_json_string is not None:
            result['IncludeStatusListJsonString'] = self.include_status_list_json_string

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('IncludeStatusListJsonString') is not None:
            self.include_status_list_json_string = m.get('IncludeStatusListJsonString')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

