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
        region_id: str = None,
        report_language: str = None,
        report_region_id: str = None,
        report_type: str = None,
        start_time: str = None,
    ):
        # The end of the inspection time range. The time must be in UTC and formatted as YYYY-MM-DDTHH:mm:ssZ. If StartTime and EndTime are not specified, the inspection covers the last 24 hours.
        self.end_time = end_time
        # The inspection items to run, separated by commas. If this parameter is omitted, all inspection items are run.
        # 
        # ### Inspection items
        # 
        # - `instance_info` (instance information)
        # 
        # - `resource_usage` (resource usage)
        # 
        # - `connection_session_management` (connection and session management)
        # 
        # - `performance_metrics` (performance metrics)
        # 
        # - `slow_query_analysis` (slow query analysis)
        # 
        # - `error_log_analysis` (error log analysis)
        # 
        # - `lock_wait_deadlock_analysis` (lock wait and deadlock analysis)
        # 
        # - `backup_recovery_analysis` (backup and recovery analysis)
        # 
        # - `high_availability_disaster_recovery_analysis` (high availability and disaster recovery inspection)
        # 
        # - `security_configuration_analysis` (security configuration inspection)
        # 
        # - `storage_engine_analysis` (storage engine inspection)
        # 
        # - `schema_object_analysis` (schema and object inspection)
        self.inspection_items = inspection_items
        # The IDs of the instances to inspect. Separate multiple instance IDs with a comma.
        self.instance_ids = instance_ids
        # The region ID.
        self.region_id = region_id
        # The language of the inspection report. Valid values are zh-CN (Simplified Chinese) and en-US (English). The default value is en-US.
        self.report_language = report_language
        self.report_region_id = report_region_id
        # The format of the inspection report. Valid values are pdf and json. The default value is pdf.
        self.report_type = report_type
        # The beginning of the inspection time range. The time must be in UTC and formatted as YYYY-MM-DDTHH:mm:ssZ. If StartTime and EndTime are not specified, the inspection covers the last 24 hours.
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

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

        return self

