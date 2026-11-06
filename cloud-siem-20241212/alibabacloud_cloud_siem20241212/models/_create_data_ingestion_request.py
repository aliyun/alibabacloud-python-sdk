# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataIngestionRequest(DaraModel):
    def __init__(
        self,
        capacity_count: int = None,
        data_ingestion_mode: str = None,
        data_ingestion_state_code: str = None,
        data_ingestion_type: str = None,
        data_source_editable: bool = None,
        data_source_id: str = None,
        lang: str = None,
        normalization_rule_editable: bool = None,
        normalization_rule_id: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        scan_data_source_id: str = None,
        stream_job_id: str = None,
        update_time: int = None,
    ):
        self.capacity_count = capacity_count
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_state_code = data_ingestion_state_code
        self.data_ingestion_type = data_ingestion_type
        self.data_source_editable = data_source_editable
        self.data_source_id = data_source_id
        self.lang = lang
        self.normalization_rule_editable = normalization_rule_editable
        self.normalization_rule_id = normalization_rule_id
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
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
        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count

        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode

        if self.data_ingestion_state_code is not None:
            result['DataIngestionStateCode'] = self.data_ingestion_state_code

        if self.data_ingestion_type is not None:
            result['DataIngestionType'] = self.data_ingestion_type

        if self.data_source_editable is not None:
            result['DataSourceEditable'] = self.data_source_editable

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_rule_editable is not None:
            result['NormalizationRuleEditable'] = self.normalization_rule_editable

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.scan_data_source_id is not None:
            result['ScanDataSourceId'] = self.scan_data_source_id

        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')

        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')

        if m.get('DataIngestionStateCode') is not None:
            self.data_ingestion_state_code = m.get('DataIngestionStateCode')

        if m.get('DataIngestionType') is not None:
            self.data_ingestion_type = m.get('DataIngestionType')

        if m.get('DataSourceEditable') is not None:
            self.data_source_editable = m.get('DataSourceEditable')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationRuleEditable') is not None:
            self.normalization_rule_editable = m.get('NormalizationRuleEditable')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('ScanDataSourceId') is not None:
            self.scan_data_source_id = m.get('ScanDataSourceId')

        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

