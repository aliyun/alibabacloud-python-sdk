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
        planned_start_time_from: str = None,
        planned_start_time_to: str = None,
        state: str = None,
    ):
        # The earliest actual start time.
        self.actual_start_time_from = actual_start_time_from
        # The latest actual start time.
        self.actual_start_time_to = actual_start_time_to
        # The instance ID of the outbound robot.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the campaign.
        self.name = name
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The earliest planned start time.
        self.planned_start_time_from = planned_start_time_from
        # The latest planned start time.
        self.planned_start_time_to = planned_start_time_to
        # The status of the campaign.
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

        if self.planned_start_time_from is not None:
            result['PlannedStartTimeFrom'] = self.planned_start_time_from

        if self.planned_start_time_to is not None:
            result['PlannedStartTimeTo'] = self.planned_start_time_to

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

        if m.get('PlannedStartTimeFrom') is not None:
            self.planned_start_time_from = m.get('PlannedStartTimeFrom')

        if m.get('PlannedStartTimeTo') is not None:
            self.planned_start_time_to = m.get('PlannedStartTimeTo')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

