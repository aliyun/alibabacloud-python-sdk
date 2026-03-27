# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AlertRuleNotificationFilter(DaraModel):
    def __init__(
        self,
        contacts: List[str] = None,
        custom_webhooks: List[str] = None,
        ding_webhooks: List[str] = None,
        fs_webhooks: List[str] = None,
        groups: List[str] = None,
        slack_webhooks: List[str] = None,
        wx_webhooks: List[str] = None,
    ):
        self.contacts = contacts
        self.custom_webhooks = custom_webhooks
        self.ding_webhooks = ding_webhooks
        self.fs_webhooks = fs_webhooks
        self.groups = groups
        self.slack_webhooks = slack_webhooks
        self.wx_webhooks = wx_webhooks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.custom_webhooks is not None:
            result['customWebhooks'] = self.custom_webhooks

        if self.ding_webhooks is not None:
            result['dingWebhooks'] = self.ding_webhooks

        if self.fs_webhooks is not None:
            result['fsWebhooks'] = self.fs_webhooks

        if self.groups is not None:
            result['groups'] = self.groups

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

        if m.get('dingWebhooks') is not None:
            self.ding_webhooks = m.get('dingWebhooks')

        if m.get('fsWebhooks') is not None:
            self.fs_webhooks = m.get('fsWebhooks')

        if m.get('groups') is not None:
            self.groups = m.get('groups')

        if m.get('slackWebhooks') is not None:
            self.slack_webhooks = m.get('slackWebhooks')

        if m.get('wxWebhooks') is not None:
            self.wx_webhooks = m.get('wxWebhooks')

        return self

