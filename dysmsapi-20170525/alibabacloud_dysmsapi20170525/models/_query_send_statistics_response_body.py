# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySendStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySendStatisticsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySendStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QuerySendStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        target_list: List[main_models.QuerySendStatisticsResponseBodyDataTargetList] = None,
        total_size: int = None,
    ):
        # The details of the data returned.
        self.target_list = target_list
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.QuerySendStatisticsResponseBodyDataTargetList()
                self.target_list.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class QuerySendStatisticsResponseBodyDataTargetList(DaraModel):
    def __init__(
        self,
        no_responded_count: int = None,
        responded_fail_count: int = None,
        responded_success_count: int = None,
        send_date: str = None,
        total_count: int = None,
    ):
        # The number of messages without a delivery receipt.
        self.no_responded_count = no_responded_count
        # The number of messages with a delivery receipt that indicates a failure.
        self.responded_fail_count = responded_fail_count
        # The number of messages with a delivery receipt that indicates a success.
        self.responded_success_count = responded_success_count
        # The date when the message is sent. Format: yyyyMMdd. Example: 20181225.
        self.send_date = send_date
        # The number of delivered messages.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.no_responded_count is not None:
            result['NoRespondedCount'] = self.no_responded_count

        if self.responded_fail_count is not None:
            result['RespondedFailCount'] = self.responded_fail_count

        if self.responded_success_count is not None:
            result['RespondedSuccessCount'] = self.responded_success_count

        if self.send_date is not None:
            result['SendDate'] = self.send_date

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoRespondedCount') is not None:
            self.no_responded_count = m.get('NoRespondedCount')

        if m.get('RespondedFailCount') is not None:
            self.responded_fail_count = m.get('RespondedFailCount')

        if m.get('RespondedSuccessCount') is not None:
            self.responded_success_count = m.get('RespondedSuccessCount')

        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

