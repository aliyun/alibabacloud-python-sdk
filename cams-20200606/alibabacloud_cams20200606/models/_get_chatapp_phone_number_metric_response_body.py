# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetChatappPhoneNumberMetricResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.GetChatappPhoneNumberMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.GetChatappPhoneNumberMetricResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetChatappPhoneNumberMetricResponseBodyData(DaraModel):
    def __init__(
        self,
        delivered_count: int = None,
        end: int = None,
        granularity: str = None,
        phone_number: str = None,
        sent_count: int = None,
        start: int = None,
    ):
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range that you queried.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The business phone number.
        self.phone_number = phone_number
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range that you queried.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count

        if self.end is not None:
            result['End'] = self.end

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.sent_count is not None:
            result['SentCount'] = self.sent_count

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

