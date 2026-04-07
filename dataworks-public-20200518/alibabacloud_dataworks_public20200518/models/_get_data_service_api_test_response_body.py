# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApiTestResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataServiceApiTestResponseBodyData = None,
        request_id: str = None,
    ):
        # Return object
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataServiceApiTestResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataServiceApiTestResponseBodyData(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        cost_time: str = None,
        debug_info: str = None,
        nodes_debug_info: str = None,
        param_map: str = None,
        ret_code: int = None,
        ret_result: str = None,
        status: str = None,
    ):
        # Test API Id
        self.api_id = api_id
        # Time consuming
        self.cost_time = cost_time
        # Debug information
        self.debug_info = debug_info
        # Node Debug information
        self.nodes_debug_info = nodes_debug_info
        # Test API request parameters
        self.param_map = param_map
        # The test API returns the code. If it is not completed, the data is empty.
        self.ret_code = ret_code
        # Return data
        self.ret_result = ret_result
        # Whether the task has been completed, including: RUNNING,FINISHED
        self.status = status

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

        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info

        if self.nodes_debug_info is not None:
            result['NodesDebugInfo'] = self.nodes_debug_info

        if self.param_map is not None:
            result['ParamMap'] = self.param_map

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_result is not None:
            result['RetResult'] = self.ret_result

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')

        if m.get('NodesDebugInfo') is not None:
            self.nodes_debug_info = m.get('NodesDebugInfo')

        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetResult') is not None:
            self.ret_result = m.get('RetResult')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

