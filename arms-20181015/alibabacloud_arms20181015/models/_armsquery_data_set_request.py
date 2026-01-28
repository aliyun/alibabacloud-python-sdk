# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20181015 import models as main_models
from darabonba.model import DaraModel

class ARMSQueryDataSetRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        date_str: str = None,
        dimensions: List[main_models.ARMSQueryDataSetRequestDimensions] = None,
        hacker_user_id: str = None,
        hungry_mode: bool = None,
        interval_in_sec: int = None,
        is_drill_down: bool = None,
        limit: int = None,
        max_time: int = None,
        measures: List[str] = None,
        min_time: int = None,
        optional_dims: List[main_models.ARMSQueryDataSetRequestOptionalDims] = None,
        order_by_key: str = None,
        reduce_tail: bool = None,
        required_dims: List[main_models.ARMSQueryDataSetRequestRequiredDims] = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.dataset_id = dataset_id
        self.date_str = date_str
        self.dimensions = dimensions
        self.hacker_user_id = hacker_user_id
        self.hungry_mode = hungry_mode
        # This parameter is required.
        self.interval_in_sec = interval_in_sec
        self.is_drill_down = is_drill_down
        self.limit = limit
        # This parameter is required.
        self.max_time = max_time
        self.measures = measures
        # This parameter is required.
        self.min_time = min_time
        self.optional_dims = optional_dims
        self.order_by_key = order_by_key
        self.reduce_tail = reduce_tail
        self.required_dims = required_dims
        self.security_token = security_token

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()
        if self.optional_dims:
            for v1 in self.optional_dims:
                 if v1:
                    v1.validate()
        if self.required_dims:
            for v1 in self.required_dims:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.date_str is not None:
            result['DateStr'] = self.date_str

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.hacker_user_id is not None:
            result['HackerUserId'] = self.hacker_user_id

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
            for k1 in self.optional_dims:
                result['OptionalDims'].append(k1.to_map() if k1 else None)

        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key

        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail

        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k1 in self.required_dims:
                result['RequiredDims'].append(k1.to_map() if k1 else None)

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ARMSQueryDataSetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('HackerUserId') is not None:
            self.hacker_user_id = m.get('HackerUserId')

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
            for k1 in m.get('OptionalDims'):
                temp_model = main_models.ARMSQueryDataSetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k1))

        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')

        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')

        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k1 in m.get('RequiredDims'):
                temp_model = main_models.ARMSQueryDataSetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k1))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

class ARMSQueryDataSetRequestRequiredDims(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ARMSQueryDataSetRequestOptionalDims(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ARMSQueryDataSetRequestDimensions(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

