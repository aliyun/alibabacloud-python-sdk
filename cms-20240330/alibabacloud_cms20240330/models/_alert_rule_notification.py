# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleNotification(DaraModel):
    def __init__(
        self,
        contacts: List[str] = None,
        custom_webhooks: List[str] = None,
        ding_cool_app_webhooks: List[str] = None,
        ding_webhooks: List[str] = None,
        fs_webhooks: List[str] = None,
        groups: List[str] = None,
        notify_time: main_models.AlertRuleTimeSpan = None,
        qwencloud_contacts: Dict[str, dict] = None,
        send_ok: bool = None,
        severity_notifications: Dict[str, main_models.SeverityNotifyConfig] = None,
        silence_time: int = None,
        slack_webhooks: List[str] = None,
        wx_webhooks: List[str] = None,
    ):
        # The list of contact IDs.
        self.contacts = contacts
        # The list of custom webhook Notification Recipient IDs.
        self.custom_webhooks = custom_webhooks
        # The list of DingTalk Cool App webhook Notification Recipient IDs.
        self.ding_cool_app_webhooks = ding_cool_app_webhooks
        # The list of DingTalk webhook Notification Recipient IDs.
        self.ding_webhooks = ding_webhooks
        # The list of Lark webhook Notification Recipient IDs.
        self.fs_webhooks = fs_webhooks
        # The list of contact group IDs.
        self.groups = groups
        # The notification time period. Notifications are sent only during this time period.
        self.notify_time = notify_time
        self.qwencloud_contacts = qwencloud_contacts
        self.send_ok = send_ok
        self.severity_notifications = severity_notifications
        # The notification mute duration, in seconds.
        self.silence_time = silence_time
        # The list of Slack webhook Notification Recipient IDs.
        self.slack_webhooks = slack_webhooks
        # The list of WeChat webhook Notification Recipient IDs.
        self.wx_webhooks = wx_webhooks

    def validate(self):
        if self.notify_time:
            self.notify_time.validate()
        if self.severity_notifications:
            for v1 in self.severity_notifications.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.custom_webhooks is not None:
            result['customWebhooks'] = self.custom_webhooks

        if self.ding_cool_app_webhooks is not None:
            result['dingCoolAppWebhooks'] = self.ding_cool_app_webhooks

        if self.ding_webhooks is not None:
            result['dingWebhooks'] = self.ding_webhooks

        if self.fs_webhooks is not None:
            result['fsWebhooks'] = self.fs_webhooks

        if self.groups is not None:
            result['groups'] = self.groups

        if self.notify_time is not None:
            result['notifyTime'] = self.notify_time.to_map()

        if self.qwencloud_contacts is not None:
            result['qwencloudContacts'] = self.qwencloud_contacts

        if self.send_ok is not None:
            result['sendOk'] = self.send_ok

        result['severityNotifications'] = {}
        if self.severity_notifications is not None:
            for k1, v1 in self.severity_notifications.items():
                result['severityNotifications'][k1] = v1.to_map() if v1 else None

        if self.silence_time is not None:
            result['silenceTime'] = self.silence_time

        if self.slack_webhooks is not None:
            result['slackWebhooks'] = self.slack_webhooks

        if self.wx_webhooks is not None:
            result['wxWebhooks'] = self.wx_webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('customWebhooks') is not None:
            self.custom_webhooks = m.get('customWebhooks')

        if m.get('dingCoolAppWebhooks') is not None:
            self.ding_cool_app_webhooks = m.get('dingCoolAppWebhooks')

        if m.get('dingWebhooks') is not None:
            self.ding_webhooks = m.get('dingWebhooks')

        if m.get('fsWebhooks') is not None:
            self.fs_webhooks = m.get('fsWebhooks')

        if m.get('groups') is not None:
            self.groups = m.get('groups')

        if m.get('notifyTime') is not None:
            temp_model = main_models.AlertRuleTimeSpan()
            self.notify_time = temp_model.from_map(m.get('notifyTime'))

        if m.get('qwencloudContacts') is not None:
            self.qwencloud_contacts = m.get('qwencloudContacts')

        if m.get('sendOk') is not None:
            self.send_ok = m.get('sendOk')

        self.severity_notifications = {}
        if m.get('severityNotifications') is not None:
            for k1, v1 in m.get('severityNotifications').items():
                temp_model = main_models.SeverityNotifyConfig()
                self.severity_notifications[k1] = temp_model.from_map(v1)

        if m.get('silenceTime') is not None:
            self.silence_time = m.get('silenceTime')

        if m.get('slackWebhooks') is not None:
            self.slack_webhooks = m.get('slackWebhooks')

        if m.get('wxWebhooks') is not None:
            self.wx_webhooks = m.get('wxWebhooks')

        return self

