# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaAlarmsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_alarms: List[main_models.ListQuotaAlarmsResponseBodyQuotaAlarms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the current query.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # > If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The details of the quota usage alerts.
        self.quota_alarms = quota_alarms
        # The request ID.
        self.request_id = request_id
        # The total number of quota usage alerts.
        self.total_count = total_count

    def validate(self):
        if self.quota_alarms:
            for v1 in self.quota_alarms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QuotaAlarms'] = []
        if self.quota_alarms is not None:
            for k1 in self.quota_alarms:
                result['QuotaAlarms'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.quota_alarms = []
        if m.get('QuotaAlarms') is not None:
            for k1 in m.get('QuotaAlarms'):
                temp_model = main_models.ListQuotaAlarmsResponseBodyQuotaAlarms()
                self.quota_alarms.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaAlarmsResponseBodyQuotaAlarms(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        exceed_threshold: bool = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        # The alert ID.
        self.alarm_id = alarm_id
        # The alert name.
        self.alarm_name = alarm_name
        # The time when the quota usage alert was created.
        self.create_time = create_time
        # Indicates whether the quota usage exceeds the alert threshold. Valid values:
        # 
        # - false
        # 
        # - true
        self.exceed_threshold = exceed_threshold
        # The notification channels of the quota alert.
        self.notify_channels = notify_channels
        # The notification object of the alert.
        # 
        # > The value can only be accountContact, which specifies the contacts of the account.
        self.notify_target = notify_target
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions
        # The used quota.
        self.quota_usage = quota_usage
        # The quota value.
        self.quota_value = quota_value
        # The numeric value of the alert threshold.
        self.threshold = threshold
        # The percentage of the alert threshold.
        self.threshold_percent = threshold_percent
        # The type of the quota alert. Valid values:
        # 
        # - used: an alert for the used quota.
        # 
        # - usable: an alert for the available quota.
        self.threshold_type = threshold_type
        # The webhook URL.
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exceed_threshold is not None:
            result['ExceedThreshold'] = self.exceed_threshold

        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_dimensions is not None:
            result['QuotaDimensions'] = self.quota_dimensions

        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type

        if self.web_hook is not None:
            result['WebHook'] = self.web_hook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExceedThreshold') is not None:
            self.exceed_threshold = m.get('ExceedThreshold')

        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')

        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaDimensions') is not None:
            self.quota_dimensions = m.get('QuotaDimensions')

        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')

        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')

        return self

