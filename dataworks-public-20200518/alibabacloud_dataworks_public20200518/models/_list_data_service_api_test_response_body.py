# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiTestResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataServiceApiTestResponseBodyData] = None,
        request_id: str = None,
    ):
        # The list of test records.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataServiceApiTestResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataServiceApiTestResponseBodyData(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        cost_time: int = None,
        create_time: int = None,
        param_map: str = None,
        ret_code: int = None,
        ret_result: str = None,
        status: str = None,
        test_id: int = None,
    ):
        # The ID of the DataService Studio API on which the test is performed.
        self.api_id = api_id
        # The time that is consumed to complete the test.
        self.cost_time = cost_time
        # The time when the test was initiated.
        self.create_time = create_time
        # The request parameters configured for the test.
        self.param_map = param_map
        # The status code returned for the test. If the test is not complete, this parameter is not returned.
        self.ret_code = ret_code
        # The result returned for the test.
        self.ret_result = ret_result
        # The status of the test. Valid values: RUNNING and FINISHED.
        self.status = status
        # The ID of the test.
        self.test_id = test_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.param_map is not None:
            result['ParamMap'] = self.param_map

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_result is not None:
            result['RetResult'] = self.ret_result

        if self.status is not None:
            result['Status'] = self.status

        if self.test_id is not None:
            result['TestId'] = self.test_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetResult') is not None:
            self.ret_result = m.get('RetResult')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')

        return self

