# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DeleteGreyTagRouteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request is successful.
        # 
        # - **3xx**: The request is redirected.
        # 
        # - **4xx**: A request error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The information about the grey tag route.
        self.data = data
        # The error code. The following describes when this field is returned:
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section of this topic.
        self.error_code = error_code
        # The response message. Valid values:
        # 
        # - **success** is returned if the request is successful.
        # 
        # - An error message is returned if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.success = success
        # The trace ID. You can use this ID to query call details.
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
            temp_model = main_models.DeleteGreyTagRouteResponseBodyData()
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

class DeleteGreyTagRouteResponseBodyData(DaraModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        # The globally unique ID of the grey tag route.
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

