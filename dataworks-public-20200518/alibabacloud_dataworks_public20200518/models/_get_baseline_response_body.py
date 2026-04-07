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
        # The data returned.
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
        # 
        # *   true
        # *   false
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
        # Indicates whether the alerting feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.alert_enabled = alert_enabled
        # The alert margin threshold. Unit: minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The alert settings.
        self.alert_settings = alert_settings
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values:
        # 
        # *   DAILY
        # *   HOURLY
        self.baseline_type = baseline_type
        # Indicates whether the baseline is enabled.
        self.enabled = enabled
        # The node IDs.
        self.node_ids = node_ids
        # The settings of the committed completion time of the baseline.
        self.over_time_settings = over_time_settings
        # The owner.
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 3, 5, 7, and 8.
        self.priority = priority
        # The workspace ID.
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
        # The period corresponding to the commitment time. The space-based line is 1, and the hourly baseline can be configured for up to 24 cycles.
        self.cycle = cycle
        # Commitment time, hh:mm format, hh value range is [0,47],mm value range is [0,59].
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
        topic_types: List[str] = None,
        webhooks: List[str] = None,
    ):
        # The event alert interval, in seconds.
        self.alert_interval = alert_interval
        # The maximum number of event alerts.
        self.alert_maximum = alert_maximum
        # Alert method list
        self.alert_methods = alert_methods
        # Alert recipient details.
        # 
        # AlertRecipientType is OWNER: empty
        # AlertRecipientType is SHIFT_SCHEDULE: duty table uid
        # AlertRecipientType is OTHER: uid list, multiple UIDs are in English, split
        self.alert_recipient = alert_recipient
        # The type of alert recipient.
        # 
        # - OWNER: task owner
        # - OTHER: designated person
        # - SHIFT: SCHEDULE-duty table
        self.alert_recipient_type = alert_recipient_type
        # Alert type
        # 
        # - BASELINE: baseline
        # - TOPIC: event
        self.alert_type = alert_type
        # The baseline alarm switch.
        # 
        # - true
        # - false
        self.baseline_alert_enabled = baseline_alert_enabled
        # DingTalk robot list.
        self.ding_robots = ding_robots
        # The end time of the silence. The format is HH:mm:ss.
        self.silence_end_time = silence_end_time
        # The start time of the silence. Format: HH:mm:ss
        self.silence_start_time = silence_start_time
        # The list of Event Alert types.
        self.topic_types = topic_types
        # webhook list.
        self.webhooks = webhooks

    def validate(self):
        if self.ding_robots:
            for v1 in self.ding_robots:
                 if v1:
                    v1.validate()

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

        if m.get('TopicTypes') is not None:
            self.topic_types = m.get('TopicTypes')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

class GetBaselineResponseBodyDataAlertSettingsDingRobots(DaraModel):
    def __init__(
        self,
        at_all: bool = None,
        web_url: str = None,
    ):
        # Whether @ everyone.
        self.at_all = at_all
        # DingTalk robot address
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

