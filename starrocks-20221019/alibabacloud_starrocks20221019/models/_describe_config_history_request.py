# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfigHistoryRequest(DaraModel):
    def __init__(
        self,
        effect_statuses: str = None,
        end_time: int = None,
        instance_id: str = None,
        need_total: bool = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.effect_statuses = effect_statuses
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.need_total = need_total
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_statuses is not None:
            result['EffectStatuses'] = self.effect_statuses

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_total is not None:
            result['NeedTotal'] = self.need_total

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectStatuses') is not None:
            self.effect_statuses = m.get('EffectStatuses')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedTotal') is not None:
            self.need_total = m.get('NeedTotal')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

