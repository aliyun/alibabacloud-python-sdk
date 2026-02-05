# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAnnotationMissionRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
        annotation_mission_name: str = None,
        annotation_status_list_filter: List[int] = None,
        annotation_status_list_string_filter: str = None,
        create_time_end_filter: int = None,
        create_time_start_filter: int = None,
        instance_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_name = annotation_mission_name
        self.annotation_status_list_filter = annotation_status_list_filter
        self.annotation_status_list_string_filter = annotation_status_list_string_filter
        self.create_time_end_filter = create_time_end_filter
        self.create_time_start_filter = create_time_start_filter
        self.instance_id = instance_id
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

        if self.annotation_mission_name is not None:
            result['AnnotationMissionName'] = self.annotation_mission_name

        if self.annotation_status_list_filter is not None:
            result['AnnotationStatusListFilter'] = self.annotation_status_list_filter

        if self.annotation_status_list_string_filter is not None:
            result['AnnotationStatusListStringFilter'] = self.annotation_status_list_string_filter

        if self.create_time_end_filter is not None:
            result['CreateTimeEndFilter'] = self.create_time_end_filter

        if self.create_time_start_filter is not None:
            result['CreateTimeStartFilter'] = self.create_time_start_filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionName') is not None:
            self.annotation_mission_name = m.get('AnnotationMissionName')

        if m.get('AnnotationStatusListFilter') is not None:
            self.annotation_status_list_filter = m.get('AnnotationStatusListFilter')

        if m.get('AnnotationStatusListStringFilter') is not None:
            self.annotation_status_list_string_filter = m.get('AnnotationStatusListStringFilter')

        if m.get('CreateTimeEndFilter') is not None:
            self.create_time_end_filter = m.get('CreateTimeEndFilter')

        if m.get('CreateTimeStartFilter') is not None:
            self.create_time_start_filter = m.get('CreateTimeStartFilter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

