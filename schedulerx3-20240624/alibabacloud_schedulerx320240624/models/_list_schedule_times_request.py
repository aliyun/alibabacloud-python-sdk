# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScheduleTimesRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        calendar: str = None,
        cluster_id: str = None,
        time_expression: str = None,
        time_type: int = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.calendar = calendar
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.time_expression = time_expression
        # This parameter is required.
        self.time_type = time_type
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

