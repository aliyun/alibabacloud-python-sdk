# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDataServiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDataServiceResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The query result returned by the API.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # 
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
            temp_model = main_models.QueryDataServiceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDataServiceResponseBodyResult(DaraModel):
    def __init__(
        self,
        headers: List[main_models.QueryDataServiceResponseBodyResultHeaders] = None,
        sql: str = None,
        values: List[Dict[str, Any]] = None,
    ):
        # The column headers.
        self.headers = headers
        # The SQL statement of the query request.
        self.sql = sql
        # The returned query results.
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
                temp_model = main_models.QueryDataServiceResponseBodyResultHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class QueryDataServiceResponseBodyResultHeaders(DaraModel):
    def __init__(
        self,
        aggregator: str = None,
        column: str = None,
        data_type: str = None,
        granularity: str = None,
        label: str = None,
        type: str = None,
    ):
        # The aggregation operator. This parameter is returned only for measure fields, such as SUM, AVG, and MAX.
        self.aggregator = aggregator
        # The name of the field, which corresponds to the field name in the physical table.
        self.column = column
        # The data type of the field. Common values include number, string, date, datetime, time, and geographic.
        self.data_type = data_type
        # The granularity of the dimension field. This parameter is returned only when the requested field is a date dimension or geographic dimension field. Valid values:
        # 
        # - Date granularity: yearRegion (year), monthRegion (month), weekRegion (week), dayRegion (day), hourRegion (hour), minRegion (minute), and secRegion (second).
        # 
        # - Geographic information granularity: COUNTRY (country level), PROVINCE (province level), CITY (city level), XIAN (district or county level), and REGION (region level).
        self.granularity = granularity
        # The alias of the field, which is the key of the map data row in the Values response parameter.
        self.label = label
        # The type of the field, which is used to distinguish whether the field is a dimension or a measure.
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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

