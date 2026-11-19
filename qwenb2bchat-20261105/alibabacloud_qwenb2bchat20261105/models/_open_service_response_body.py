# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qwenb2bchat20261105 import models as main_models
from darabonba.model import DaraModel

class OpenServiceResponseBody(DaraModel):
    def __init__(
        self,
        error: main_models.OpenServiceResponseBodyError = None,
        order_id: str = None,
        sp_instance_id: str = None,
        status: str = None,
    ):
        # The details of a non-2xx error response, which are mutually exclusive with the status, orderId, and spInstanceId of a normal response.
        self.error = error
        # The order ID associated with the service activation process. Returned when an order exists.
        self.order_id = order_id
        # The service instance ID returned after successful activation and settlement.
        self.sp_instance_id = sp_instance_id
        # The test or activation result. TEST_OK indicates that the call validation succeeded.
        self.status = status

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.sp_instance_id is not None:
            result['spInstanceId'] = self.sp_instance_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            temp_model = main_models.OpenServiceResponseBodyError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('spInstanceId') is not None:
            self.sp_instance_id = m.get('spInstanceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class OpenServiceResponseBodyError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code recognizable by programs.
        # 
        # This parameter is required.
        self.code = code
        # The error description.
        # 
        # This parameter is required.
        self.message = message
        # The correlation ID of the current call.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

