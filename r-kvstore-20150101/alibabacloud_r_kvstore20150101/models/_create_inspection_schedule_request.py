# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInspectionScheduleRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        inspection_items: str = None,
        inspection_window: str = None,
        instance_id: str = None,
        instance_ids: str = None,
        report_language: str = None,
        schedule_name: str = None,
        security_token: str = None,
        timezone: str = None,
    ):
        # The cron expression for the periodic scheduling.
        self.cron_expression = cron_expression
        # The specified inspection items. The following inspection items are supported:
        # 
        # - RESOURCE_USAGE
        # - BIGKEY
        # - HOTKEY
        # - PERFORMANCE_METRICS
        # - SLOWLOG
        self.inspection_items = inspection_items
        # The time window.
        self.inspection_window = inspection_window
        # The O&M Assistant instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of associated instance IDs.
        # > 
        # > - Separate multiple instances with commas (,).
        self.instance_ids = instance_ids
        # The report language.
        self.report_language = report_language
        # The name of the timed scheduling.
        self.schedule_name = schedule_name
        self.security_token = security_token
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.inspection_window is not None:
            result['InspectionWindow'] = self.inspection_window

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InspectionWindow') is not None:
            self.inspection_window = m.get('InspectionWindow')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

