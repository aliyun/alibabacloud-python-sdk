# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class UpdateBaselineRequest(DaraModel):
    def __init__(
        self,
        alert_enabled: bool = None,
        alert_margin_threshold: int = None,
        alert_settings: List[main_models.UpdateBaselineRequestAlertSettings] = None,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        enabled: bool = None,
        node_ids: str = None,
        overtime_settings: List[main_models.UpdateBaselineRequestOvertimeSettings] = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        remove_node_ids: str = None,
    ):
        # Specifies whether to enable the alerting feature. Valid values: true and false.
        self.alert_enabled = alert_enabled
        # The alert margin threshold of the baseline. Unit: minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The alert settings of the baseline.
        self.alert_settings = alert_settings
        # The baseline ID. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY and HOURLY.
        self.baseline_type = baseline_type
        # Specifies whether to enable the baseline. Valid values: true and false.
        self.enabled = enabled
        # The ancestor nodes of nodes in the baseline. Separate the ancestor nodes with commas (,). If a large number of ancestor nodes exist, we recommend that you create a zero load node and configure the zero load node as the descendant node of nodes in the baseline to facilitate node management.
        self.node_ids = node_ids
        # The settings of the committed completion time of the baseline.
        self.overtime_settings = overtime_settings
        # The ID of the Alibaba Cloud account used by the baseline owner.
        self.owner = owner
        # The priority of the baseline. Valid values: {1,3,5,7,8}.
        self.priority = priority
        # The workspace ID. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The ID of the node that you want to disassociate from the baseline. You can specify multiple node IDs. Separate multiple node IDs with commas (,).
        self.remove_node_ids = remove_node_ids

    def validate(self):
        if self.alert_settings:
            for v1 in self.alert_settings:
                 if v1:
                    v1.validate()
        if self.overtime_settings:
            for v1 in self.overtime_settings:
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

        result['OvertimeSettings'] = []
        if self.overtime_settings is not None:
            for k1 in self.overtime_settings:
                result['OvertimeSettings'].append(k1.to_map() if k1 else None)

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.remove_node_ids is not None:
            result['RemoveNodeIds'] = self.remove_node_ids

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
                temp_model = main_models.UpdateBaselineRequestAlertSettings()
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

        self.overtime_settings = []
        if m.get('OvertimeSettings') is not None:
            for k1 in m.get('OvertimeSettings'):
                temp_model = main_models.UpdateBaselineRequestOvertimeSettings()
                self.overtime_settings.append(temp_model.from_map(k1))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemoveNodeIds') is not None:
            self.remove_node_ids = m.get('RemoveNodeIds')

        return self

class UpdateBaselineRequestOvertimeSettings(DaraModel):
    def __init__(
        self,
        cycle: int = None,
        time: str = None,
    ):
        # The cycle that corresponds to the committed completion time. For a day-level baseline, set this parameter to 1. For an hour-level baseline, set this parameter to a value that is no more than 24.
        self.cycle = cycle
        # The committed completion time in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
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

class UpdateBaselineRequestAlertSettings(DaraModel):
    def __init__(
        self,
        alert_interval: int = None,
        alert_maximum: int = None,
        alert_methods: List[str] = None,
        alert_recipient: str = None,
        alert_recipient_type: str = None,
        alert_type: str = None,
        baseline_alert_enabled: bool = None,
        ding_robots: List[main_models.UpdateBaselineRequestAlertSettingsDingRobots] = None,
        silence_end_time: str = None,
        silence_start_time: str = None,
        topic_types: List[str] = None,
        webhooks: List[str] = None,
    ):
        # The interval at which an event alert notification is sent. Unit: minutes. Minimum value: 5. Maximum value: 1,440.
        self.alert_interval = alert_interval
        # The maximum number of times an event alert notification is sent. Maximum value: 24.
        self.alert_maximum = alert_maximum
        # The alert notification methods. Valid values: MAIL, SMS, PHONE, DINGROBOTS, and Webhooks. The value MAIL indicates that alert notifications are sent by email. The value SMS indicates that alert notifications are sent by text message. The value PHONE indicates that alert notifications are sent by phone call. You can use this notification method only in DataWorks Professional Edition or a more advanced edition. The value DINGROBOTS indicates that alert notifications are sent by using a DingTalk chatbot. You can use this notification method only if the RobotUrls parameter is configured. The value Webhooks indicates that alert notifications are sent by WeCom or Lark. You can use this notification method only if the Webhooks parameter is configured.
        self.alert_methods = alert_methods
        # The details of the alert recipient. If you set AlertRecipientType to OWNER, leave this parameter empty. If you set AlertRecipientType to SHIFT_SCHEDULE, set this parameter to the name of the shift schedule. If you set AlertRecipientType to OTHER, set this parameter to the employee IDs of specified personnel.
        self.alert_recipient = alert_recipient
        # The type of the alert recipient. Valid values: OWNER, OTHER, and SHIFT_SCHEDULE. The value OWNER indicates the node owner. The value OTHER indicates specified personnel. The value SHIFT_SCHEDULE indicates personnel in a shift schedule.
        self.alert_recipient_type = alert_recipient_type
        # The type of the alert. Valid values: BASELINE and TOPIC. The value BASELINE indicates a baseline alert. The value TOPIC indicates an event alert.
        self.alert_type = alert_type
        # Specifies whether to enable the baseline alerting feature. This feature is specific to baselines. Valid values: true and false.
        self.baseline_alert_enabled = baseline_alert_enabled
        # The DingTalk chatbots.
        self.ding_robots = ding_robots
        # The end time of silence.
        self.silence_end_time = silence_end_time
        # The start time of silence.
        self.silence_start_time = silence_start_time
        # The types of event alerts, which are event-specific configurations.
        self.topic_types = topic_types
        # The webhook URLs.
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
                temp_model = main_models.UpdateBaselineRequestAlertSettingsDingRobots()
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

class UpdateBaselineRequestAlertSettingsDingRobots(DaraModel):
    def __init__(
        self,
        at_all: bool = None,
        web_url: str = None,
    ):
        # Specifies whether to remind all members by using the at sign (@). Valid values: true and false.
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

