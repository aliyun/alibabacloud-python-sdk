# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class DeleteAggregatorsResponseBody(DaraModel):
    def __init__(
        self,
        operate_aggregators_result: main_models.DeleteAggregatorsResponseBodyOperateAggregatorsResult = None,
        request_id: str = None,
    ):
        # The returned result.
        self.operate_aggregators_result = operate_aggregators_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.operate_aggregators_result:
            self.operate_aggregators_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_aggregators_result is not None:
            result['OperateAggregatorsResult'] = self.operate_aggregators_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateAggregatorsResult') is not None:
            temp_model = main_models.DeleteAggregatorsResponseBodyOperateAggregatorsResult()
            self.operate_aggregators_result = temp_model.from_map(m.get('OperateAggregatorsResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteAggregatorsResponseBodyOperateAggregatorsResult(DaraModel):
    def __init__(
        self,
        operate_aggregators: List[main_models.DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators] = None,
    ):
        # The details of the account group.
        self.operate_aggregators = operate_aggregators

    def validate(self):
        if self.operate_aggregators:
            for v1 in self.operate_aggregators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperateAggregators'] = []
        if self.operate_aggregators is not None:
            for k1 in self.operate_aggregators:
                result['OperateAggregators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_aggregators = []
        if m.get('OperateAggregators') is not None:
            for k1 in m.get('OperateAggregators'):
                temp_model = main_models.DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators()
                self.operate_aggregators.append(temp_model.from_map(k1))

        return self

class DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        # The ID of the account group.
        self.aggregator_id = aggregator_id
        # The error code returned.
        # 
        # > No error code is returned for the account group if the account group is deleted.
        self.error_code = error_code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

