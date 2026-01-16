# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryInvalidAddressResponseBody(DaraModel):
    def __init__(
        self,
        next_start: str = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryInvalidAddressResponseBodyData = None,
    ):
        # Next request starting position.
        self.next_start = next_start
        # Request ID.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count
        # Records.
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryInvalidAddressResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryInvalidAddressResponseBodyData(DaraModel):
    def __init__(
        self,
        mail_detail: List[main_models.QueryInvalidAddressResponseBodyDataMailDetail] = None,
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
                temp_model = main_models.QueryInvalidAddressResponseBodyDataMailDetail()
                self.mail_detail.append(temp_model.from_map(k1))

        return self

class QueryInvalidAddressResponseBodyDataMailDetail(DaraModel):
    def __init__(
        self,
        last_update_time: str = None,
        to_address: str = None,
        utc_last_update_time: int = None,
    ):
        # Update time.
        self.last_update_time = last_update_time
        # Recipient address.
        self.to_address = to_address
        # Update time (in timestamp format).
        self.utc_last_update_time = utc_last_update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.to_address is not None:
            result['ToAddress'] = self.to_address

        if self.utc_last_update_time is not None:
            result['UtcLastUpdateTime'] = self.utc_last_update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')

        if m.get('UtcLastUpdateTime') is not None:
            self.utc_last_update_time = m.get('UtcLastUpdateTime')

        return self

