# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListScheduledTasksResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        schedules: List[main_models.ListScheduledTasksResponseBodySchedules] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of records returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of scheduled inspection tasks.
        self.schedules = schedules
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.schedules:
            for v1 in self.schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Schedules'] = []
        if self.schedules is not None:
            for k1 in self.schedules:
                result['Schedules'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.schedules = []
        if m.get('Schedules') is not None:
            for k1 in m.get('Schedules'):
                temp_model = main_models.ListScheduledTasksResponseBodySchedules()
                self.schedules.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScheduledTasksResponseBodySchedules(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        frequency: str = None,
        inspection_items: str = None,
        instance_count: int = None,
        name: str = None,
        region_id: str = None,
        report_language: str = None,
        report_type: str = None,
        scheduled_id: str = None,
        task_start_time: str = None,
        time_range: str = None,
    ):
        # The creation time of the task.
        self.create_time = create_time
        # The description of the inspection task.
        self.description = description
        # The new inspection frequency. Separate multiple values with commas (,). Default value: DAILY. Valid values:
        # 
        # *   DAILY
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        # 
        # ### [](#daily--dailymonday--daily-)Note: DAILY takes precedence over other values. For example, if you set this parameter to DAILY,Monday, the backend will use DAILY as the inspection frequency.
        self.frequency = frequency
        self.inspection_items = inspection_items
        # The number of instances covered by the task.
        self.instance_count = instance_count
        # The name of the task.
        self.name = name
        self.region_id = region_id
        self.report_language = report_language
        self.report_type = report_type
        # The ID of the scheduled inspection configuration.
        self.scheduled_id = scheduled_id
        # The actual start time of the task.
        self.task_start_time = task_start_time
        # The inspection time range. The default value is the latest 24 hours. Valid values: 1 to 168. The maximum value is 7 days.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

