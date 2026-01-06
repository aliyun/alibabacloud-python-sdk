# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class EventCenterQueryEventsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.EventCenterQueryEventsRequestBody = None,
        bus_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The request body.
        # 
        # This parameter is required.
        self.body = body
        # The name of the event bus.
        self.bus_name = bus_name
        # The number of entries per page. Valid values: 0 to 10000. Default value: 100.
        self.max_results = max_results
        # 用来标记当前开始读取的位置。置空表示从头开始。
        self.next_token = next_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.bus_name is not None:
            result['BusName'] = self.bus_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.EventCenterQueryEventsRequestBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class EventCenterQueryEventsRequestBody(DaraModel):
    def __init__(
        self,
        parameters: main_models.EventCenterQueryEventsRequestBodyParameters = None,
        query_type: str = None,
        schema_id: str = None,
    ):
        # The query parameters.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The query type. Valid values:
        # 
        # *   **timeseries**: queries time series data.
        # *   **table**: queries table data.
        # *   **timeseries_and_table**: queries time series data and table data at the same time.
        # 
        # This parameter is required.
        self.query_type = query_type
        # The schema ID.
        # 
        # This parameter is required.
        self.schema_id = schema_id

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            temp_model = main_models.EventCenterQueryEventsRequestBodyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class EventCenterQueryEventsRequestBodyParameters(DaraModel):
    def __init__(
        self,
        breakdowns: List[str] = None,
        calculations: List[main_models.EventCenterQueryEventsRequestBodyParametersCalculations] = None,
        end_time: int = None,
        filter_combination: str = None,
        filters: List[main_models.EventCenterQueryEventsRequestBodyParametersFilters] = None,
        granularity: int = None,
        limit: int = None,
        offset: int = None,
        orders: List[main_models.EventCenterQueryEventsRequestBodyParametersOrders] = None,
        start_time: int = None,
        time_range: int = None,
    ):
        # Specifies whether to further split the dataset based on the column name.
        self.breakdowns = breakdowns
        # The operator that is used to calculate the specified column.
        self.calculations = calculations
        # The timestamp that specifies the end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The logic used to filter the combination of conditions.
        self.filter_combination = filter_combination
        # The filter conditions.
        self.filters = filters
        # The minimum time unit for querying time series data. Minimum value: 1. Unit: seconds. The value of this parameter is a recommended value. The actual value returned shall prevail.
        self.granularity = granularity
        # The maximum number of events to query. Valid values: 1 to 10000.
        self.limit = limit
        # The offset of the start position for this query. The offset starts from 0.
        self.offset = offset
        # The order of the query results. This parameter is valid only if you set QueryType to table.
        self.orders = orders
        # The timestamp that specifies the beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The time range during which events are queried. Minimum value: 1000. Unit: milliseconds.
        self.time_range = time_range

    def validate(self):
        if self.calculations:
            for v1 in self.calculations:
                 if v1:
                    v1.validate()
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()
        if self.orders:
            for v1 in self.orders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.breakdowns is not None:
            result['Breakdowns'] = self.breakdowns

        result['Calculations'] = []
        if self.calculations is not None:
            for k1 in self.calculations:
                result['Calculations'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filter_combination is not None:
            result['FilterCombination'] = self.filter_combination

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.offset is not None:
            result['Offset'] = self.offset

        result['Orders'] = []
        if self.orders is not None:
            for k1 in self.orders:
                result['Orders'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Breakdowns') is not None:
            self.breakdowns = m.get('Breakdowns')

        self.calculations = []
        if m.get('Calculations') is not None:
            for k1 in m.get('Calculations'):
                temp_model = main_models.EventCenterQueryEventsRequestBodyParametersCalculations()
                self.calculations.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FilterCombination') is not None:
            self.filter_combination = m.get('FilterCombination')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.EventCenterQueryEventsRequestBodyParametersFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        self.orders = []
        if m.get('Orders') is not None:
            for k1 in m.get('Orders'):
                temp_model = main_models.EventCenterQueryEventsRequestBodyParametersOrders()
                self.orders.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

class EventCenterQueryEventsRequestBodyParametersOrders(DaraModel):
    def __init__(
        self,
        column: str = None,
        desc: bool = None,
        op: str = None,
    ):
        # The column name.
        self.column = column
        # Specifies whether to sort the query results in descending order.
        self.desc = desc
        # The operator.
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.op is not None:
            result['Op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        return self

class EventCenterQueryEventsRequestBodyParametersFilters(DaraModel):
    def __init__(
        self,
        column: str = None,
        nested_filter_combination: str = None,
        nested_filters: List[main_models.EventCenterQueryEventsRequestBodyParametersFiltersNestedFilters] = None,
        op: str = None,
        values: List[str] = None,
    ):
        # The column name.
        self.column = column
        self.nested_filter_combination = nested_filter_combination
        self.nested_filters = nested_filters
        # The operator.
        self.op = op
        # The values that are used together with the operator.
        self.values = values

    def validate(self):
        if self.nested_filters:
            for v1 in self.nested_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.nested_filter_combination is not None:
            result['NestedFilterCombination'] = self.nested_filter_combination

        result['NestedFilters'] = []
        if self.nested_filters is not None:
            for k1 in self.nested_filters:
                result['NestedFilters'].append(k1.to_map() if k1 else None)

        if self.op is not None:
            result['Op'] = self.op

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('NestedFilterCombination') is not None:
            self.nested_filter_combination = m.get('NestedFilterCombination')

        self.nested_filters = []
        if m.get('NestedFilters') is not None:
            for k1 in m.get('NestedFilters'):
                temp_model = main_models.EventCenterQueryEventsRequestBodyParametersFiltersNestedFilters()
                self.nested_filters.append(temp_model.from_map(k1))

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class EventCenterQueryEventsRequestBodyParametersFiltersNestedFilters(DaraModel):
    def __init__(
        self,
        column: str = None,
        op: str = None,
        values: List[str] = None,
    ):
        self.column = column
        self.op = op
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.op is not None:
            result['Op'] = self.op

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class EventCenterQueryEventsRequestBodyParametersCalculations(DaraModel):
    def __init__(
        self,
        column: str = None,
        op: str = None,
    ):
        # The column name.
        self.column = column
        # The operator.
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.op is not None:
            result['Op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        return self

