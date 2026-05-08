# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class QuerySingleActivityInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.QuerySingleActivityInfoResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySingleActivityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySingleActivityInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        channel_name: str = None,
        company_name: str = None,
        customer_name: str = None,
        email: str = None,
        id: int = None,
        is_vip_customer: str = None,
        mobile: str = None,
        qrcode: str = None,
        report_fields: str = None,
    ):
        self.activity_id = activity_id
        self.channel_name = channel_name
        self.company_name = company_name
        self.customer_name = customer_name
        self.email = email
        self.id = id
        self.is_vip_customer = is_vip_customer
        self.mobile = mobile
        self.qrcode = qrcode
        self.report_fields = report_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.email is not None:
            result['Email'] = self.email

        if self.id is not None:
            result['Id'] = self.id

        if self.is_vip_customer is not None:
            result['IsVipCustomer'] = self.is_vip_customer

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.qrcode is not None:
            result['QRCode'] = self.qrcode

        if self.report_fields is not None:
            result['ReportFields'] = self.report_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsVipCustomer') is not None:
            self.is_vip_customer = m.get('IsVipCustomer')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')

        if m.get('ReportFields') is not None:
            self.report_fields = m.get('ReportFields')

        return self

