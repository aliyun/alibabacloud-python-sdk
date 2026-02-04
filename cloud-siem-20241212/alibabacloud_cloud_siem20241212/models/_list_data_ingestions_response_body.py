# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataIngestionsResponseBody(DaraModel):
    def __init__(
        self,
        data_ingestions: List[main_models.ListDataIngestionsResponseBodyDataIngestions] = None,
        request_id: str = None,
    ):
        self.data_ingestions = data_ingestions
        self.request_id = request_id

    def validate(self):
        if self.data_ingestions:
            for v1 in self.data_ingestions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataIngestions'] = []
        if self.data_ingestions is not None:
            for k1 in self.data_ingestions:
                result['DataIngestions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_ingestions = []
        if m.get('DataIngestions') is not None:
            for k1 in m.get('DataIngestions'):
                temp_model = main_models.ListDataIngestionsResponseBodyDataIngestions()
                self.data_ingestions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataIngestionsResponseBodyDataIngestions(DaraModel):
    def __init__(
        self,
        active_time: int = None,
        capacity_count: int = None,
        create_time: int = None,
        data_ingestion_id: str = None,
        data_ingestion_mode: str = None,
        data_ingestion_mode_editable: bool = None,
        data_ingestion_state: str = None,
        data_ingestion_state_code: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_type: str = None,
        data_source_editable: bool = None,
        data_source_id: str = None,
        normalization_rule_editable: bool = None,
        normalization_rule_id: str = None,
        realtime_data_source_id: str = None,
        scan_data_source_id: str = None,
        stream_job_id: str = None,
        update_time: int = None,
    ):
        self.active_time = active_time
        self.capacity_count = capacity_count
        self.create_time = create_time
        self.data_ingestion_id = data_ingestion_id
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_mode_editable = data_ingestion_mode_editable
        self.data_ingestion_state = data_ingestion_state
        self.data_ingestion_state_code = data_ingestion_state_code
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_type = data_ingestion_type
        self.data_source_editable = data_source_editable
        self.data_source_id = data_source_id
        self.normalization_rule_editable = normalization_rule_editable
        self.normalization_rule_id = normalization_rule_id
        self.realtime_data_source_id = realtime_data_source_id
        self.scan_data_source_id = scan_data_source_id
        self.stream_job_id = stream_job_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time

        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode

        if self.data_ingestion_mode_editable is not None:
            result['DataIngestionModeEditable'] = self.data_ingestion_mode_editable

        if self.data_ingestion_state is not None:
            result['DataIngestionState'] = self.data_ingestion_state

        if self.data_ingestion_state_code is not None:
            result['DataIngestionStateCode'] = self.data_ingestion_state_code

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id

        if self.data_ingestion_type is not None:
            result['DataIngestionType'] = self.data_ingestion_type

        if self.data_source_editable is not None:
            result['DataSourceEditable'] = self.data_source_editable

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.normalization_rule_editable is not None:
            result['NormalizationRuleEditable'] = self.normalization_rule_editable

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.realtime_data_source_id is not None:
            result['RealtimeDataSourceId'] = self.realtime_data_source_id

        if self.scan_data_source_id is not None:
            result['ScanDataSourceId'] = self.scan_data_source_id

        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')

        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')

        if m.get('DataIngestionModeEditable') is not None:
            self.data_ingestion_mode_editable = m.get('DataIngestionModeEditable')

        if m.get('DataIngestionState') is not None:
            self.data_ingestion_state = m.get('DataIngestionState')

        if m.get('DataIngestionStateCode') is not None:
            self.data_ingestion_state_code = m.get('DataIngestionStateCode')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')

        if m.get('DataIngestionType') is not None:
            self.data_ingestion_type = m.get('DataIngestionType')

        if m.get('DataSourceEditable') is not None:
            self.data_source_editable = m.get('DataSourceEditable')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('NormalizationRuleEditable') is not None:
            self.normalization_rule_editable = m.get('NormalizationRuleEditable')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('RealtimeDataSourceId') is not None:
            self.realtime_data_source_id = m.get('RealtimeDataSourceId')

        if m.get('ScanDataSourceId') is not None:
            self.scan_data_source_id = m.get('ScanDataSourceId')

        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

