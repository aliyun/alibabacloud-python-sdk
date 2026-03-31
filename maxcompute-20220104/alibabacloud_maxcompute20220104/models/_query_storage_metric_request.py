# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryStorageMetricRequest(DaraModel):
    def __init__(
        self,
        project_list: List[str] = None,
        type_list: List[str] = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.project_list = project_list
        self.type_list = type_list
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_list is not None:
            result['projectList'] = self.project_list

        if self.type_list is not None:
            result['typeList'] = self.type_list

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectList') is not None:
            self.project_list = m.get('projectList')

        if m.get('typeList') is not None:
            self.type_list = m.get('typeList')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

