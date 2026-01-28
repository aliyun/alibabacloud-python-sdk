# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20181015 import models as main_models
from darabonba.model import DaraModel

class MetricQueryRequest(DaraModel):
    def __init__(
        self,
        dimensions: List[str] = None,
        end_time: int = None,
        filters: List[main_models.MetricQueryRequestFilters] = None,
        hacker_user_id: str = None,
        iinterval_in_sec: int = None,
        limit: int = None,
        measures: List[str] = None,
        metric: str = None,
        order: str = None,
        order_by: str = None,
        security_token: str = None,
        start_time: int = None,
    ):
        self.dimensions = dimensions
        # This parameter is required.
        self.end_time = end_time
        self.filters = filters
        self.hacker_user_id = hacker_user_id
        self.iinterval_in_sec = iinterval_in_sec
        self.limit = limit
        # This parameter is required.
        self.measures = measures
        # This parameter is required.
        self.metric = metric
        self.order = order
        self.order_by = order_by
        self.security_token = security_token
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.hacker_user_id is not None:
            result['HackerUserId'] = self.hacker_user_id

        if self.iinterval_in_sec is not None:
            result['IintervalInSec'] = self.iinterval_in_sec

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.measures is not None:
            result['Measures'] = self.measures

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.MetricQueryRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('HackerUserId') is not None:
            self.hacker_user_id = m.get('HackerUserId')

        if m.get('IintervalInSec') is not None:
            self.iinterval_in_sec = m.get('IintervalInSec')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Measures') is not None:
            self.measures = m.get('Measures')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class MetricQueryRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

