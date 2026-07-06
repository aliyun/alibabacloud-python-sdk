# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetGovernanceItemReportResponseBody(DaraModel):
    def __init__(
        self,
        columns_schema: main_models.GetGovernanceItemReportResponseBodyColumnsSchema = None,
        columns_value: main_models.GetGovernanceItemReportResponseBodyColumnsValue = None,
        generate_time: str = None,
        is_truncated: bool = None,
        marker: str = None,
        metric_type: str = None,
        metric_value: Any = None,
        request_id: str = None,
    ):
        self.columns_schema = columns_schema
        self.columns_value = columns_value
        # The time when the report for the check item was generated.
        self.generate_time = generate_time
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_truncated = is_truncated
        # This parameter is returned only when `IsTruncated` is set to true. Use this parameter to retrieve the truncated content.
        self.marker = marker
        # The data type of the metric value. Valid values:
        # 
        # - Number: the numeric type.
        # 
        # - String: the string type.
        # 
        # - Boolean: the Boolean type.
        self.metric_type = metric_type
        # The metric value.
        self.metric_value = metric_value
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.columns_schema:
            self.columns_schema.validate()
        if self.columns_value:
            self.columns_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns_schema is not None:
            result['ColumnsSchema'] = self.columns_schema.to_map()

        if self.columns_value is not None:
            result['ColumnsValue'] = self.columns_value.to_map()

        if self.generate_time is not None:
            result['GenerateTime'] = self.generate_time

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnsSchema') is not None:
            temp_model = main_models.GetGovernanceItemReportResponseBodyColumnsSchema()
            self.columns_schema = temp_model.from_map(m.get('ColumnsSchema'))

        if m.get('ColumnsValue') is not None:
            temp_model = main_models.GetGovernanceItemReportResponseBodyColumnsValue()
            self.columns_value = temp_model.from_map(m.get('ColumnsValue'))

        if m.get('GenerateTime') is not None:
            self.generate_time = m.get('GenerateTime')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGovernanceItemReportResponseBodyColumnsValue(DaraModel):
    def __init__(
        self,
        column_row: List[main_models.GetGovernanceItemReportResponseBodyColumnsValueColumnRow] = None,
    ):
        self.column_row = column_row

    def validate(self):
        if self.column_row:
            for v1 in self.column_row:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnRow'] = []
        if self.column_row is not None:
            for k1 in self.column_row:
                result['ColumnRow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_row = []
        if m.get('ColumnRow') is not None:
            for k1 in m.get('ColumnRow'):
                temp_model = main_models.GetGovernanceItemReportResponseBodyColumnsValueColumnRow()
                self.column_row.append(temp_model.from_map(k1))

        return self

class GetGovernanceItemReportResponseBodyColumnsValueColumnRow(DaraModel):
    def __init__(
        self,
        column_value: List[Any] = None,
    ):
        self.column_value = column_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_value is not None:
            result['ColumnValue'] = self.column_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnValue') is not None:
            self.column_value = m.get('ColumnValue')

        return self

class GetGovernanceItemReportResponseBodyColumnsSchema(DaraModel):
    def __init__(
        self,
        column_schema: List[main_models.GetGovernanceItemReportResponseBodyColumnsSchemaColumnSchema] = None,
    ):
        self.column_schema = column_schema

    def validate(self):
        if self.column_schema:
            for v1 in self.column_schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnSchema'] = []
        if self.column_schema is not None:
            for k1 in self.column_schema:
                result['ColumnSchema'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_schema = []
        if m.get('ColumnSchema') is not None:
            for k1 in m.get('ColumnSchema'):
                temp_model = main_models.GetGovernanceItemReportResponseBodyColumnsSchemaColumnSchema()
                self.column_schema.append(temp_model.from_map(k1))

        return self

class GetGovernanceItemReportResponseBodyColumnsSchemaColumnSchema(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_type: str = None,
    ):
        self.column_name = column_name
        self.column_type = column_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        return self

