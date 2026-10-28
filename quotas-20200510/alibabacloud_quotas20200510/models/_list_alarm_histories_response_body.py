# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListAlarmHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        alarm_histories: List[main_models.ListAlarmHistoriesResponseBodyAlarmHistories] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the quota alert history records.
        self.alarm_histories = alarm_histories
        # The maximum number of entries returned for the current query.
        self.max_results = max_results
        # The token that marks the position of the returned query data. An empty value indicates that all data has been queried.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned for the current request.
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for v1 in self.alarm_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k1 in self.alarm_histories:
                result['AlarmHistories'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k1 in m.get('AlarmHistories'):
                temp_model = main_models.ListAlarmHistoriesResponseBodyAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlarmHistoriesResponseBodyAlarmHistories(DaraModel):
    def __init__(
        self,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_usage: float = None,
        threshold: float = None,
        threshold_percent: float = None,
    ):
        # The name of the quota alert.
        self.alarm_name = alarm_name
        # The time when the quota alert was created.
        self.create_time = create_time
        # The notification channels for the quota alert.
        self.notify_channels = notify_channels
        # The notification recipients of the quota alert.
        self.notify_target = notify_target
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota usage.
        self.quota_usage = quota_usage
        # The value of the quota alert threshold.
        self.threshold = threshold
        # The percentage of the quota alert threshold.
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')

        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        return self

