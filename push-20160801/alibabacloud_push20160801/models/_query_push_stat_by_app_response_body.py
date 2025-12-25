# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryPushStatByAppResponseBody(DaraModel):
    def __init__(
        self,
        app_push_stats: main_models.QueryPushStatByAppResponseBodyAppPushStats = None,
        request_id: str = None,
    ):
        self.app_push_stats = app_push_stats
        self.request_id = request_id

    def validate(self):
        if self.app_push_stats:
            self.app_push_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_push_stats is not None:
            result['AppPushStats'] = self.app_push_stats.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPushStats') is not None:
            temp_model = main_models.QueryPushStatByAppResponseBodyAppPushStats()
            self.app_push_stats = temp_model.from_map(m.get('AppPushStats'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPushStatByAppResponseBodyAppPushStats(DaraModel):
    def __init__(
        self,
        app_push_stat: List[main_models.QueryPushStatByAppResponseBodyAppPushStatsAppPushStat] = None,
    ):
        self.app_push_stat = app_push_stat

    def validate(self):
        if self.app_push_stat:
            for v1 in self.app_push_stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppPushStat'] = []
        if self.app_push_stat is not None:
            for k1 in self.app_push_stat:
                result['AppPushStat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_push_stat = []
        if m.get('AppPushStat') is not None:
            for k1 in m.get('AppPushStat'):
                temp_model = main_models.QueryPushStatByAppResponseBodyAppPushStatsAppPushStat()
                self.app_push_stat.append(temp_model.from_map(k1))

        return self

class QueryPushStatByAppResponseBodyAppPushStatsAppPushStat(DaraModel):
    def __init__(
        self,
        accept_count: int = None,
        deleted_count: int = None,
        opened_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_failed_count: int = None,
        sms_receive_failed_count: int = None,
        sms_receive_success_count: int = None,
        sms_sent_count: int = None,
        sms_skip_count: int = None,
        time: str = None,
    ):
        self.accept_count = accept_count
        self.deleted_count = deleted_count
        self.opened_count = opened_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_failed_count = sms_failed_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_sent_count = sms_sent_count
        self.sms_skip_count = sms_skip_count
        self.time = time

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

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')

        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')

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

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

