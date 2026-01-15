# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class TestModelResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        request_id: str = None,
        result_object: main_models.TestModelResponseBodyResultObject = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.result_object = result_object
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.TestModelResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TestModelResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        consistency_count: int = None,
        consistency_rate: float = None,
        test_result: List[main_models.TestModelResponseBodyResultObjectTestResult] = None,
        total: int = None,
    ):
        self.consistency_count = consistency_count
        self.consistency_rate = consistency_rate
        self.test_result = test_result
        self.total = total

    def validate(self):
        if self.test_result:
            for v1 in self.test_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistency_count is not None:
            result['ConsistencyCount'] = self.consistency_count

        if self.consistency_rate is not None:
            result['ConsistencyRate'] = self.consistency_rate

        result['TestResult'] = []
        if self.test_result is not None:
            for k1 in self.test_result:
                result['TestResult'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistencyCount') is not None:
            self.consistency_count = m.get('ConsistencyCount')

        if m.get('ConsistencyRate') is not None:
            self.consistency_rate = m.get('ConsistencyRate')

        self.test_result = []
        if m.get('TestResult') is not None:
            for k1 in m.get('TestResult'):
                temp_model = main_models.TestModelResponseBodyResultObjectTestResult()
                self.test_result.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class TestModelResponseBodyResultObjectTestResult(DaraModel):
    def __init__(
        self,
        actual_result: str = None,
        consistency: bool = None,
        test_result: str = None,
        train_result: str = None,
    ):
        self.actual_result = actual_result
        self.consistency = consistency
        self.test_result = test_result
        self.train_result = train_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_result is not None:
            result['ActualResult'] = self.actual_result

        if self.consistency is not None:
            result['Consistency'] = self.consistency

        if self.test_result is not None:
            result['TestResult'] = self.test_result

        if self.train_result is not None:
            result['TrainResult'] = self.train_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualResult') is not None:
            self.actual_result = m.get('ActualResult')

        if m.get('Consistency') is not None:
            self.consistency = m.get('Consistency')

        if m.get('TestResult') is not None:
            self.test_result = m.get('TestResult')

        if m.get('TrainResult') is not None:
            self.train_result = m.get('TrainResult')

        return self

