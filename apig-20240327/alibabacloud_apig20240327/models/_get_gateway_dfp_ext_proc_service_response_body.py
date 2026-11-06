# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayDfpExtProcServiceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayDfpExtProcServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request result code. The value is Ok if the request succeeds.
        self.code = code
        # The binding information of the dynamic forwarding ExtProc service for the gateway.
        self.data = data
        # The result description. This field contains the fault information if the request fails.
        self.message = message
        # The request ID for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGatewayDfpExtProcServiceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayDfpExtProcServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        bound: bool = None,
        service_id: str = None,
        service_port: int = None,
    ):
        # Indicates whether the gateway is bound to a dynamic forwarding ExtProc service.
        self.bound = bound
        # The ID of the bound ExtProc gRPC service. This field is not returned if no service is bound.
        self.service_id = service_id
        # The gRPC port of the bound service. This field is not returned if no service is bound.
        self.service_port = service_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound is not None:
            result['bound'] = self.bound

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_port is not None:
            result['servicePort'] = self.service_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bound') is not None:
            self.bound = m.get('bound')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('servicePort') is not None:
            self.service_port = m.get('servicePort')

        return self

