# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class InquiryPriceRefundInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InquiryPriceRefundInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # data
        self.data = data
        # The description of the execution result.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
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
            temp_model = main_models.InquiryPriceRefundInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InquiryPriceRefundInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        host_id: str = None,
        instance_id: str = None,
        refund_amount: float = None,
    ):
        # The currency.
        self.currency = currency
        # The site of the execution host.
        self.host_id = host_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The refundable amount.
        self.refund_amount = refund_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')

        return self

