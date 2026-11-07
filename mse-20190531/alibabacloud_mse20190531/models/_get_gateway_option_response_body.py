# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayOptionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GatewayOption = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The gateway operation details.
        # 
        # - **TraceDetails**: The XTrace sampling description. It includes TraceEnabled, which indicates whether XTrace is enabled, and Sample, which indicates the XTrace sampling rate.
        # 
        # - **LogConfigDetails**: The log delivery service description. It includes LogEnabled, which indicates whether log delivery to Simple Log Service (SLS) is enabled, ProjectName, which indicates the destination project for log delivery, and LogStoreName, which indicates the Logstore name.
        # 
        # - **EnableHardwareAcceleration**: Indicates whether hardware acceleration is enabled.
        # 
        # - **DisableHttp2Alpn**: Indicates whether HTTP/2 is disabled.
        # 
        # - **EnableWaf**: Indicates whether Web Application Firewall (WAF) is enabled.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        # 
        # - If the request is successful, a success message is returned.
        # - If the request fails, the cause of the failure is returned, such as TaskId not found.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The request result. Valid values:
        # - `true`: The request is successful.
        # - `false`: The request fails.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GatewayOption()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

