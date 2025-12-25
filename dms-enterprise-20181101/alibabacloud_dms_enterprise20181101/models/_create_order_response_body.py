# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateOrderResponseBody(DaraModel):
    def __init__(
        self,
        create_order_result: main_models.CreateOrderResponseBodyCreateOrderResult = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the ticket.
        self.create_order_result = create_order_result
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.create_order_result:
            self.create_order_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            temp_model = main_models.CreateOrderResponseBodyCreateOrderResult()
            self.create_order_result = temp_model.from_map(m.get('CreateOrderResult'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateOrderResponseBodyCreateOrderResult(DaraModel):
    def __init__(
        self,
        order_ids: List[int] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')

        return self

