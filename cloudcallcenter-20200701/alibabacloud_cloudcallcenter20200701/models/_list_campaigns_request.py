# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCampaignsRequest(DaraModel):
    def __init__(
        self,
        actual_start_time_from: str = None,
        actual_start_time_to: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        planed_start_time_from: str = None,
        planed_start_time_to: str = None,
        queue_id: str = None,
        state: str = None,
    ):
        self.actual_start_time_from = actual_start_time_from
        self.actual_start_time_to = actual_start_time_to
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.planed_start_time_from = planed_start_time_from
        self.planed_start_time_to = planed_start_time_to
        self.queue_id = queue_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_start_time_from is not None:
            result['ActualStartTimeFrom'] = self.actual_start_time_from

        if self.actual_start_time_to is not None:
            result['ActualStartTimeTo'] = self.actual_start_time_to

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.planed_start_time_from is not None:
            result['PlanedStartTimeFrom'] = self.planed_start_time_from

        if self.planed_start_time_to is not None:
            result['PlanedStartTimeTo'] = self.planed_start_time_to

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualStartTimeFrom') is not None:
            self.actual_start_time_from = m.get('ActualStartTimeFrom')

        if m.get('ActualStartTimeTo') is not None:
            self.actual_start_time_to = m.get('ActualStartTimeTo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanedStartTimeFrom') is not None:
            self.planed_start_time_from = m.get('PlanedStartTimeFrom')

        if m.get('PlanedStartTimeTo') is not None:
            self.planed_start_time_to = m.get('PlanedStartTimeTo')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

