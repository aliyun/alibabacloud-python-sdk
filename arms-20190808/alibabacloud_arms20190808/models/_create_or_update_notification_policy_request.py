# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateNotificationPolicyRequest(DaraModel):
    def __init__(
        self,
        directed_mode: bool = None,
        escalation_policy_id: int = None,
        group_rule: str = None,
        id: int = None,
        integration_id: int = None,
        matching_rules: str = None,
        name: str = None,
        notify_rule: str = None,
        notify_template: str = None,
        region_id: str = None,
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
        # 
        # *   If you do not specify the groupingFields field, all alerts will be sent to contacts based on `alertname`.
        # *   If you specify the groupingFields field, alerts with the same field will be sent to contacts in one notification.
        # 
        # Sample statement:
        # 
        #     { 
        #     "groupWait":5,    // The waiting time for grouping. 
        #     "groupInterval":30,     // The time interval of grouping. 
        #     "groupingFields":["alertname"]       // The field that is used to group alert events. 
        #     }
        self.group_rule = group_rule
        # The ID of the notification policy.
        # 
        # *   If you do not specify this parameter, a new notification policy is created.
        # *   If you specify this parameter, the specified notification policy is modified.
        self.id = id
        # The integration ID of the ticket system to which alerts are pushed.
        self.integration_id = integration_id
        # The matching rules. Format:
        # 
        #     [
        #      {
        #      "matchingConditions": [
        #      { 
        #      "value": "test",    // The value of the matching condition. 
        #      "key": "alertname",     // The key of the matching condition. 
        #      "operator": "eq"   // The logical operator of the matching condition, including eq (equal to), neq (not equal to), in (contains), nin (does not contain), re (regular expression match), and nre (regular expression mismatch).   
        #      }
        #      ]
        #      } 
        #      ]
        self.matching_rules = matching_rules
        # The name of the notification policy.
        # 
        # This parameter is required.
        self.name = name
        # An array of notification rule objects. Format:
        # 
        #     { 
        #      "notifyStartTime":"00:00",      // The start time of the notification window. 
        #      "notifyEndTime":"23:59",       // The end time of the notification window. 
        #      "notifyChannels":["dingTalk", "email", "sms", "tts", "webhook"],       // The notification methods. Valid values: dingTalk, email, sms, tts, and webhook. 
        #      "notifyObjects":[{       // An array of notification objects. 
        #      "notifyObjectType":"CONTACT",       // The type of the notification object. Valid values: CONTACT (contact), CONTACT_GROUP (contact group), ARMS_CONTACT (ARMS contact), ARMS_CONTACT_GROUP (ARMS contact group), DING_ROBOT_GROUP (DingTalk, Lark, WeCom, or IM robot), and CONTACT_SCHEDULE (user on duty defined by a schedule). 
        #      "notifyObjectId":123,       // The ID of the notification object. 
        #      "notifyObjectName":"test"       // The name of the notification object. 
        #      }]
        # 
        # This parameter is required.
        self.notify_rule = notify_rule
        # The notification template. The default notification template is provided below the table.
        self.notify_template = notify_template
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to resend a notification for a long-lasting unresolved alert. Default value: true. Valid values:
        # 
        # *   `true`: If you set this parameter to `true`, you must set **RepeatInterval**.
        # *   `false`: If you set this parameter to `false`, you must set **EscalationPolicyId**.
        self.repeat = repeat
        # The time interval at which a notification is resent for a long-lasting unresolved alert. Unit: seconds.
        self.repeat_interval = repeat_interval
        # Specifies whether the status of an alert automatically changes to Resolved when all events related to the alert change to the Restored state. ARMS notifies contacts when the alert status changes to Resolved.
        # 
        # *   `true`: The system sends a notification.
        # *   `false`: The system does not send a notification.
        self.send_recover_message = send_recover_message
        # Specifies whether to enable the notification policy. Valid values: enable and disable.
        self.state = state

    def validate(self):
        pass

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
            result['GroupRule'] = self.group_rule

        if self.id is not None:
            result['Id'] = self.id

        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id

        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules

        if self.name is not None:
            result['Name'] = self.name

        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule

        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
            self.group_rule = m.get('GroupRule')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')

        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyRule') is not None:
            self.notify_rule = m.get('NotifyRule')

        if m.get('NotifyTemplate') is not None:
            self.notify_template = m.get('NotifyTemplate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

