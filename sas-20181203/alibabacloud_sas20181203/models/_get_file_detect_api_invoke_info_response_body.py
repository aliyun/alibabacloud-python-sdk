# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileDetectApiInvokeInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileDetectApiInvokeInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # Returns the response body.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileDetectApiInvokeInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileDetectApiInvokeInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_count: int = None,
        auth_count_in_sale_version: int = None,
        expire: int = None,
        flow_rate: int = None,
        invoke_count: int = None,
        invoke_count_in_sale_version: int = None,
        remain_auth_count: int = None,
        sale_version: int = None,
        time_unit: str = None,
    ):
        # The total number of authorizations.
        self.auth_count = auth_count
        # The total number of authorizations(excluding trials).
        self.auth_count_in_sale_version = auth_count_in_sale_version
        # The timestamp of the expiration date of the authorization number.
        self.expire = expire
        # The frequency of calls.
        self.flow_rate = flow_rate
        # The number of authorizations used.
        self.invoke_count = invoke_count
        # The number of authorizations used(excluding trials).
        self.invoke_count_in_sale_version = invoke_count_in_sale_version
        # The number of remaining authorizations.
        self.remain_auth_count = remain_auth_count
        # The Authorized Version. Valid values include:
        # 
        # * **1:** trial version
        # * **2:** Enterprise Edition
        self.sale_version = sale_version
        # The time unit of the frequency limit. Value:
        # 
        # * **SECONDS**
        # * **MINUTES**
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_count is not None:
            result['AuthCount'] = self.auth_count

        if self.auth_count_in_sale_version is not None:
            result['AuthCountInSaleVersion'] = self.auth_count_in_sale_version

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.flow_rate is not None:
            result['FlowRate'] = self.flow_rate

        if self.invoke_count is not None:
            result['InvokeCount'] = self.invoke_count

        if self.invoke_count_in_sale_version is not None:
            result['InvokeCountInSaleVersion'] = self.invoke_count_in_sale_version

        if self.remain_auth_count is not None:
            result['RemainAuthCount'] = self.remain_auth_count

        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCount') is not None:
            self.auth_count = m.get('AuthCount')

        if m.get('AuthCountInSaleVersion') is not None:
            self.auth_count_in_sale_version = m.get('AuthCountInSaleVersion')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('FlowRate') is not None:
            self.flow_rate = m.get('FlowRate')

        if m.get('InvokeCount') is not None:
            self.invoke_count = m.get('InvokeCount')

        if m.get('InvokeCountInSaleVersion') is not None:
            self.invoke_count_in_sale_version = m.get('InvokeCountInSaleVersion')

        if m.get('RemainAuthCount') is not None:
            self.remain_auth_count = m.get('RemainAuthCount')

        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

