# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ARMSQueryDataSetRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequestOptionalDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequestRequiredDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        date_str: int = None,
        dimensions: List[ARMSQueryDataSetRequestDimensions] = None,
        hungry_mode: bool = None,
        interval_in_sec: int = None,
        is_drill_down: bool = None,
        limit: int = None,
        max_time: int = None,
        measures: List[str] = None,
        min_time: int = None,
        optional_dims: List[ARMSQueryDataSetRequestOptionalDims] = None,
        order_by_key: str = None,
        reduce_tail: bool = None,
        required_dims: List[ARMSQueryDataSetRequestRequiredDims] = None,
    ):
        self.dataset_id = dataset_id
        self.date_str = date_str
        self.dimensions = dimensions
        self.hungry_mode = hungry_mode
        self.interval_in_sec = interval_in_sec
        self.is_drill_down = is_drill_down
        self.limit = limit
        self.max_time = max_time
        self.measures = measures
        self.min_time = min_time
        self.optional_dims = optional_dims
        self.order_by_key = order_by_key
        self.reduce_tail = reduce_tail
        self.required_dims = required_dims

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.optional_dims:
            for k in self.optional_dims:
                if k:
                    k.validate()
        if self.required_dims:
            for k in self.required_dims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.hungry_mode is not None:
            result['HungryMode'] = self.hungry_mode
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        result['OptionalDims'] = []
        if self.optional_dims is not None:
            for k in self.optional_dims:
                result['OptionalDims'].append(k.to_map() if k else None)
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k in self.required_dims:
                result['RequiredDims'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ARMSQueryDataSetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('HungryMode') is not None:
            self.hungry_mode = m.get('HungryMode')
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        self.optional_dims = []
        if m.get('OptionalDims') is not None:
            for k in m.get('OptionalDims'):
                temp_model = ARMSQueryDataSetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k))
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k in m.get('RequiredDims'):
                temp_model = ARMSQueryDataSetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k))
        return self


class ARMSQueryDataSetResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ARMSQueryDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ARMSQueryDataSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ARMSQueryDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WhereInDimQueryRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class WhereInDimQueryRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        date_str: str = None,
        dimensions: List[WhereInDimQueryRequestDimensions] = None,
        interval_in_sec: int = None,
        is_drill_down: bool = None,
        limit: int = None,
        max_time: int = None,
        measures: List[str] = None,
        min_time: int = None,
        order_by_key: str = None,
        reduce_tail: bool = None,
        where_in_key: str = None,
        where_in_values: List[str] = None,
    ):
        self.dataset_id = dataset_id
        self.date_str = date_str
        self.dimensions = dimensions
        self.interval_in_sec = interval_in_sec
        self.is_drill_down = is_drill_down
        self.limit = limit
        self.max_time = max_time
        self.measures = measures
        self.min_time = min_time
        self.order_by_key = order_by_key
        self.reduce_tail = reduce_tail
        self.where_in_key = where_in_key
        self.where_in_values = where_in_values

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        if self.where_in_key is not None:
            result['WhereInKey'] = self.where_in_key
        if self.where_in_values is not None:
            result['WhereInValues'] = self.where_in_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = WhereInDimQueryRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        if m.get('WhereInKey') is not None:
            self.where_in_key = m.get('WhereInKey')
        if m.get('WhereInValues') is not None:
            self.where_in_values = m.get('WhereInValues')
        return self


class WhereInDimQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class WhereInDimQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WhereInDimQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = WhereInDimQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


