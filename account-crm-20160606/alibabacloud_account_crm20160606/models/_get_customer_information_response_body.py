# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetCustomerInformationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomerInformationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetCustomerInformationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomerInformationResponseBodyData(DaraModel):
    def __init__(
        self,
        biz: str = None,
        customer_category: str = None,
        website: str = None,
    ):
        self.biz = biz
        self.customer_category = customer_category
        self.website = website

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.customer_category is not None:
            result['CustomerCategory'] = self.customer_category

        if self.website is not None:
            result['Website'] = self.website

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('CustomerCategory') is not None:
            self.customer_category = m.get('CustomerCategory')

        if m.get('Website') is not None:
            self.website = m.get('Website')

        return self

