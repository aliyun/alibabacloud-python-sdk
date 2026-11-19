# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDataResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the API. Valid values:
        # 
        # - true: The execution is successful.
        # - false: The execution fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryDataResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        headers: List[main_models.QueryDataResponseBodyResultHeaders] = None,
        sql: str = None,
        values: List[Dict[str, Any]] = None,
        values_v2: List[main_models.QueryDataResponseBodyResultValuesV2] = None,
    ):
        # The column headers.
        self.headers = headers
        # The SQL statement of the query.
        # > In addition to the parameter conditions of the current API, the filter conditions in the returned SQL statement also include the row-level and column-level permission configurations.
        self.sql = sql
        # The returned query results.
        self.values = values
        # The returned query results, including the original value fields.
        self.values_v2 = values_v2

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()
        if self.values_v2:
            for v1 in self.values_v2:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.values is not None:
            result['Values'] = self.values

        result['ValuesV2'] = []
        if self.values_v2 is not None:
            for k1 in self.values_v2:
                result['ValuesV2'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.QueryDataResponseBodyResultHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        self.values_v2 = []
        if m.get('ValuesV2') is not None:
            for k1 in m.get('ValuesV2'):
                temp_model = main_models.QueryDataResponseBodyResultValuesV2()
                self.values_v2.append(temp_model.from_map(k1))

        return self

class QueryDataResponseBodyResultValuesV2(DaraModel):
    def __init__(
        self,
        row_value: List[main_models.QueryDataResponseBodyResultValuesV2RowValue] = None,
    ):
        # The row values.
        self.row_value = row_value

    def validate(self):
        if self.row_value:
            for v1 in self.row_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RowValue'] = []
        if self.row_value is not None:
            for k1 in self.row_value:
                result['RowValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.row_value = []
        if m.get('RowValue') is not None:
            for k1 in m.get('RowValue'):
                temp_model = main_models.QueryDataResponseBodyResultValuesV2RowValue()
                self.row_value.append(temp_model.from_map(k1))

        return self

class QueryDataResponseBodyResultValuesV2RowValue(DaraModel):
    def __init__(
        self,
        l: str = None,
        r: str = None,
        v: str = None,
    ):
        # The field alias set in Data Service.
        self.l = l
        # The original value.
        self.r = r
        # The display value.
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.l is not None:
            result['L'] = self.l

        if self.r is not None:
            result['R'] = self.r

        if self.v is not None:
            result['V'] = self.v

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('L') is not None:
            self.l = m.get('L')

        if m.get('R') is not None:
            self.r = m.get('R')

        if m.get('V') is not None:
            self.v = m.get('V')

        return self

class QueryDataResponseBodyResultHeaders(DaraModel):
    def __init__(
        self,
        aggregator: str = None,
        column: str = None,
        data_type: str = None,
        granularity: str = None,
        label: str = None,
        original_column: str = None,
        type: str = None,
    ):
        # The aggregation operator. This field is available only for measure fields, such as SUM, AVG, and MAX. Valid values:
        # - SUM: Sum.
        # - MAX: Maximum value.
        # - MIN: Minimum value.
        # - AVG: Average value.
        # - COUNT: Count.
        # - COUNTD: Deduplicate count.
        # - STDDEV_POP: Population standard deviation.
        # - STDDEV_SAMP: Sample standard deviation.
        # - VAR_POP: Population variance.
        # - VAR_SAMP: Sample variance.
        self.aggregator = aggregator
        # The name of the field, which corresponds to the field name in the physical table.
        self.column = column
        # The data type of the field. Valid values:
        # - number: Numeric.
        # - string: String.
        # - date: Date.
        # - time: Time.
        # - datetime: Date and time.
        self.data_type = data_type
        # The granularity of the dimension field. This field is returned only when the requested field is a date dimension or a geographic dimension. Valid values:
        # 
        # - Date granularity: yearRegion (year), monthRegion (month), weekRegion (week), dayRegion (day), hourRegion (hour), minRegion (minute), and secRegion (second).
        # 
        # - Geographic granularity: COUNTRY (country), PROVINCE (province), CITY (city), XIAN (district/county), and REGION (region).
        self.granularity = granularity
        # The alias of the field, which is the key of the map data row in the values result parameter.
        self.label = label
        # The original name of the corresponding field in the dataset.
        self.original_column = original_column
        # The type of the field, which is used to distinguish whether the field is a dimension or a measure. Valid values:
        # - Dimension: Dimension.
        # - Measure: Measure.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator

        if self.column is not None:
            result['Column'] = self.column

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.label is not None:
            result['Label'] = self.label

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')

        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

