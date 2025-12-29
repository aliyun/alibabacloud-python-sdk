# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateGreyTagRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information about the canary release rule.
        self.data = data
        # The error code. Valid values:
        # 
        # *   **ErrorCode** is not returned if a request is successful.
        # *   **ErrorCode** is returned if a request failed. For more information, see **Error code** section of this topic.
        self.error_code = error_code
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the information of the change order was queried. Valid values:
        # 
        # *   **true**: The information was queried.
        # *   **false**: The information failed to be queried.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class CreateGreyTagRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        # The ID of the canary release rule. The ID is globally unique.
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')

        return self

