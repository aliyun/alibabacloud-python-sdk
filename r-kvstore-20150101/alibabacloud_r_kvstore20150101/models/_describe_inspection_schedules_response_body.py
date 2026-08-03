# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInspectionSchedulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeInspectionSchedulesResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeInspectionSchedulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInspectionSchedulesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeInspectionSchedulesResponseBodyDataItems] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeInspectionSchedulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInspectionSchedulesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cron_expression: str = None,
        enabled: int = None,
        inspection_items: str = None,
        inspection_window: str = None,
        instance_ids: str = None,
        next_fire_time: str = None,
        notify_config: str = None,
        report_language: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
        timezone: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.cron_expression = cron_expression
        self.enabled = enabled
        self.inspection_items = inspection_items
        self.inspection_window = inspection_window
        self.instance_ids = instance_ids
        self.next_fire_time = next_fire_time
        self.notify_config = notify_config
        self.report_language = report_language
        self.schedule_id = schedule_id
        self.schedule_name = schedule_name
        self.timezone = timezone
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.inspection_window is not None:
            result['InspectionWindow'] = self.inspection_window

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.next_fire_time is not None:
            result['NextFireTime'] = self.next_fire_time

        if self.notify_config is not None:
            result['NotifyConfig'] = self.notify_config

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InspectionWindow') is not None:
            self.inspection_window = m.get('InspectionWindow')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('NextFireTime') is not None:
            self.next_fire_time = m.get('NextFireTime')

        if m.get('NotifyConfig') is not None:
            self.notify_config = m.get('NotifyConfig')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

