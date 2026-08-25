# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetAlertRuleResponseBody(DaraModel):
    def __init__(
        self,
        alert_rule: main_models.GetAlertRuleResponseBodyAlertRule = None,
        request_id: str = None,
    ):
        # The details of the custom alert rule.
        self.alert_rule = alert_rule
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.alert_rule:
            self.alert_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRule') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRule()
            self.alert_rule = temp_model.from_map(m.get('AlertRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAlertRuleResponseBodyAlertRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        notification: main_models.GetAlertRuleResponseBodyAlertRuleNotification = None,
        owner: str = None,
        trigger_condition: main_models.GetAlertRuleResponseBodyAlertRuleTriggerCondition = None,
    ):
        # Indicates whether the alert rule is enabled.
        self.enabled = enabled
        # The ID of the custom alert rule.
        self.id = id
        # The name of the custom alert rule.
        self.name = name
        # The alert notification configuration.
        self.notification = notification
        # The Alibaba Cloud UID of the owner of the custom alert rule.
        self.owner = owner
        # The condition that triggers the alert.
        self.trigger_condition = trigger_condition

    def validate(self):
        if self.notification:
            self.notification.validate()
        if self.trigger_condition:
            self.trigger_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.trigger_condition is not None:
            result['TriggerCondition'] = self.trigger_condition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notification') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TriggerCondition') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerCondition()
            self.trigger_condition = temp_model.from_map(m.get('TriggerCondition'))

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerCondition(DaraModel):
    def __init__(
        self,
        extension: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtension = None,
        target: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionTarget = None,
        type: str = None,
    ):
        # The extension information. Required for certain trigger conditions.
        self.extension = extension
        # The monitored object.
        self.target = target
        # The type of the alert trigger. Valid values:
        # 
        # - Finished: instance completed.
        # - UnFinished: instance not completed.
        # - Error: instance failed.
        # - CycleUnfinished: instance cycle not completed.
        # - Timeout: instance timed out.
        # - InstanceTransferComplete: node-to-instance conversion completed.
        # - InstanceTransferFluctuate: instance count fluctuation.
        # - ExhaustedError: instance still failed after automatic reruns.
        # - InstanceKeyword: failed instance contains keyword.
        # - InstanceErrorCount: number of failed instances.
        # - InstanceErrorPercentage: percentage of failed instances.
        # - ResourceGroupPercentage: schedule resource utilization.
        # - ResourceGroupWaitCount: number of instances waiting for schedule resources.
        self.type = type

    def validate(self):
        if self.extension:
            self.extension.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtension()
            self.extension = temp_model.from_map(m.get('Extension'))

        if m.get('Target') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionTarget(DaraModel):
    def __init__(
        self,
        allow_tasks: List[int] = None,
        ids: List[int] = None,
        type: str = None,
    ):
        # The whitelist of monitored nodes.
        self.allow_tasks = allow_tasks
        # The list of monitored object IDs.
        self.ids = ids
        # The monitored object type. Valid values:
        # 
        # - Task: node.
        # - Baseline: baseline.
        # - Project: workspace.
        # - BizProcess: business process flow.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_tasks is not None:
            result['AllowTasks'] = self.allow_tasks

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowTasks') is not None:
            self.allow_tasks = m.get('AllowTasks')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtension(DaraModel):
    def __init__(
        self,
        cycle_unfinished: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinished = None,
        error: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionError = None,
        instance_error_count: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorCount = None,
        instance_error_percentage: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorPercentage = None,
        instance_transfer_fluctuate: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceTransferFluctuate = None,
        timeout: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionTimeout = None,
        un_finished: main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionUnFinished = None,
    ):
        # The cycle-not-completed alert configuration.
        self.cycle_unfinished = cycle_unfinished
        # The error alert configuration.
        self.error = error
        # The instance error count alert configuration.
        self.instance_error_count = instance_error_count
        # The instance error percentage alert configuration.
        self.instance_error_percentage = instance_error_percentage
        # The instance count fluctuation alert configuration.
        self.instance_transfer_fluctuate = instance_transfer_fluctuate
        # The timeout alert configuration.
        self.timeout = timeout
        # The not-completed alert configuration.
        self.un_finished = un_finished

    def validate(self):
        if self.cycle_unfinished:
            self.cycle_unfinished.validate()
        if self.error:
            self.error.validate()
        if self.instance_error_count:
            self.instance_error_count.validate()
        if self.instance_error_percentage:
            self.instance_error_percentage.validate()
        if self.instance_transfer_fluctuate:
            self.instance_transfer_fluctuate.validate()
        if self.timeout:
            self.timeout.validate()
        if self.un_finished:
            self.un_finished.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_unfinished is not None:
            result['CycleUnfinished'] = self.cycle_unfinished.to_map()

        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.instance_error_count is not None:
            result['InstanceErrorCount'] = self.instance_error_count.to_map()

        if self.instance_error_percentage is not None:
            result['InstanceErrorPercentage'] = self.instance_error_percentage.to_map()

        if self.instance_transfer_fluctuate is not None:
            result['InstanceTransferFluctuate'] = self.instance_transfer_fluctuate.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout.to_map()

        if self.un_finished is not None:
            result['UnFinished'] = self.un_finished.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleUnfinished') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinished()
            self.cycle_unfinished = temp_model.from_map(m.get('CycleUnfinished'))

        if m.get('Error') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('InstanceErrorCount') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorCount()
            self.instance_error_count = temp_model.from_map(m.get('InstanceErrorCount'))

        if m.get('InstanceErrorPercentage') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorPercentage()
            self.instance_error_percentage = temp_model.from_map(m.get('InstanceErrorPercentage'))

        if m.get('InstanceTransferFluctuate') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceTransferFluctuate()
            self.instance_transfer_fluctuate = temp_model.from_map(m.get('InstanceTransferFluctuate'))

        if m.get('Timeout') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionTimeout()
            self.timeout = temp_model.from_map(m.get('Timeout'))

        if m.get('UnFinished') is not None:
            temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionUnFinished()
            self.un_finished = temp_model.from_map(m.get('UnFinished'))

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionUnFinished(DaraModel):
    def __init__(
        self,
        un_finished_time: str = None,
    ):
        # The not-completed time. Format: hh:mm. Valid values of hh: 0 to 47. Valid values of mm: 0 to 59.
        self.un_finished_time = un_finished_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.un_finished_time is not None:
            result['UnFinishedTime'] = self.un_finished_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnFinishedTime') is not None:
            self.un_finished_time = m.get('UnFinishedTime')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionTimeout(DaraModel):
    def __init__(
        self,
        timeout_in_minutes: int = None,
    ):
        # The timeout duration, in minutes.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceTransferFluctuate(DaraModel):
    def __init__(
        self,
        percentage: int = None,
        trend: str = None,
    ):
        # The fluctuation percentage. Valid values: 1 to 100.
        self.percentage = percentage
        # The fluctuation type. Valid values:
        # 
        # - abs: absolute value.
        # - increase: increase.
        # - decrease: decrease.
        self.trend = trend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.trend is not None:
            result['Trend'] = self.trend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorPercentage(DaraModel):
    def __init__(
        self,
        percentage: int = None,
    ):
        # The percentage of failed instances. Valid values: 1 to 100.
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionInstanceErrorCount(DaraModel):
    def __init__(
        self,
        count: int = None,
    ):
        # The number of failed instances. Valid values: 1 to 10000.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionError(DaraModel):
    def __init__(
        self,
        auto_rerun_alert_enabled: bool = None,
        stream_task_ids: List[int] = None,
    ):
        # Specifies whether to generate an alert when a batch task is automatically rerun due to a failure.
        self.auto_rerun_alert_enabled = auto_rerun_alert_enabled
        # The IDs of real-time computing nodes to monitor.
        self.stream_task_ids = stream_task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_rerun_alert_enabled is not None:
            result['AutoRerunAlertEnabled'] = self.auto_rerun_alert_enabled

        if self.stream_task_ids is not None:
            result['StreamTaskIds'] = self.stream_task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRerunAlertEnabled') is not None:
            self.auto_rerun_alert_enabled = m.get('AutoRerunAlertEnabled')

        if m.get('StreamTaskIds') is not None:
            self.stream_task_ids = m.get('StreamTaskIds')

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinished(DaraModel):
    def __init__(
        self,
        cycle_and_time: List[main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinishedCycleAndTime] = None,
    ):
        # The list of cycle and time configurations.
        self.cycle_and_time = cycle_and_time

    def validate(self):
        if self.cycle_and_time:
            for v1 in self.cycle_and_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CycleAndTime'] = []
        if self.cycle_and_time is not None:
            for k1 in self.cycle_and_time:
                result['CycleAndTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cycle_and_time = []
        if m.get('CycleAndTime') is not None:
            for k1 in m.get('CycleAndTime'):
                temp_model = main_models.GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinishedCycleAndTime()
                self.cycle_and_time.append(temp_model.from_map(k1))

        return self

class GetAlertRuleResponseBodyAlertRuleTriggerConditionExtensionCycleUnfinishedCycleAndTime(DaraModel):
    def __init__(
        self,
        cycle_id: int = None,
        time: str = None,
    ):
        # The cycle ID. Valid values: 1 to 288.
        self.cycle_id = cycle_id
        # The timeout time. Format: hh:mm. Valid values of hh: 0 to 47. Valid values of mm: 0 to 59.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_id is not None:
            result['CycleId'] = self.cycle_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleId') is not None:
            self.cycle_id = m.get('CycleId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class GetAlertRuleResponseBodyAlertRuleNotification(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        interval_in_minutes: int = None,
        maximum: int = None,
        receivers: List[main_models.GetAlertRuleResponseBodyAlertRuleNotificationReceivers] = None,
        silence_end_time: str = None,
        silence_start_time: str = None,
    ):
        # The list of alert channels.
        self.channels = channels
        # The alert interval, in minutes. Valid values: 5 to 10000.
        self.interval_in_minutes = interval_in_minutes
        # The maximum number of alerts within a calendar day. Valid values: 1 to 10000.
        self.maximum = maximum
        # The alert recipients.
        self.receivers = receivers
        # The end time of the mute period. Format: HH:mm:ss.
        self.silence_end_time = silence_end_time
        # The start time of the mute period. Format: HH:mm:ss.
        self.silence_start_time = silence_start_time

    def validate(self):
        if self.receivers:
            for v1 in self.receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        if self.interval_in_minutes is not None:
            result['IntervalInMinutes'] = self.interval_in_minutes

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        result['Receivers'] = []
        if self.receivers is not None:
            for k1 in self.receivers:
                result['Receivers'].append(k1.to_map() if k1 else None)

        if self.silence_end_time is not None:
            result['SilenceEndTime'] = self.silence_end_time

        if self.silence_start_time is not None:
            result['SilenceStartTime'] = self.silence_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('IntervalInMinutes') is not None:
            self.interval_in_minutes = m.get('IntervalInMinutes')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        self.receivers = []
        if m.get('Receivers') is not None:
            for k1 in m.get('Receivers'):
                temp_model = main_models.GetAlertRuleResponseBodyAlertRuleNotificationReceivers()
                self.receivers.append(temp_model.from_map(k1))

        if m.get('SilenceEndTime') is not None:
            self.silence_end_time = m.get('SilenceEndTime')

        if m.get('SilenceStartTime') is not None:
            self.silence_start_time = m.get('SilenceStartTime')

        return self

class GetAlertRuleResponseBodyAlertRuleNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The additional configuration required by the alert recipient. If ReceiverType is DingdingUrl, you can set {"atAll":true} to @ all members.
        self.extension = extension
        # The type of the alert recipient. Valid values:
        # 
        # - AliUid: Alibaba Cloud UID.
        # - ShiftSchedule: shift schedule.
        # - TaskOwner: node owner. Applicable to custom alerting and event alerting.
        # - Owner: owner. Applicable to baseline alerting.
        # - WebhookUrl: custom webhook URL.
        # - DingdingUrl: DingTalk webhook URL.
        # - FeishuUrl: Lark webhook URL.
        # - WeixinUrl: WeChat webhook URL.
        self.receiver_type = receiver_type
        # The values of the alert recipient.
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')

        return self

