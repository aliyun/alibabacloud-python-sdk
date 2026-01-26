# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateNotificationPolicyResponseBody(DaraModel):
    def __init__(
        self,
        notification_policy: main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy = None,
        request_id: str = None,
    ):
        # An array of notification policy objects.
        self.notification_policy = notification_policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.notification_policy:
            self.notification_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_policy is not None:
            result['NotificationPolicy'] = self.notification_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationPolicy') is not None:
            temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy()
            self.notification_policy = temp_model.from_map(m.get('NotificationPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy(DaraModel):
    def __init__(
        self,
        directed_mode: bool = None,
        escalation_policy_id: int = None,
        group_rule: main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule = None,
        id: int = None,
        integration_id: int = None,
        matching_rules: List[main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules] = None,
        name: str = None,
        notify_rule: main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule = None,
        notify_template: main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate = None,
        repeat: bool = None,
        repeat_interval: int = None,
        send_recover_message: bool = None,
        state: str = None,
    ):
        # Specifies whether to enable simple mode.
        self.directed_mode = directed_mode
        # The ID of the escalation policy.
        self.escalation_policy_id = escalation_policy_id
        # An array of alert event group objects.
        self.group_rule = group_rule
        # The ID of the notification policy.
        self.id = id
        # The integration ID of the ticket system to which alerts are pushed.
        self.integration_id = integration_id
        # The matching rules.
        self.matching_rules = matching_rules
        # The name of the notification policy.
        self.name = name
        # An array of notification rule objects.
        self.notify_rule = notify_rule
        # The notification template.
        self.notify_template = notify_template
        # Indicates whether a notification is resent for a long-lasting unresolved alert. Default value: true. Valid values:
        # 
        # *   `true`: The system resends a notification for a long-lasting unresolved alert at a specified time interval.
        # *   `false`: The system sends a notification for a long-lasting unresolved alert based on an escalation policy.
        self.repeat = repeat
        # The time interval at which a notification is resent for a long-lasting unresolved alert. Unit: seconds.
        self.repeat_interval = repeat_interval
        # Indicates whether the status of an alert automatically changes to Resolved when all events related to the alert change to the Restored state. ARMS notifies contacts when the alert status changes to Resolved.
        # 
        # *   `true`: The system sends a notification.
        # *   `false`: The system does not send a notification.
        self.send_recover_message = send_recover_message
        # Indicates whether the notification policy is enabled. Valid values: enable and disable.
        self.state = state

    def validate(self):
        if self.group_rule:
            self.group_rule.validate()
        if self.matching_rules:
            for v1 in self.matching_rules:
                 if v1:
                    v1.validate()
        if self.notify_rule:
            self.notify_rule.validate()
        if self.notify_template:
            self.notify_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directed_mode is not None:
            result['DirectedMode'] = self.directed_mode

        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id

        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id

        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k1 in self.matching_rules:
                result['MatchingRules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()

        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template.to_map()

        if self.repeat is not None:
            result['Repeat'] = self.repeat

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectedMode') is not None:
            self.directed_mode = m.get('DirectedMode')

        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')

        if m.get('GroupRule') is not None:
            temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule()
            self.group_rule = temp_model.from_map(m.get('GroupRule'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')

        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k1 in m.get('MatchingRules'):
                temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyRule') is not None:
            temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule()
            self.notify_rule = temp_model.from_map(m.get('NotifyRule'))

        if m.get('NotifyTemplate') is not None:
            temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate()
            self.notify_template = temp_model.from_map(m.get('NotifyTemplate'))

        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate(DaraModel):
    def __init__(
        self,
        email_content: str = None,
        email_recover_content: str = None,
        email_recover_title: str = None,
        email_title: str = None,
        robot_content: str = None,
        sms_content: str = None,
        sms_recover_content: str = None,
        tts_content: str = None,
        tts_recover_content: str = None,
    ):
        # The content of the alert notification sent through email.
        self.email_content = email_content
        # The content of the alert resolution notification sent through email.
        self.email_recover_content = email_recover_content
        # The title of the alert resolution notification sent through email.
        self.email_recover_title = email_recover_title
        # The title of the alert notification sent through email.
        self.email_title = email_title
        # The content of the alert notification sent by the IM robot.
        self.robot_content = robot_content
        # The content of the alert notification sent through text message.
        self.sms_content = sms_content
        # The content of the alert resolution notification sent through text message.
        self.sms_recover_content = sms_recover_content
        # The content of the alert notification by phone.
        self.tts_content = tts_content
        # The content of the alert resolution notification by phone.
        self.tts_recover_content = tts_recover_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email_content is not None:
            result['EmailContent'] = self.email_content

        if self.email_recover_content is not None:
            result['EmailRecoverContent'] = self.email_recover_content

        if self.email_recover_title is not None:
            result['EmailRecoverTitle'] = self.email_recover_title

        if self.email_title is not None:
            result['EmailTitle'] = self.email_title

        if self.robot_content is not None:
            result['RobotContent'] = self.robot_content

        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content

        if self.sms_recover_content is not None:
            result['SmsRecoverContent'] = self.sms_recover_content

        if self.tts_content is not None:
            result['TtsContent'] = self.tts_content

        if self.tts_recover_content is not None:
            result['TtsRecoverContent'] = self.tts_recover_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmailContent') is not None:
            self.email_content = m.get('EmailContent')

        if m.get('EmailRecoverContent') is not None:
            self.email_recover_content = m.get('EmailRecoverContent')

        if m.get('EmailRecoverTitle') is not None:
            self.email_recover_title = m.get('EmailRecoverTitle')

        if m.get('EmailTitle') is not None:
            self.email_title = m.get('EmailTitle')

        if m.get('RobotContent') is not None:
            self.robot_content = m.get('RobotContent')

        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')

        if m.get('SmsRecoverContent') is not None:
            self.sms_recover_content = m.get('SmsRecoverContent')

        if m.get('TtsContent') is not None:
            self.tts_content = m.get('TtsContent')

        if m.get('TtsRecoverContent') is not None:
            self.tts_recover_content = m.get('TtsRecoverContent')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule(DaraModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_end_time: str = None,
        notify_objects: List[main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects] = None,
        notify_start_time: str = None,
    ):
        # The notification method.
        self.notify_channels = notify_channels
        # The end time of the notification window.
        self.notify_end_time = notify_end_time
        # An array of notification objects.
        self.notify_objects = notify_objects
        # The start time of the notification window.
        self.notify_start_time = notify_start_time

    def validate(self):
        if self.notify_objects:
            for v1 in self.notify_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        if self.notify_end_time is not None:
            result['NotifyEndTime'] = self.notify_end_time

        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k1 in self.notify_objects:
                result['NotifyObjects'].append(k1.to_map() if k1 else None)

        if self.notify_start_time is not None:
            result['NotifyStartTime'] = self.notify_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')

        if m.get('NotifyEndTime') is not None:
            self.notify_end_time = m.get('NotifyEndTime')

        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k1 in m.get('NotifyObjects'):
                temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k1))

        if m.get('NotifyStartTime') is not None:
            self.notify_start_time = m.get('NotifyStartTime')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects(DaraModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_object_id: int = None,
        notify_object_name: str = None,
        notify_object_type: str = None,
    ):
        # The notification methods specified for a contact.
        self.notify_channels = notify_channels
        # The ID of the notification object.
        self.notify_object_id = notify_object_id
        # The name of the notification object.
        self.notify_object_name = notify_object_name
        # The type of the notification object. Valid values:
        # 
        # *   CONTACT: contact
        # *   CONTACT_GROUP: contact group
        # *   ARMS_CONTACT: ARMS contact
        # *   ARMS_CONTACT_GROUP: ARMS contact group
        # *   DING_ROBOT_GROUP: DingTalk, Lark, WeCom, or IM robot
        # *   CONTACT_SCHEDULE: user on duty defined by a schedule
        self.notify_object_type = notify_object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels

        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id

        if self.notify_object_name is not None:
            result['NotifyObjectName'] = self.notify_object_name

        if self.notify_object_type is not None:
            result['NotifyObjectType'] = self.notify_object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')

        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')

        if m.get('NotifyObjectName') is not None:
            self.notify_object_name = m.get('NotifyObjectName')

        if m.get('NotifyObjectType') is not None:
            self.notify_object_type = m.get('NotifyObjectType')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules(DaraModel):
    def __init__(
        self,
        matching_conditions: List[main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions] = None,
    ):
        # The matching conditions.
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for v1 in self.matching_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k1 in self.matching_conditions:
                result['MatchingConditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k1 in m.get('MatchingConditions'):
                temp_model = main_models.CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k1))

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key of the matching condition.
        self.key = key
        # The logical operator of the matching condition. Valid values:
        # 
        # *   `eq`: equal to
        # *   `neq`: not equal to
        # *   `in`: contains
        # *   `nin`: does not contain
        # *   `re`: regular expression match
        # *   `nre`: regular expression mismatch
        self.operator = operator
        # The value of the matching condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule(DaraModel):
    def __init__(
        self,
        group_interval: int = None,
        group_wait: int = None,
        grouping_fields: List[str] = None,
    ):
        # The time interval of grouping. Unit: seconds. Default value: 30.
        self.group_interval = group_interval
        # The waiting time for grouping. Unit: seconds. Default value: 5.
        self.group_wait = group_wait
        # An array of alert event group objects.
        # 
        # *   If you do not specify the groupingFields field, all alerts will be sent to contacts based on `alertname`.
        # *   If you specify the groupingFields field, alerts with the same field will be sent to contacts in one notification.
        self.grouping_fields = grouping_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval

        if self.group_wait is not None:
            result['GroupWait'] = self.group_wait

        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')

        if m.get('GroupWait') is not None:
            self.group_wait = m.get('GroupWait')

        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')

        return self

