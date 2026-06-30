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
        # The inspection frequency. Use commas (,) to separate multiple values. The default is DAILY. Valid values:
        # 
        # - DAILY: Every day
        # 
        # - Monday: Monday
        # 
        # - Tuesday: Tuesday
        # 
        # - Wednesday: Wednesday
        # 
        # - Thursday: Thursday
        # 
        # - Friday: Friday
        # 
        # - Saturday: Saturday
        # 
        # - Sunday: Sunday
        # 
        # ### Note: DAILY overrides weekly values. For example, if you enter DAILY,Monday, the system uses DAILY as the inspection frequency.
        self.frequency = frequency
        self.inspection_items = inspection_items
        # The IDs of the instances for the task. Use commas (,) to separate multiple IDs.
        self.instance_ids = instance_ids
        # The name of the scheduled inspection task. The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The report language. The default value is zh-CN. Supported values: zh-CN, zh-TW, ja-JP, and en-US.
        self.report_language = report_language
        # The ID of the region where the report is stored.
        self.report_region_id = report_region_id
        # The type of the report.
        self.report_type = report_type
        # The execution time for the scheduled inspection task. Specify the time in the HH:mm:ssZ format (UTC time). The default is 02:00:00Z.
        self.start_time = start_time
        # The time range of data to inspect, in hours. Valid values are from 1 to 168 (7 days). The default is 24.
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

