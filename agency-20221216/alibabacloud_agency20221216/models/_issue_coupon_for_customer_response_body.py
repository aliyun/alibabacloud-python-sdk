# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class IssueCouponForCustomerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        data: main_models.IssueCouponForCustomerResponseBodyData = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.data = data

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('data') is not None:
            temp_model = main_models.IssueCouponForCustomerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class IssueCouponForCustomerResponseBodyData(DaraModel):
    def __init__(
        self,
        coupon_template_id: int = None,
        create_time: str = None,
        uidlist: str = None,
    ):
        self.coupon_template_id = coupon_template_id
        self.create_time = create_time
        self.uidlist = uidlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_template_id is not None:
            result['CouponTemplateId'] = self.coupon_template_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.uidlist is not None:
            result['Uidlist'] = self.uidlist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponTemplateId') is not None:
            self.coupon_template_id = m.get('CouponTemplateId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Uidlist') is not None:
            self.uidlist = m.get('Uidlist')

        return self

