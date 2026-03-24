# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

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
        silence_time: int = None,
        slack_webhooks: List[str] = None,
        wx_webhooks: List[str] = None,
    ):
        self.contacts = contacts
        self.custom_webhooks = custom_webhooks
        self.ding_cool_app_webhooks = ding_cool_app_webhooks
        self.ding_webhooks = ding_webhooks
        self.fs_webhooks = fs_webhooks
        self.groups = groups
        self.notify_time = notify_time
        self.silence_time = silence_time
        self.slack_webhooks = slack_webhooks
        self.wx_webhooks = wx_webhooks

    def validate(self):
        if self.notify_time:
            self.notify_time.validate()

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

        if m.get('silenceTime') is not None:
            self.silence_time = m.get('silenceTime')

        if m.get('slackWebhooks') is not None:
            self.slack_webhooks = m.get('slackWebhooks')

        if m.get('wxWebhooks') is not None:
            self.wx_webhooks = m.get('wxWebhooks')

        return self

