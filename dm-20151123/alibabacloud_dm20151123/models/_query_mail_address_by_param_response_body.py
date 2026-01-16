# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryMailAddressByParamResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryMailAddressByParamResponseBodyData = None,
    ):
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # List of sending addresses
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryMailAddressByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryMailAddressByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        mail_address: List[main_models.QueryMailAddressByParamResponseBodyDataMailAddress] = None,
    ):
        self.mail_address = mail_address

    def validate(self):
        if self.mail_address:
            for v1 in self.mail_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mailAddress'] = []
        if self.mail_address is not None:
            for k1 in self.mail_address:
                result['mailAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mail_address = []
        if m.get('mailAddress') is not None:
            for k1 in m.get('mailAddress'):
                temp_model = main_models.QueryMailAddressByParamResponseBodyDataMailAddress()
                self.mail_address.append(temp_model.from_map(k1))

        return self

class QueryMailAddressByParamResponseBodyDataMailAddress(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_status: str = None,
        config_set_id: str = None,
        config_set_name: str = None,
        create_time: str = None,
        daily_count: str = None,
        daily_req_count: str = None,
        domain_status: str = None,
        mail_address_id: str = None,
        month_count: str = None,
        month_req_count: str = None,
        reply_address: str = None,
        reply_status: str = None,
        sendtype: str = None,
    ):
        # Sending address
        self.account_name = account_name
        # Account status, frozen: 1, normal: 0.
        self.account_status = account_status
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Creation time
        self.create_time = create_time
        # Daily quota limit
        self.daily_count = daily_count
        # Daily quota
        self.daily_req_count = daily_req_count
        # Domain status, 0 indicates normal, 1 indicates abnormal.
        self.domain_status = domain_status
        # Sending address ID
        self.mail_address_id = mail_address_id
        # Monthly quota limit
        self.month_count = month_count
        # Monthly quota
        self.month_req_count = month_req_count
        # Reply address
        self.reply_address = reply_address
        # Reply address status
        self.reply_status = reply_status
        # Sending address type. Values:
        # 
        # - batch: bulk email
        # - trigger: triggered email
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id

        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.daily_count is not None:
            result['DailyCount'] = self.daily_count

        if self.daily_req_count is not None:
            result['DailyReqCount'] = self.daily_req_count

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id

        if self.month_count is not None:
            result['MonthCount'] = self.month_count

        if self.month_req_count is not None:
            result['MonthReqCount'] = self.month_req_count

        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address

        if self.reply_status is not None:
            result['ReplyStatus'] = self.reply_status

        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')

        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DailyCount') is not None:
            self.daily_count = m.get('DailyCount')

        if m.get('DailyReqCount') is not None:
            self.daily_req_count = m.get('DailyReqCount')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')

        if m.get('MonthCount') is not None:
            self.month_count = m.get('MonthCount')

        if m.get('MonthReqCount') is not None:
            self.month_req_count = m.get('MonthReqCount')

        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')

        if m.get('ReplyStatus') is not None:
            self.reply_status = m.get('ReplyStatus')

        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')

        return self

