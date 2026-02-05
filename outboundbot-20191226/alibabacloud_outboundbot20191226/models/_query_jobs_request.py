# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryJobsRequest(DaraModel):
    def __init__(
        self,
        contact_name: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
        scenario_id: str = None,
        start_time: int = None,
        time_alignment: str = None,
    ):
        self.contact_name = contact_name
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.phone_number = phone_number
        self.scenario_id = scenario_id
        self.start_time = start_time
        self.time_alignment = time_alignment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_alignment is not None:
            result['TimeAlignment'] = self.time_alignment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeAlignment') is not None:
            self.time_alignment = m.get('TimeAlignment')

        return self

