# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QueryCustomizeFlowStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.QueryCustomizeFlowStrategyResponseBodyResultObject] = None,
        success: bool = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # ID of this request.
        self.request_id = request_id
        # Processing result.
        self.result_object = result_object
        # Whether the response was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.QueryCustomizeFlowStrategyResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCustomizeFlowStrategyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        accumulate_key: str = None,
        accumulate_window: str = None,
        api_name: str = None,
        flow_type: str = None,
        id: str = None,
        operation: str = None,
        status: str = None,
        threshold: str = None,
        user_id: str = None,
    ):
        # AccumulateKey
        self.accumulate_key = accumulate_key
        # Flow control statistical window, unit: **minutes**.
        self.accumulate_window = accumulate_window
        # API name, same as **ProductCode**.
        self.api_name = api_name
        # Flow type:
        # - **ACCUMULATE**: ID card reappears
        # - **PASSED_RATE**: Pass rate less than
        # - **SUB_CODE_205**: Authentication failed and liveness attack 205 ratio greater than
        # - **SUB_CODE_206**: Authentication failed and liveness attack 206 ratio greater than
        self.flow_type = flow_type
        # Rule ID.
        self.id = id
        # Operation.
        self.operation = operation
        # Status:
        # - **disabled**: Disabled
        # - **normal**: Enabled
        self.status = status
        # Threshold.
        self.threshold = threshold
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accumulate_key is not None:
            result['AccumulateKey'] = self.accumulate_key

        if self.accumulate_window is not None:
            result['AccumulateWindow'] = self.accumulate_window

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.id is not None:
            result['Id'] = self.id

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.status is not None:
            result['Status'] = self.status

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulateKey') is not None:
            self.accumulate_key = m.get('AccumulateKey')

        if m.get('AccumulateWindow') is not None:
            self.accumulate_window = m.get('AccumulateWindow')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

