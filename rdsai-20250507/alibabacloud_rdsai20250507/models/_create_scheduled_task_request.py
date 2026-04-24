# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        frequency: str = None,
        inspection_items: str = None,
        instance_ids: str = None,
        name: str = None,
        region_id: str = None,
        report_language: str = None,
        report_region_id: str = None,
        report_type: str = None,
        start_time: str = None,
        time_range: str = None,
    ):
        # The description of the scheduled inspection task.
        self.description = description
        # The new inspection frequency. Separate multiple values with commas (,). Default value: DAILY. Valid values:
        # 
        # *   DAILY
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday \\*Sunday
        # 
        # ### [](#daily--dailymonday--daily-)Note: DAILY takes precedence over other values. For example, if you enter DAILY,Monday, the backend uses DAILY as the inspection frequency.
        self.frequency = frequency
        self.inspection_items = inspection_items
        # The IDs of the related instances. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The name of the scheduled inspection task. The name cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.report_language = report_language
        self.report_region_id = report_region_id
        self.report_type = report_type
        # The time when the inspection task is executed. Specify the time in the ISO 8601 standard in the HH:mm:ssZ format. The time must be in UTC. Default value: 02:00 AM.
        self.start_time = start_time
        # The inspection time range. The default value is the latest 24 hours. Valid values: 1 to 168. The maximum value is 7 days.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.report_region_id is not None:
            result['ReportRegionId'] = self.report_region_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ReportRegionId') is not None:
            self.report_region_id = m.get('ReportRegionId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

