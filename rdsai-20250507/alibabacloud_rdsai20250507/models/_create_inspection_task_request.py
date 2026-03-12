# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInspectionTaskRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        inspection_items: str = None,
        instance_ids: str = None,
        report_language: str = None,
        start_time: str = None,
    ):
        # The end time of the inspection task. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. By default, the time range of the task is the latest 24 hours.
        self.end_time = end_time
        # The inspection items. Separates multiple items with commas (,). If this parameter is empty or not specified, all inspection items are executed.
        # 
        # ### [](#)Valid values:
        # 
        # *   instance_info
        # *   resource_usage
        # *   connection_session_management
        # *   performance_metrics
        # *   slow_query_analysis
        # *   error_log_analysis
        # *   lock_wait_deadlock_analysis
        # *   backup_recovery_analysis
        # *   high_availability_disaster_recovery_analysis
        # *   security_configuration_analysis
        # *   storage_engine_analysis
        # *   schema_object_analysis
        self.inspection_items = inspection_items
        # The instances covered by the task. Separates multiple instance IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.report_language = report_language
        # The start time of the inspection task. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. By default, the time range of the task is the latest 24 hours.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

