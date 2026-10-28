# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateQuotaAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        # The ID of the quota alert.
        # 
        # > For more information about how to obtain the ID of a quota alert, see [ListQuotaAlarms](https://help.aliyun.com/document_detail/440561.html).
        # 
        # This parameter is required.
        self.alarm_id = alarm_id
        # The name of the quota alert.
        # 
        # > For more information about how to obtain the name of a quota alert, see [ListQuotaAlarms](https://help.aliyun.com/document_detail/440561.html).
        # 
        # This parameter is required.
        self.alarm_name = alarm_name
        # The numeric value of the alert threshold. Valid values:
        # 
        # - If you set `ThresholdType` to `used`, an alert is triggered when the used quota is greater than or equal to this value. The alert threshold must be greater than the current used quota.
        # 
        # - If you set `ThresholdType` to `usable`, an alert is triggered when the usable quota is less than or equal to this value. The alert threshold must be less than the current usable quota.
        # 
        # > You must set either Threshold or ThresholdPercent.
        self.threshold = threshold
        # The percentage of the alert threshold. Valid values:
        # 
        # - If you set `ThresholdType` to `used`, an alert is triggered when the percentage of the used quota is greater than or equal to this value. The value must be in the range of (50%, 100%].
        # 
        # - If you set `ThresholdType` to `usable`, an alert is triggered when the percentage of the usable quota is less than or equal to this value. The value must be in the range of (0%, 50%].
        # 
        # > You must set either Threshold or ThresholdPercent.
        self.threshold_percent = threshold_percent
        # The type of the quota alert. Valid values:
        # 
        # - used (default): The alert is triggered based on the used quota.
        # 
        # - usable: The alert is triggered based on the usable quota.
        self.threshold_type = threshold_type
        # The webhook URL. Quota Center sends alert notifications to this URL using an HTTP POST request.
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

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')

        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')

        return self

