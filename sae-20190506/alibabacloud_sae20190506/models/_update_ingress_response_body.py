# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateIngressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # API status or POP error code. Details are as follows:
        # 
        # - **2xx**: Success.
        # 
        # - **3xx**: Redirection.
        # 
        # - **4xx**: Request error.
        # 
        # - **5xx**: Server error.
        self.code = code
        # Returned result.
        self.data = data
        # Error code. Details are as follows:
        # 
        # - If the request is successful, the **ErrorCode** field is not returned.
        # 
        # - If the request failed, the **ErrorCode** field is returned. For more information, see the **Error Codes** list in this topic.
        self.error_code = error_code
        # Additional information. Details are as follows:
        # 
        # - If the request is normal, **success** is returned.
        # 
        # - If the request is abnormal, a specific abnormal error code is returned.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the Ingress instance configuration was successfully updated. Details are as follows:
        # 
        # - **true**: The update was successful.
        # 
        # - **false**: The update failed.
        self.success = success
        # Call chain ID.
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
            temp_model = main_models.UpdateIngressResponseBodyData()
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

class UpdateIngressResponseBodyData(DaraModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        # Routing rule ID.
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')

        return self

