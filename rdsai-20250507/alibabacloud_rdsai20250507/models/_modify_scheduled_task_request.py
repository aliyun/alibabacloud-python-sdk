# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        frequency: str = None,
        inspection_items: str = None,
        instance_ids: str = None,
        name: str = None,
        report_language: str = None,
        scheduled_id: str = None,
        start_time: str = None,
        time_range: str = None,
    ):
        # The new description of the inspection configuration.
        self.description = description
        # The new inspection frequency. Separate multiple values with a comma (,). The default value is DAILY. Valid values:
        # 
        # - DAILY: Every day
        # 
        # - Monday: Every Monday
        # 
        # - Tuesday: Every Tuesday
        # 
        # - Wednesday: Every Wednesday
        # 
        # - Thursday: Every Thursday
        # 
        # - Friday: Every Friday
        # 
        # - Saturday: Every Saturday
        # 
        # - Sunday: Every Sunday
        # 
        # ### Note: `DAILY` overrides all other day-of-the-week settings. For example, if you specify `DAILY,Monday`, the system uses `DAILY` as the inspection frequency.
        self.frequency = frequency
        self.inspection_items = inspection_items
        # The new instance IDs to associate with the task. Separate multiple IDs with a comma (,).
        self.instance_ids = instance_ids
        # The new name of the inspection configuration.
        self.name = name
        self.report_language = report_language
        # The ID of the scheduled inspection configuration.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id
        # The new time to run the inspection task. The time must be in the `HH:mm:ssZ` format and in UTC.
        self.start_time = start_time
        # The inspection time range in hours. The default is 24, which means data from the last 24 hours is inspected. Valid values: 1 to 168. The maximum supported range is 7 days.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

