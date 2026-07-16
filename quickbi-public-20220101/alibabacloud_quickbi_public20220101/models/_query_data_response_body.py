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
        # The request ID.
        self.request_id = request_id
        # The result of the API call. Valid values:
        # 
        # - true: The call was successful.
        # 
        # - false: The call failed.
        self.result = result
        # Whether the request succeeded. Valid values:
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
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
    ):
        # The column headers.
        self.headers = headers
        # The SQL statement for the query.
        # 
        # > The returned SQL includes both the filter conditions from this call and any row-level or column-level permission rules.
        self.sql = sql
        # The query results.
        self.values = values

    def validate(self):
        if self.headers:
            for v1 in self.headers:
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
        # The aggregate operator. Returned only for measure fields.
        # 
        # - SUM: The sum.
        # 
        # - MAX: The maximum value.
        # 
        # - MIN: The minimum value.
        # 
        # - AVG: The average value.
        # 
        # - COUNT: The count.
        # 
        # - COUNTD: The count of unique values.
        # 
        # - STDDEV_POP: The population standard deviation.
        # 
        # - STDDEV_SAMP: The sample standard deviation.
        # 
        # - VAR_POP: The population variance.
        # 
        # - VAR_SAMP: The sample variance.
        self.aggregator = aggregator
        # The physical table field name.
        self.column = column
        # The field data type. Common types:
        # 
        # - number
        # 
        # - string
        # 
        # - date
        # 
        # - time
        # 
        # - datetime
        self.data_type = data_type
        # The dimension granularity. Returned only for date or geographic dimensions. Valid values:
        # 
        # - Date granularity: yearRegion (year), monthRegion (month), weekRegion (week), dayRegion (day), hourRegion (hour), minRegion (minute), secRegion (second)
        # 
        # - Geographic granularity: COUNTRY (country), PROVINCE (province), CITY (city), XIAN (county/district), REGION (region)
        self.granularity = granularity
        # The field alias. Used as the key in each Values map entry.
        self.label = label
        # The original field name in the dataset.
        self.original_column = original_column
        # Whether the field is a dimension or measure.
        # 
        # - Dimension
        # 
        # - Measure
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

