# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryPushStatByMsgResponseBody(DaraModel):
    def __init__(
        self,
        push_stats: main_models.QueryPushStatByMsgResponseBodyPushStats = None,
        request_id: str = None,
    ):
        self.push_stats = push_stats
        self.request_id = request_id

    def validate(self):
        if self.push_stats:
            self.push_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_stats is not None:
            result['PushStats'] = self.push_stats.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushStats') is not None:
            temp_model = main_models.QueryPushStatByMsgResponseBodyPushStats()
            self.push_stats = temp_model.from_map(m.get('PushStats'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPushStatByMsgResponseBodyPushStats(DaraModel):
    def __init__(
        self,
        push_stat: List[main_models.QueryPushStatByMsgResponseBodyPushStatsPushStat] = None,
    ):
        self.push_stat = push_stat

    def validate(self):
        if self.push_stat:
            for v1 in self.push_stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushStat'] = []
        if self.push_stat is not None:
            for k1 in self.push_stat:
                result['PushStat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_stat = []
        if m.get('PushStat') is not None:
            for k1 in m.get('PushStat'):
                temp_model = main_models.QueryPushStatByMsgResponseBodyPushStatsPushStat()
                self.push_stat.append(temp_model.from_map(k1))

        return self

class QueryPushStatByMsgResponseBodyPushStatsPushStat(DaraModel):
    def __init__(
        self,
        accept_count: int = None,
        deleted_count: int = None,
        message_id: str = None,
        opened_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_failed_count: int = None,
        sms_receive_failed_count: int = None,
        sms_receive_success_count: int = None,
        sms_sent_count: int = None,
        sms_skip_count: int = None,
    ):
        self.accept_count = accept_count
        self.deleted_count = deleted_count
        self.message_id = message_id
        self.opened_count = opened_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_failed_count = sms_failed_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_sent_count = sms_sent_count
        self.sms_skip_count = sms_skip_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_count is not None:
            result['AcceptCount'] = self.accept_count

        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.opened_count is not None:
            result['OpenedCount'] = self.opened_count

        if self.received_count is not None:
            result['ReceivedCount'] = self.received_count

        if self.sent_count is not None:
            result['SentCount'] = self.sent_count

        if self.sms_failed_count is not None:
            result['SmsFailedCount'] = self.sms_failed_count

        if self.sms_receive_failed_count is not None:
            result['SmsReceiveFailedCount'] = self.sms_receive_failed_count

        if self.sms_receive_success_count is not None:
            result['SmsReceiveSuccessCount'] = self.sms_receive_success_count

        if self.sms_sent_count is not None:
            result['SmsSentCount'] = self.sms_sent_count

        if self.sms_skip_count is not None:
            result['SmsSkipCount'] = self.sms_skip_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')

        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('OpenedCount') is not None:
            self.opened_count = m.get('OpenedCount')

        if m.get('ReceivedCount') is not None:
            self.received_count = m.get('ReceivedCount')

        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')

        if m.get('SmsFailedCount') is not None:
            self.sms_failed_count = m.get('SmsFailedCount')

        if m.get('SmsReceiveFailedCount') is not None:
            self.sms_receive_failed_count = m.get('SmsReceiveFailedCount')

        if m.get('SmsReceiveSuccessCount') is not None:
            self.sms_receive_success_count = m.get('SmsReceiveSuccessCount')

        if m.get('SmsSentCount') is not None:
            self.sms_sent_count = m.get('SmsSentCount')

        if m.get('SmsSkipCount') is not None:
            self.sms_skip_count = m.get('SmsSkipCount')

        return self

