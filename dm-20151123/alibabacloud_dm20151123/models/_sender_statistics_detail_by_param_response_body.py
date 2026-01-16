# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SenderStatisticsDetailByParamResponseBody(DaraModel):
    def __init__(
        self,
        next_start: str = None,
        request_id: str = None,
        data: main_models.SenderStatisticsDetailByParamResponseBodyData = None,
    ):
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Request ID
        self.request_id = request_id
        # Detailed records
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_start is not None:
            result['NextStart'] = self.next_start

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.SenderStatisticsDetailByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class SenderStatisticsDetailByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        mail_detail: List[main_models.SenderStatisticsDetailByParamResponseBodyDataMailDetail] = None,
    ):
        self.mail_detail = mail_detail

    def validate(self):
        if self.mail_detail:
            for v1 in self.mail_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mailDetail'] = []
        if self.mail_detail is not None:
            for k1 in self.mail_detail:
                result['mailDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mail_detail = []
        if m.get('mailDetail') is not None:
            for k1 in m.get('mailDetail'):
                temp_model = main_models.SenderStatisticsDetailByParamResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k1))

        return self

class SenderStatisticsDetailByParamResponseBodyDataMailDetail(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        config_set_id: str = None,
        config_set_name: str = None,
        error_classification: str = None,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
        last_update_time: str = None,
        message: str = None,
        status: int = None,
        subject: str = None,
        to_address: str = None,
        utc_last_update_time: str = None,
    ):
        # Sending address
        self.account_name = account_name
        self.config_set_id = config_set_id
        self.config_set_name = config_set_name
        # Detailed classification of error reasons: - SendOk - SmtpNxBox
        # etc.
        self.error_classification = error_classification
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name
        # Update time
        self.last_update_time = last_update_time
        # Delivery detail information
        self.message = message
        # Delivery status: 0 Success, 2 Invalid Address, 3 Spam, 4 Other Failures
        self.status = status
        # Email subject
        self.subject = subject
        # Recipient address
        self.to_address = to_address
        # UTC formatted update time
        self.utc_last_update_time = utc_last_update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id

        if self.config_set_name is not None:
            result['ConfigSetName'] = self.config_set_name

        if self.error_classification is not None:
            result['ErrorClassification'] = self.error_classification

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.to_address is not None:
            result['ToAddress'] = self.to_address

        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')

        if m.get('ConfigSetName') is not None:
            self.config_set_name = m.get('ConfigSetName')

        if m.get('ErrorClassification') is not None:
            self.error_classification = m.get('ErrorClassification')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')

        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')

        return self

