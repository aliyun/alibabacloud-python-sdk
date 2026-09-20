# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetBaselineResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBaselineResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true
        # - false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetBaselineResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBaselineResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_enabled: bool = None,
        alert_margin_threshold: int = None,
        alert_settings: List[main_models.GetBaselineResponseBodyDataAlertSettings] = None,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        enabled: bool = None,
        node_ids: List[int] = None,
        over_time_settings: List[main_models.GetBaselineResponseBodyDataOverTimeSettings] = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
    ):
        # Indicates whether alerting is started. Valid values:
        # 
        # - true
        # - false
        self.alert_enabled = alert_enabled
        # The alert margin threshold, in minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The alert settings.
        self.alert_settings = alert_settings
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values:
        # 
        # - DAILY: daily baseline.
        # - HOURLY: hourly baseline.
        self.baseline_type = baseline_type
        # Indicates whether the baseline is started.
        self.enabled = enabled
        # The list of upstream nodes of the baseline.
        self.node_ids = node_ids
        # The baseline committed time settings.
        self.over_time_settings = over_time_settings
        # The owner.
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 3, 5, 7, and 8.
        self.priority = priority
        # The project ID.
        self.project_id = project_id

    def validate(self):
        if self.alert_settings:
            for v1 in self.alert_settings:
                 if v1:
                    v1.validate()
        if self.over_time_settings:
            for v1 in self.over_time_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_enabled is not None:
            result['AlertEnabled'] = self.alert_enabled

        if self.alert_margin_threshold is not None:
            result['AlertMarginThreshold'] = self.alert_margin_threshold

        result['AlertSettings'] = []
        if self.alert_settings is not None:
            for k1 in self.alert_settings:
                result['AlertSettings'].append(k1.to_map() if k1 else None)

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        result['OverTimeSettings'] = []
        if self.over_time_settings is not None:
            for k1 in self.over_time_settings:
                result['OverTimeSettings'].append(k1.to_map() if k1 else None)

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEnabled') is not None:
            self.alert_enabled = m.get('AlertEnabled')

        if m.get('AlertMarginThreshold') is not None:
            self.alert_margin_threshold = m.get('AlertMarginThreshold')

        self.alert_settings = []
        if m.get('AlertSettings') is not None:
            for k1 in m.get('AlertSettings'):
                temp_model = main_models.GetBaselineResponseBodyDataAlertSettings()
                self.alert_settings.append(temp_model.from_map(k1))

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        self.over_time_settings = []
        if m.get('OverTimeSettings') is not None:
            for k1 in m.get('OverTimeSettings'):
                temp_model = main_models.GetBaselineResponseBodyDataOverTimeSettings()
                self.over_time_settings.append(temp_model.from_map(k1))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class GetBaselineResponseBodyDataOverTimeSettings(DaraModel):
    def __init__(
        self,
        cycle: int = None,
        time: str = None,
    ):
        # The cycle corresponding to the committed time. The value is 1 for daily baselines. You can configure up to 24 cycles for hourly baselines.
        self.cycle = cycle
        # The committed time in hh:mm format, where hh ranges from 0 to 47 and mm ranges from 0 to 59.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class GetBaselineResponseBodyDataAlertSettings(DaraModel):
    def __init__(
        self,
        alert_interval: int = None,
        alert_maximum: int = None,
        alert_methods: List[str] = None,
        alert_recipient: str = None,
        alert_recipient_type: str = None,
        alert_type: str = None,
        baseline_alert_enabled: bool = None,
        ding_robots: List[main_models.GetBaselineResponseBodyDataAlertSettingsDingRobots] = None,
        silence_end_time: str = None,
        silence_start_time: str = None,
        topic_slow_config: main_models.GetBaselineResponseBodyDataAlertSettingsTopicSlowConfig = None,
        topic_types: List[str] = None,
        webhooks: List[str] = None,
    ):
        # The event alerting interval, in seconds.
        self.alert_interval = alert_interval
        # The maximum number of event alerting notifications.
        self.alert_maximum = alert_maximum
        # The list of alert methods.
        self.alert_methods = alert_methods
        # The alert recipient details.
        # 
        # - If AlertRecipientType is set to OWNER: empty.
        # - If AlertRecipientType is set to SHIFT_SCHEDULE: the UID of the shift schedule.
        # - If AlertRecipientType is set to OTHER: a list of UIDs. Separate multiple UIDs with commas (,).
        self.alert_recipient = alert_recipient
        # The type of alert recipient. Valid values:
        # 
        # - OWNER: node owner.
        # - OTHER: specified users.
        # - SHIFT_SCHEDULE: shift schedule.
        self.alert_recipient_type = alert_recipient_type
        # The alerting type. Valid values:
        # - BASELINE: baseline.
        # - TOPIC: event.
        self.alert_type = alert_type
        # The baseline alert switch. This is a baseline-specific configuration. Valid values:
        # 
        # - true: started.
        # - false: stopped.
        self.baseline_alert_enabled = baseline_alert_enabled
        # The list of DingTalk chatbots.
        self.ding_robots = ding_robots
        # The silence end time, in the HH:mm:ss format.
        self.silence_end_time = silence_end_time
        # The silence start time, in the HH:mm:ss format.
        self.silence_start_time = silence_start_time
        self.topic_slow_config = topic_slow_config
        # The list of event alerting types. This is an event-specific configuration.
        self.topic_types = topic_types
        # The list of webhooks.
        self.webhooks = webhooks

    def validate(self):
        if self.ding_robots:
            for v1 in self.ding_robots:
                 if v1:
                    v1.validate()
        if self.topic_slow_config:
            self.topic_slow_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_interval is not None:
            result['AlertInterval'] = self.alert_interval

        if self.alert_maximum is not None:
            result['AlertMaximum'] = self.alert_maximum

        if self.alert_methods is not None:
            result['AlertMethods'] = self.alert_methods

        if self.alert_recipient is not None:
            result['AlertRecipient'] = self.alert_recipient

        if self.alert_recipient_type is not None:
            result['AlertRecipientType'] = self.alert_recipient_type

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.baseline_alert_enabled is not None:
            result['BaselineAlertEnabled'] = self.baseline_alert_enabled

        result['DingRobots'] = []
        if self.ding_robots is not None:
            for k1 in self.ding_robots:
                result['DingRobots'].append(k1.to_map() if k1 else None)

        if self.silence_end_time is not None:
            result['SilenceEndTime'] = self.silence_end_time

        if self.silence_start_time is not None:
            result['SilenceStartTime'] = self.silence_start_time

        if self.topic_slow_config is not None:
            result['TopicSlowConfig'] = self.topic_slow_config.to_map()

        if self.topic_types is not None:
            result['TopicTypes'] = self.topic_types

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertInterval') is not None:
            self.alert_interval = m.get('AlertInterval')

        if m.get('AlertMaximum') is not None:
            self.alert_maximum = m.get('AlertMaximum')

        if m.get('AlertMethods') is not None:
            self.alert_methods = m.get('AlertMethods')

        if m.get('AlertRecipient') is not None:
            self.alert_recipient = m.get('AlertRecipient')

        if m.get('AlertRecipientType') is not None:
            self.alert_recipient_type = m.get('AlertRecipientType')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('BaselineAlertEnabled') is not None:
            self.baseline_alert_enabled = m.get('BaselineAlertEnabled')

        self.ding_robots = []
        if m.get('DingRobots') is not None:
            for k1 in m.get('DingRobots'):
                temp_model = main_models.GetBaselineResponseBodyDataAlertSettingsDingRobots()
                self.ding_robots.append(temp_model.from_map(k1))

        if m.get('SilenceEndTime') is not None:
            self.silence_end_time = m.get('SilenceEndTime')

        if m.get('SilenceStartTime') is not None:
            self.silence_start_time = m.get('SilenceStartTime')

        if m.get('TopicSlowConfig') is not None:
            temp_model = main_models.GetBaselineResponseBodyDataAlertSettingsTopicSlowConfig()
            self.topic_slow_config = temp_model.from_map(m.get('TopicSlowConfig'))

        if m.get('TopicTypes') is not None:
            self.topic_types = m.get('TopicTypes')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

class GetBaselineResponseBodyDataAlertSettingsTopicSlowConfig(DaraModel):
    def __init__(
        self,
        min_over: int = None,
        over_factor: float = None,
    ):
        self.min_over = min_over
        self.over_factor = over_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.min_over is not None:
            result['MinOver'] = self.min_over

        if self.over_factor is not None:
            result['OverFactor'] = self.over_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinOver') is not None:
            self.min_over = m.get('MinOver')

        if m.get('OverFactor') is not None:
            self.over_factor = m.get('OverFactor')

        return self

class GetBaselineResponseBodyDataAlertSettingsDingRobots(DaraModel):
    def __init__(
        self,
        at_all: bool = None,
        web_url: str = None,
    ):
        # Indicates whether to @ all members.
        self.at_all = at_all
        # The webhook URL of the DingTalk chatbot.
        self.web_url = web_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at_all is not None:
            result['AtAll'] = self.at_all

        if self.web_url is not None:
            result['WebUrl'] = self.web_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtAll') is not None:
            self.at_all = m.get('AtAll')

        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')

        return self

