# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetQuotaAlarmResponseBody(DaraModel):
    def __init__(
        self,
        quota_alarm: main_models.GetQuotaAlarmResponseBodyQuotaAlarm = None,
        request_id: str = None,
    ):
        # The details of the quota alert.
        self.quota_alarm = quota_alarm
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.quota_alarm:
            self.quota_alarm.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_alarm is not None:
            result['QuotaAlarm'] = self.quota_alarm.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaAlarm') is not None:
            temp_model = main_models.GetQuotaAlarmResponseBodyQuotaAlarm()
            self.quota_alarm = temp_model.from_map(m.get('QuotaAlarm'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetQuotaAlarmResponseBodyQuotaAlarm(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimension: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        webhook: str = None,
    ):
        # The ID of the quota alert.
        self.alarm_id = alarm_id
        # The name of the quota alert.
        self.alarm_name = alarm_name
        # The time when the quota alert was created.
        self.create_time = create_time
        # The notification channels for the alert.
        self.notify_channels = notify_channels
        # The notification recipient of the quota alert.
        self.notify_target = notify_target
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The quota dimension.
        self.quota_dimension = quota_dimension
        # The quota usage.
        self.quota_usage = quota_usage
        # The quota value.
        self.quota_value = quota_value
        # The numeric value of the quota alert threshold.
        self.threshold = threshold
        # The percentage of the quota alert threshold.
        self.threshold_percent = threshold_percent
        # The Alarm Metric of the quota alerting. Valid values:
        # 
        # - used: Alerting on the used quota usage.
        # - usable: Alerting on the remaining active quota.
        self.threshold_type = threshold_type
        # The public URL to which Quota Center sends alert messages by using HTTP POST requests.
        self.webhook = webhook

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

        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension

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

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

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

        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')

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

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

